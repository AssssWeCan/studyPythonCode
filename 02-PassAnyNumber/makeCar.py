def make_car(maker,model,**cars):
    '''将一个汽车的信息储存在字典中'''
    car_info={}
    car_info['maker'] = maker
    car_info['model'] = model
    for key,value in cars.items():
        car_info[key] = value
    return car_info

info = make_car('BMW','X5',seat = '5',value = '173W')
print(info)