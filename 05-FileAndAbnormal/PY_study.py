filename = r'C:\Users\42582\Desktop\pcc-master\py_study.txt'
with open(filename) as file_object:
    file_content0 = file_object.read()
    file_content0 = file_content0.replace('A', 'AAAA')
print(file_content0.rstrip())
print('1\n')
#全片打印文件内容

with open(filename) as file_object:
    for line in file_object:
        line = line.replace('A', 'xxxxxxxxxxxxx')
        print(line.rstrip())
print('2\n')
#遍历打印文件内容

with open(filename) as file_object:
    file_content1 = file_object
    for line in file_content1:
        line = line.replace('Python', '___')
        print(line.rstrip())
print('3')
#存入列表后再打印
message = 'python'
print(message.replace('python','c'))