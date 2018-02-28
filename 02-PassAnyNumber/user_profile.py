def bulid_profile(first, last, **user_info):
    '''获取用户信息,在形参阶段创建一个字典获取姓名'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = bulid_profile('lucy', 'dick', location='American', field='biology')
print(user_profile)