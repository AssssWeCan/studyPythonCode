while True:
    first_number = input('first number:  ')
    #输入数字
    if first_number == 'quit':
        break
    second_number = input('second number:  ')
    if second_number == 'quit':
        break
    try:
        result = int(first_number)/int(second_number)
        #计算加法结果
        print(result)
    except ValueError:
        #错误时打印信息
        print("please input integer!!!")
