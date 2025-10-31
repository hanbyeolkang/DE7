from __future__ import annotations
from airflow import DAG
from airflow.models import Variable
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task

from datetime import datetime
from datetime import timedelta

import requests
import logging
import psycopg2
from typing import Any


def get_Redshift_connection(autocommit=True):
    hook = PostgresHook(postgres_conn_id='redshift_dev_db')
    conn = hook.get_conn()
    conn.autocommit = autocommit
    return conn.cursor()


@task
def extract(url):
    logging.info("extract 시작")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API 호출 중 오류 발생: {e}")
        raise


@task
def transform(country_list):
    logging.info(f"transform 시작. 총 {len(country_list)}개 국가 처리 예정.")
    records = []

    for country in country_list:
        official_name = country.get('name', {}).get('official').replace("'", "''")
        population = country.get('population')
        area = country.get('area')
        records.append((official_name, population, area))

    logging.info(f"transform 완료. 추출된 데이터: {len(records)}개")
    return records


@task
def load(schema, table, records):
    logging.info("load 시작")    
    cur = get_Redshift_connection()

    try:
        cur.execute("BEGIN;")

        # 1. 테이블 구조 생성 (IF NOT EXISTS)
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {schema}.{table} (
            country VARCHAR(256),
            population BIGINT,
            area FLOAT,
            loaded_at TIMESTAMP DEFAULT GETDATE()
        );
        """
        cur.execute(create_table_sql)
        logging.info(f"{table} 생성 완료")

        # 2. 기존 데이터 삭제 (Full Refresh)
        delete_sql = f"DELETE FROM {schema}.{table};"
        cur.execute(delete_sql)
        logging.info(f"{table} 기존 데이터 삭제 완료")

        # 3. INSERT 수행
        for r in records:
            country = r[0]
            population = r[1]
            area = r[2]
            insert_sql = f"INSERT INTO {schema}.{table} VALUES ('{country}', {population}, {area});"
            cur.execute(insert_sql)

        cur.execute("COMMIT;")   # cur.execute("END;") 
        logging.info(f"{table}에 {len(records)}건의 데이터 삽입 완료")

    except Exception as e:
        logging.error(f"Redshift 로드 중 오류 발생: {e}")
        cur.execute("ROLLBACK;")
        raise


with DAG(
    dag_id='country_api',
    start_date=datetime(2025, 1, 1),
    schedule='30 6 * * 6', # 매주 토요일 6시 30분 (UTC)
    max_active_runs=1,
    catchup=False,
    default_args={
        'retries': 1,
        'retry_delay': timedelta(minutes=3),
    }
) as dag:

    url = Variable.get("restcountries_url")
    schema = 'strongstar1210'
    table = 'country'

    records = transform(extract(url))
    load(schema, table, records)