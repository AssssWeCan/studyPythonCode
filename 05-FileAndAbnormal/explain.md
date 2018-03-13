#文件与异常
###读取与写入
python可以读取打开文件并读取其内容
如下面代码
```python
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
```
* 使用`with`可以在你不需要继续访问文件时将它关闭。在这里我们调用了`open()`但是并没有调用`close()`；当然我们亦可以这么用，但是如果程序出现bug时，会可能导致`close()`没有执行，文件将不会被关闭，可能导致文件丢失。  
* `open`可以打开文件，括号中只填写文件地址，则文件只能读取，不能进行写入操作。`open(filename,'r')`为*读取模式*，`'w'`为*写入模式*（写入并覆盖以前内容）,`'a'`为*附加模式*（写入并加入以前内容之后）、`'r+'`为*读取和写入模式  
* 文件使用`open()`后，使用`as`对文件对象命名`f_obj`，对f_obj进行`read()`之后才能对文件内容进行处理，逐行读取时，使用`readlines()`方法
* 文件读取每完成一次，会自动在最后加上一个换行符，使用`rstrip()`可以去掉
* windows环境下，会出现转义问题，需要在文件地址前加一个r

###异常
Python文件出现异常时，会出现traceback代码块，包含异常报告，显示出你的程序中文件的名称，看到你不能运行的代码，对一个攻击者来说可以判断出需要对你的代码的攻击方式
```python
def open_and_read(filename):
    """打开文件并逐行打印文件内容"""
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                article = line.rstrip()
    except FileNotFoundError:
#    print('illegal file location')
        pass
    else:
        print(article)
f_names = ['C:\\Users\\42582\\Desktop\\pcc-master\\cats.txt','C:\\Users\\42582\\Desktop\\pcc-master\\dogs.txt']
for f_name in f_names:
    open_and_read(f_name)
```
* 将文件地址组成列表，可以用循环让同一个函数读取不同的文件
* `try-escept-else`可以让程序先试图运行`try`中的代码块，当出现`except`中描述的错误时，运行`except`中的代码块。若`try`中成功运行，则跳过`except`中代码块。继续运行`else`
* `except`其后可以不写错误类型，则`try`出**任何**错时都会运行`except`中的代码
* 要让代码出现失败时一声不吭，则只用在`except`后的代码块运行`pass`
###使用json存储数据
使用`import json`导入json，通过 XXX.json 文件存储数据
```python
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
    '''判断是否存在用户名且用户名相同，不存在或不相同则创建新的用户'''
    user_name = get_users_name()
    now_username = input('tell me your name and I will check')
    if user_name and now_username == user_name:
        print('Welcome back ' + user_name)
    else:
        user_name = get_new_username()
        print('I will remember you ' + user_name)

greet_users()
```
* `json.dump(content, file_object)`可以将内容（content），存储到文件中（file_object）
* `content = json.load(file_object)`可以将文件读取出来，并存储到代码中（content）
* 代码需要重构，重构的目的是编写出易于维护且容易拓展的代码