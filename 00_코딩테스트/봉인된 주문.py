# 알파벳을 26진법으로 생각하기
def solution(n, bans):
    # a -> 1, b -> 2 ... aa -> 27, ab -> 28
    def str_to_num(s):
        num = 0
        for i, char in enumerate(reversed(s)):
            num += (ord(char) - ord('a') + 1) * (26 ** i)
        return num
    
    # 1 -> a, 2 -> b ... 27 -> aa, 28 -> ab
    def num_to_str(num):
        res = []
        while num > 0:
            num, rem = divmod(num - 1, 26)
            res.append(chr(ord('a') + rem))
        return "".join(reversed(res))
    
    # 삭제할 주문들을 숫자로 바꿔서 정렬
    ban_nums = sorted([str_to_num(b) for b in bans])

    # 삭제된 주문 만큼 n값 보정해주기
    for b in ban_nums:
        if b <= n:
            n += 1
        else:
            break

    return num_to_str(n)


n = 30
bans = ["d", "e", "bb", "aa", "ae"]
print(solution(n, bans))    # 예상 결과 : ah

# https://school.programmers.co.kr/learn/courses/30/lessons/389481