from decimal import Decimal, getcontext

getcontext().prec = 100

a, b, c = map(Decimal, input().split())

print(f'{(a * b / c):.18f}')
