'''
删除无效空行

    以空行作为不同成员的分割

'''

filename = input('请输入需要重整的文件\n')
all_members = list()
filename = "0.txt"
with open(filename, 'r', encoding='UTF-8') as f:
    each_member = f.readline()
    new_member = "" # 初始化
    while each_member:
        new_member += each_member[:-1]

        if each_member == "\n":
            if (new_member + "\n\n" ) in all_members:
                print("重复行：", new_member + "\n\n")
            # if new_member != "": 
            else:  
                all_members.append(new_member + "\n\n")
                new_member = ""
            
        
        each_member = f.readline()


with open("res3.txt","w", encoding='UTF-8') as f:
    for each in all_members:
        f.write(each)


