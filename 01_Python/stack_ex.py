class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    postfixList = []
    opStack = ArrayStack()
    
    for token in tokenList:
        if str(token).isnumeric():
            postfixList.append(token)
        elif token == '(':
            opStack.push('(')
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()   # '(' 버리기
        else:
            while not opStack.isEmpty():
                if prec[token] <= prec[opStack.peek()]:
                    o = opStack.pop()
                    if o != '(':
                        postfixList.append(opStack.pop())
                else:
                    break
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        
    return postfixList


def postfixEval(tokenList):
    s = ArrayStack()
    for token in tokenList:
        if str(token).isnumeric():
            s.push(token)
        else:
            num1 = s.pop()
            num2 = s.pop()
            if token == '+':
                s.push(num1 + num2)
            elif token == '-':
                s.push(num2 - num1) # 순서 주의
            elif token == '*':
                s.push(num1 * num2)
            elif token == '/':
                s.push(num2 / num1) # 순서 주의
    return s.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


expr = "7 * (9 - (3+2))"
answer = solution(expr)
print(answer)