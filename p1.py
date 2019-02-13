def f(a, b, x):
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        '%': a % b,
        '^': a ** b,
    }[x]

A = int(raw_input("\n\nPress FIRST number: "));
B = int(raw_input("\n\nPress SECOND number: "));
O = raw_input("\n\nPress OPERATOR: ");

print(f(A, B, O));