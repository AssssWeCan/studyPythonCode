import json

#打印用户喜欢的数字
def output_number():
    filename = r'C:\Users\42582\Desktop\pcc-master\favourite_number.txt'
    with open(filename) as file_object:
        number = json.load(file_object)
    print(number)