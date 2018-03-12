import json

#询问并保存用户喜欢的数字
def remember_number():
    filename = r'C:\Users\42582\Desktop\pcc-master\favourite_number.txt'
    number = input('tell me your favourite number:  ')
    with open(filename,'w') as file_object:
        json.dump(number,file_object)