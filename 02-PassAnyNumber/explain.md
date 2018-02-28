#传递任意数量的实参
形参中加入 `*`(一个)可以使其创建一个同名元组  
eg:
```python
def add_material(*materials):
    '''打印客户需要的材料'''
    print('The custom wanna')
    for material in materials:
        print(material)

add_material('beef','pork','chicken')
```

形参中加入`**`(两个)可以使其长剑一个同名的字典
```python
def bulid_profile(first, last, **user_info):
    '''获取用户信息,在形参阶段创建一个字典获取姓名'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = bulid_profile('lucy', 'dick', location='American', field='biology')
print(user_profile)
```
**特别注意**  
当通过`**`生成字典时，实参格式略有不同，其“key”位置无单(双)引号，如上述代码  
`user_profile = bulid_profile('lucy', 'dick', location='American', field='biology')`
但是输出时，其存在字符类型的单引号  

![mark](http://p4ihydscy.bkt.clouddn.com/blog/180228/k5kCG4Icfj.png?imageslim)