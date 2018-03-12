def open_and_read(filename):
    """打开文件并逐行打印文件内容"""
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
#    print('illegal file location')
        pass
f_names = ['C:\\Users\\42582\\Desktop\\pcc-master\\cats.txt','C:\\Users\\42582\\Desktop\\pcc-master\\dogs.txt']
for f_name in f_names:
    open_and_read(f_name)
