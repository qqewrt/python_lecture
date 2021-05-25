def sum_nums(*args):
    total = 0
    for i in args:
        total += i
    avg = total /len(args)
    print(f'{len(args)}개의 인자 {args}')
    return total, avg

sum_nums(10,20,30)
print(f'합계 : {total} , 평균 : {avg}')

sum_nums(10,20,30,40,50)
print(f'합계 : {total} , 평균 : {avg}')

