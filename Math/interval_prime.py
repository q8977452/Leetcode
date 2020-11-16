def interval_prime(lower,upper):
    '''
    lower : 下界
    upper : 上屆
    a : list 儲存上下界間的質數
    '''
    a = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                a.append(num)
    return a
