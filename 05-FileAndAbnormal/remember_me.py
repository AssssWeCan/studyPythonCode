import json

def get_users_name():
    '''尝试获取文件中的用户名'''
    filename = r'C:\Users\42582\Desktop\pcc-master\pcc-master\chapter_10\remember_me.txt'
    try:
        with open(filename) as file_object:
            user_name = json.load(file_object)
    except:
        return None
    else:
        return user_name

def get_new_username():
    '''创建新的用户名'''
    filename = r'C:\Users\42582\Desktop\pcc-master\pcc-master\chapter_10\remember_me.txt'
    user_name = input('please tell me your name:  ')
    with open(filename, 'w') as file_object:
        json.dump(user_name, file_object)
    return user_name

def greet_users():
    '''判断是否存在用户名，不存在则创建新的用户'''
    user_name = get_users_name()
    now_username = input('tell me your name and I will check')
    if user_name and now_username == user_name:
        print('Welcome back ' + user_name)
    else:
        user_name = get_new_username()
        print('I will remember you ' + user_name)

greet_users()