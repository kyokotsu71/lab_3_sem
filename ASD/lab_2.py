# На вход подаётся математическое выражение. Элементы - числа. Операции - "+ - * /".
# Также есть скобочки. Окончанием выражения служит "=". Программа должна вывести результат выражения
# Пример ввода:
# 2+7*(3/9)-5=
# Замечание:
# Программа также должна делать "проверку на дурака": нет деления на 0, все скобки стоят верно (см лабу №1) и т.п.

string = (input())
stack = []
s_right = True
z_right = True

operands = []
    operators = []
    current_operand = ""
    for char in string:
        if char.isdigit() or char == ".":
            current_operand += char
        else:
            if current_operand:
                operands.append(float(current_operand))
                current_operand = ""
            if char in "+-*/":
                operators.append(char)

    if current_operand:
        operands.append(float(current_operand))

    while operators:
        operator = operators.pop(0)
        if operator == "*":
            operands[0] = operands[0] * operands[1]
        elif operator == "/":
            operands[0] = operands[0] / operands[1]
        elif operator == "+":
            operands[0] = operands[0] + operands[1]
        elif operator == "-":
            operands[0] = operands[0] - operands[1]
        operands.pop(1)

if string[len(string)-1] == '=':
    string = string[:-1]
else:
    print('Введите = как окончание выражения')
    exit()

for i in string:
    if i in '([{':
        stack.append(i)
    if i in ')]}':
        if not stack:
            s_right = False
            break
        pop = stack.pop()
        if pop == '(' and i == ')':
            continue
        if pop == '[' and i == ']':
            continue
        if pop == '{' and i == '}':
            continue
        s_right = False
        break

    if i == '/':
        if string[string.index(i) + 1] == '0':
            z_right = False
            break

if s_right and z_right and not stack:
    print(eval(string))
elif not s_right or stack:
    print('Ошибка: неправильно расставлены скобки')
elif not z_right:
    print('Ошибка: деление на 0')

