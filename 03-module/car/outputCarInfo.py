#import makeCarFunction
#from makeCarFunction import make_car
#from makeCarFunction import make_car as MC
#import makeCarFunction as MCF
from makeCarFunction import *

#从模块调用函数并执行
info = make_car('BMW','X5',seat = '5',value = '173W')
print(info)
