'''
最终结果：
“zstp10_gxcz1d2_NODERELNODE.csv”
“zstp10_gxcz1d2_ALL_LABLE.csv”
“zstp10_gxcz1d2_ALL_DESCRIBE.csv”
“zstp10_gxcz1d2_NODE_REL_NODE_NO.csv”

第一阶段：分离出具有确定的
1.先把数据集根据【TheLabel】分成两份，一份不包含“zstp10_gxcz1d2_without_lable.csv”，
        一份是全label,“zstp10_gxcz1d2_ALL_LABLE.csv”，用于日后的添加
2.在“zstp10_gxcz1d2_without_lable.csv”分离出【describe】，“zstp10_gxcz1d2_ALL_DESCRIBE.csv”，
和去掉describe的文件“zstp10_gxcz1d2_without_lableAndDescribe.csv”

3.在“zstp10_gxcz1d2_without_lableAndDescribe.csv”中，分离出包含“createrelation2020.csv”中出现的关系的数据到
    “zstp10_gxcz1d2_NODE_REL_NODE_YSE.csv”,；
    没出现的放入“zstp10_gxcz1d2_node_re_node_DONT_KNOW.csv”

第二阶段：
4.在“zstp10_gxcz1d2_node_re_node_DONT_KNOW.csv”的进一步分离：
在‘finall2020.csv’中得到结点集合，在“zstp10_gxcz1d2_node_re_node_DONT_KNOW.csv”遍历，是否客体属于节点集合中一员,是
则放入“zstp10_gxcz1d2_NODE_REL_NODE_YSE.csv”,没出现的放入“zstp10_gxcz1d2_node_re_node_DONT_KNOW.csv”

5.在“zstp10_gxcz1d2_node_re_node_DONT_KNOW2.csv”中分离出“zstp10_gxcz1d2_NODE_REL_NODE_YSE2.csv”中的节点连接，称为
“zstp10_gxcz1d2_NODE_REL_NODE_YSE3.csv”，其他的写入“zstp10_gxcz1d2_NODE_REL_NODE_NO.csv”

6.将“zstp10_gxcz1d2_NODE_REL_NODE_YSE.csv”“zstp10_gxcz1d2_NODE_REL_NODE_YSE2.csv”“zstp10_gxcz1d2_NODE_REL_NODE_YSE3.csv”三个文件
合并到“zstp10_gxcz1d2_NODERELNODE.csv”
'''
def A():
    with open('./data/zstp10_gxcz1d2_ALL_LABLE.csv', 'a+', encoding='utf-8') as ff:
        with open('./data/zstp10_gxcz1d2_without_lable.csv','a+',encoding='utf-8') as f:
            with open('./data/finall2020.csv','r',encoding='utf-8') as r:
                for line in r:
                    row=line.split(',')
                    if row[1]!='TheLabel':
                        f.write(line)
                    else:
                        ff.write(line)
    print("A_done!")
def B():
    with open('./data/zstp10_gxcz1d2_ALL_DESCRIBE.csv', 'a+', encoding='utf-8') as ff:
        with open('./data/zstp10_gxcz1d2_without_lableAndDescribe.csv','a+',encoding='utf-8') as f:
            with open('./data/zstp10_gxcz1d2_without_lable.csv','r',encoding='utf-8') as r:
                for line in r:
                    row=line.split(',')
                    if row[1]!='describe':
                        f.write(line)
                    else:
                        ff.write(line)
    print("B_done!")

def C():
    guanxi=[]
    with open('./data/createrelation2020.csv', 'r', encoding='utf-8') as r:
        for line in r:
            row = line.split(',')
            if row[1] not in guanxi:
                guanxi.append(row[1])
    print("C1.done!")
    with open('./data/zstp10_gxcz1d2_node_re_node_DONT_KNOW.csv', 'a+', encoding='utf-8') as ff:
        with open('data/zstp10_gxcz1d2_NODE_REL_NODE_YSE.csv', 'a+', encoding='utf-8') as f:
            with open('./data/zstp10_gxcz1d2_without_lableAndDescribe.csv','r',encoding='utf-8') as r:
                for line in r:
                    row=line.split(',')
                    if row[1] in guanxi:
                        f.write(line)
                    else:
                        ff.write(line)
    print("C2_done!")

def D():
    nodes = set()
    oldstring=''
    with open('./data/finall2020.csv', 'r', encoding='utf-8') as r:
        for line in r:
            row = line.split(',')
            if row[0]!=oldstring:
                oldstring=row[0]
                nodes.add(oldstring)
        r.close()
    print('D1_DONE!')
    with open('./data/zstp10_gxcz1d2_NODE_REL_NODE_YSE2.csv', 'a+', encoding='utf-8') as ff:
        with open('data/zstp10_gxcz1d2_node_re_node_DONT_KNOW2.csv', 'a+', encoding='utf-8') as f:
            with open('./data/zstp10_gxcz1d2_node_re_node_DONT_KNOW.csv', 'r', encoding='utf-8') as r:
                for line in r:
                    row = line.strip('\n').split(',')
                    if row[2] in nodes:
                        ff.write(line)
                    else:
                        f.write(line)

'''5.在“zstp10_gxcz1d2_node_re_node_DONT_KNOW2.csv”中分离出“zstp10_gxcz1d2_NODE_REL_NODE_YSE2.csv”中的节点连接，称为
“zstp10_gxcz1d2_NODE_REL_NODE_YSE3.csv”，其他的写入“zstp10_gxcz1d2_NODE_REL_NODE_NO.csv”'''
def F():
    relations=set()
    with open('./data/zstp10_gxcz1d2_NODE_REL_NODE_YSE2.csv', 'r', encoding='utf-8') as r:
        for line in r:
            row = line.split(',')
            relations.add(row[1])
    with open('./data/zstp10_gxcz1d2_NODE_REL_NODE_YSE3.csv', 'a+', encoding='utf-8') as ff:
        with open('data/zstp10_gxcz1d2_NODE_REL_NODE_NO.csv', 'a+', encoding='utf-8') as f:
            with open('./data/zstp10_gxcz1d2_node_re_node_DONT_KNOW2.csv', 'r', encoding='utf-8') as r:
                for line in r:
                    row = line.split(',')
                    if row[1] in relations:
                        ff.write(line)
                    else:
                        f.write(line)



'''6.将“zstp10_gxcz1d2_NODE_REL_NODE_YSE.csv”“zstp10_gxcz1d2_NODE_REL_NODE_YSE2.csv”“zstp10_gxcz1d2_NODE_REL_NODE_YSE3.csv”三个文件
合并到“zstp10_gxcz1d2_NODERELNODE.csv”'''
def E():
    with open('./data/zstp10_gxcz1d2_NODERELNODE.csv', 'a+', encoding='utf-8') as t:
        with open('./data/zstp10_gxcz1d2_NODE_REL_NODE_YSE.csv', 'r', encoding='utf-8') as r:
            for line in r:
                t.write(line)
            r.close()
            print("E1!")
        with open('./data/zstp10_gxcz1d2_NODE_REL_NODE_YSE2.csv', 'r', encoding='utf-8') as r:
            for line in r:
                t.write(line)
            r.close()
            print("E2!")
        with open('./data/zstp10_gxcz1d2_NODE_REL_NODE_YSE3.csv', 'r', encoding='utf-8') as r:
            for line in r:
                t.write(line)
            r.close()
            print("E3!")

# A()
# B()
# C()
# D()
# F()
E()