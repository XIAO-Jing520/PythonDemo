'''
显示两组成员的差别

    以空行作为不同成员的分割

'''
print('请将当前成员填入current.txt中')
filename = input('请输入全体成员文件名\n')
filename = "454_.txt"
all_members = set()

with open(filename, 'r', encoding='UTF-8') as f:
    each_member = f.readline()
    new_member = "" # 初始化
    while each_member:
        new_member += each_member[:-1]

        if each_member == "\n":
            if new_member != "":
                all_members.add(new_member + "\n\n")
                new_member = ""
            
        
        each_member = f.readline()

current_members = set()
with open('current.txt', 'r', encoding='UTF-8') as f:
    each_member = f.readline()
    new_member = "" # 初始化
    while each_member:
        new_member += each_member[:-1]

        if each_member == "\n":
            current_members.add(new_member + "\n\n")
            new_member = ""
            
        
        each_member = f.readline()



result = all_members - current_members
print("缺少项有：",len(result))
print("结果保存在 res.txt 中")
with open("res.txt","w", encoding='UTF-8') as f:
    for each in result:
        f.write(each)


need = input('需要反向比较？y/n')

if need == 'y':
    result = current_members - all_members
    print("结果保存在 ires.txt 中")
    print("缺少项有：",len(result))
    with open("ires.txt","w", encoding='UTF-8') as f:
        for each in result:
            f.write(each)
