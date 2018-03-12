while True:
    filename = r'C:\Users\42582\Desktop\pcc-master\Users_language.txt'
    User_language = input('please tell me your favourate LANGUAGE： \n')
    if User_language == 'break':
        break
    with open(filename,'a') as file_object:
        file_object.write(User_language + '\n')
    #存入受访者最喜欢的语言


    with open(filename) as  file_object_read:
        lines = file_object_read.readlines()
        for line in lines:
            print(line.rstrip())
    #打印所有已存在语言
