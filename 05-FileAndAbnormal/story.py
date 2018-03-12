filename = r'C:\Users\42582\Desktop\pcc-master\story.txt'
content = ''
#打开story并读取
with open(filename) as F_obj:
    lines = F_obj.readlines()
    for line in lines:
        content += line.rstrip()
#全部处理为小写,并统计单词出现频率
content = content.lower()
number = content.count('child')
print(number)