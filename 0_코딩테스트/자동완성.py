def solution(words):
    words.sort()

    prefix_set = set()
    for i in range(1, len(words)):
        w1, w2 = words[i-1], words[i]
        for j in range(1, min(len(w1), len(w2))+1):
            if w1[:j] == w2[:j]:
                prefix_set.add(w1[:j])
            else:
                break;

    answer = 0
    for w in words:
        for i in range(1, len(w)+1):
            answer += 1
            if w[:i] not in prefix_set:
                break;
    
    return answer


words = ["word", "war", "warrior", "world"]
print(solution(words))  # 예상 결과 : 15

# https://school.programmers.co.kr/learn/courses/30/lessons/17685