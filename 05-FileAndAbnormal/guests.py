def guest():
    '''保存姓名并访问'''
    while True:
        user = input('please input yor account: \n')
        if user == 'quit':
            break
        filename = r'C:\Users\42582\Desktop\pcc-master\Users_name.txt'
        with open(filename,'a') as file_object:
            file_object.write(user + '\n')
        print('hello ' + user)

guest()