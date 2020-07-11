'''
显示哪些成员没有完成

    filename = 'demo.txt'
    testname = 'demo_test.txt'
'''
print('请将当前成员填入current.txt中')
filename = input('请输入全体成员文件名\n')


all_member = set()

with open(filename, 'r',encoding='utf-8') as f:
    each_member = f.readline()

    while each_member:
        all_member.add(each_member[0:-1])
        each_member = f.readline()

current_member = set()
with open('current.txt', 'r',encoding='utf-8') as f:
    each_member = f.readline()

    while each_member:
        current_member.add(each_member[0:-1])
        each_member = f.readline()


result = all_member - current_member
for each in result:
    print(each)


need = input('需要反向比较？y/n')
if need == 'y':
    result = current_member - all_member
    for each in result:
        print(each)
