#模块化存储函数  
```python
def make_car(maker,model,**cars):
    '''将一个汽车的信息储存在字典中'''
    car_info={}
    car_info['maker'] = maker
    car_info['model'] = model
    for key,value in cars.items():
        car_info[key] = value
    return car_info
```
```python
import makeCarFunction
#通过模块调用函数
info = makeCarFunction.make_car('BMW','X5',seat = '5',value = '173W')
print(info)
```
将函数存储在独立文件中（模块），再将函数导入主程序中:  
`import makeCarFunction`  
使用时需要声明模块名称，即：  
`makeCarFunction.make_car('BMW','X5',seat = '5',value = '173W')`  

导入模块中函数除了上述方法，还有很多其他方法，但是函数使用时略有不同:  
1.  `from makeCarFunction import make_car`  
&nbsp;不需要声明模块名称  
2.  `from makeCarFunction import make_car as MC`  
&nbsp;不需要声明模块名称,且函数名在此程序中替换为MC 
3.  `import makeCarFunction as MCF`  
&nbsp;需要声明模块名，但模块名在此程序中替换为MCF
4.  `from makeCarFunction import *`  
&nbsp;引入此模块中所有的函数  


##附  
pycharm中，import自己的模块会出现报错情况，pycharm不会将你的当前文件目录加入source_path,只要将文件夹手动添加source_path到就可以愉快玩耍了  
![mark](http://p4ihydscy.bkt.clouddn.com/blog/180301/H45mib5Ib0.png?imageslim)