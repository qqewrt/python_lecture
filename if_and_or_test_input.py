a = int(input ("a를 입력하세요."))
print(type(a))
b = int (input ("b를 입력하세요."))
print(type(b))
if (a%2==0)and(b%2==0):
    print('두 수 모두 짝수입니다.')
if (a%2==0)or(b%2==0):
    print('두 수 중 하나 이상이 짝수입니다.')