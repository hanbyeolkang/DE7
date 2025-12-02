import copy

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def changeWord(currWord, target, words, cnt):
        if currWord == target:
            nonlocal minCnt
            minCnt = min(minCnt, cnt)
            return

        availableWords = []
        for word in words:
            diffCnt = 0
            for i in range(len(currWord)):
                if currWord[i] != word[i]:
                    diffCnt += 1
            if diffCnt == 1:
                availableWords.append(word)

        for word in availableWords:
            newWords = copy.deepcopy(words)
            newWords.remove(word)
            changeWord(word, target, newWords, cnt+1)


    minCnt = float('inf')
    changeWord(begin, target, words, 0)

    if minCnt == float('inf'):
        return 0 
    else:
        return minCnt


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))   # 예상 결과 : 4

# https://school.programmers.co.kr/learn/courses/30/lessons/43163