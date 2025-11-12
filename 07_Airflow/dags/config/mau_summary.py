{
          'table': 'mau_summary',
          'schema': 'strongstar1210',
          'main_sql': """
SELECT LEFT(ST.ts, 7) as month,
  COUNT(DISTINCT USC.userid) AS user_count
FROM raw_data.user_session_channel AS USC
JOIN raw_data.session_timestamp AS ST ON USC.sessionid = ST.sessionid
GROUP BY month
ORDER BY month;""",
          'input_check':
          [
            {
              'sql': 'SELECT COUNT(1) FROM raw_data.user_session_channel',
              'count': 10000
            },
          ],
          'output_check':
          [
            {
              'sql': 'SELECT COUNT(1) FROM {schema}.temp_{table}',
              'count': 1
            }
          ],
}
