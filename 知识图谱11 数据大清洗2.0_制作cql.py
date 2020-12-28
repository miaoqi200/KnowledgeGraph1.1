# #label
# '''
# merge该节点，把lablezhi都拼接上去
# '''
#
#
# # `如果出现新的节点，
# # 会立即cql封尾，且不是第一次的话会提交cql
# # cql重置，oldone值重置，对节点初始化
# # `如果没有出现新的节点，则再cql增加标签
# # `等到结束，再封尾提交
# def A():
#     oldone = ''
#     with open('./data/zstp11_sjdqx_ALL_LABLE_cql.csv', 'a+', encoding='utf-8') as ff:
#         with open('./data/zstp11_sjdqx_ALL_LABLE.csv', 'r', encoding='utf-8') as g:
#             # for line in g:
#             #     print(line)
#             #     break
#             count = 0
#             cql = ''
#             for row in g:
#                 count += 1
#                 # print(count)
#                 # if count > 100:
#                 #     break
#                 line = row.rstrip('\n').split(',')
#                 if line[0] != oldone:
#                     if count != 1:
#                         cql += ';'
#                         ff.write(cql + '\n')
#                         # print(cql)
#                     oldone = line[0]
#                     cql = "merge (n:Node{NodeId:'" + line[0] + "'}) set n:" + line[2]
#                 else:
#                     cql = cql + ':' + line[2]
#             cql += ';'
#             ff.write(cql + '\n')
#             # print(cql)
#




#
# # describe
# '''直接导入就行了'''
# def B():
#     pass

#
# # 独立节点
# '''之后再讲'''
# def C():
#     pass


# 节点到节点
def D():
    with open('data/zstp11_sjdqx_NODERELNODE_YES_cql.csv', 'w', encoding='utf-8') as ff:
        ff.close()
    with open('data/zstp11_sjdqx_NODERELNODE_YES.csv', 'r', encoding='utf-8') as f:
        with open('data/zstp11_sjdqx_NODERELNODE_YES_cql.csv', 'a+', encoding='utf-8') as ff:
            for row in f:
                line = row.strip('\n').split(',')
                string="merge (a:Node{NodeId:'"+line[0]+"'}) merge (b:Node{NodeId:'"+line[2]+"'}) create (a)-[c:"+line[1]+"]->(b);"
                # print(string)
                # break
                ff.write(string+'\n')
                # if line[0] != '' and line[1] != '' and line[2] != '':
                #     # print((line[0]+','+line[1]+','+line[2]+'\n'))
                #     ff.write(line[0] + ',' + line[1] + ',' + line[2] + '\n')
D()
# A()