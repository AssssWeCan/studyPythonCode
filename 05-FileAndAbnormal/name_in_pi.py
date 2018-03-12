def downtext(filename):
    with open(filename) as file_object:
        lines = file_object.readlines()
        #获取文件存储文件于lines
    pi_number = ''
    for line in lines:
        pi_number += line.strip()
    return pi_number
    #圆周率完整存储在了pi_number上

def judge(birthday,pi_number):
    '''判断是否存在圆周率中'''
    if birthday in pi_number:
        print('yes')
    else:
        print('no')

local_adress = r'C:\Users\42582\Desktop\pcc-master\pcc-master\chapter_10\pi_million_digits.txt'
pi_million_number = downtext(local_adress)
day_data = input('tell me your birthday: \n')
judge(day_data,pi_million_number)