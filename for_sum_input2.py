#어떤 수를 입력 받아 그 수까지의 합을 구하여라.
n = int(input('값을 입력하세요.'))
a=0
for i in range(1,n+1):
    a += i
print(a)
print(f"1부터 {n}까지의 합은 {a}입니다.")