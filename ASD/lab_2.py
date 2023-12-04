from sys import exit


def bracket_check(input):
    flag = True
    bracket = []
    for i in text:
        if i == '(':
            bracket.append(i)
        elif i in ')':
            if not bracket:
                flag = False
                break
            pop = bracket.pop()
            if pop == '(' and i == ')':
                continue
            else:
                flag = False
                print('Строка не существует')
                exit(1)


def priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return 0


def do_operation():
    op = operation.pop()
    right = number.pop()
    left = number.pop()
    if op == '+':
        number.append(left + right)
    elif op == '-':
        number.append(left - right)
    elif op == '*':
        number.append(left * right)
    elif op == '/':
        try:
            number.append(left / right)
        except ZeroDivisionError:
            print('Нельзя делить на ноль')
            exit(1)


text = input()
if text[-1] != '=':
    exit('Не стоит = в конце')
bracket_check(text)

number = []
operation = []
i = 0
while i < len(text):
    if text[i].isdigit():
        j = i + 1
        while j < len(text) and (text[j].isdigit() or text[j] == '.'):
            j += 1
        number.append(float(text[i:j]))
        i = j
    elif text[i] == '(':
        operation.append(text[i])
        i += 1
    elif text[i] == ')':
        while operation[-1] != '(':
            do_operation()
        operation.pop()
        i += 1
    elif text[i] == '+' or text[i] == '-' or text[i] == '*' or text[i] == '/':
        while len(operation) > 0 and priority(operation[-1]) >= priority(text[i]):
            do_operation()
        operation.append(text[i])
        i += 1
    else:
        i += 1
while len(operation) > 0:
    do_operation()
print(number[0])
