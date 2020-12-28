# datas={}
# with open('data/relation_all.csv','r',encoding='utf-8') as fa:
#     for row1 in fa:
#         a=row1.rstrip("\n").split(',')
#         ss = a[1]
#         for i in ['<','>',';','\\',':','：','/',',','"' ,"'", '#', '!', "！", '.', '。', '？', '?', '[', ']', '{', '}', '【', '】', '`', '~', '@', '%', '&','(',')','，']:
#             ss = ss.replace(i, '')
#         datas[ss]=a[0]
#     fa.close()
# print('done')
# with open('data/zstp11_sjdqx_NODERELNODE_YES.csv','r',encoding='utf-8') as fa:
#     with open('data/zstp13_hfzw_NODERELNODE_CH_EN.csv', 'a+', encoding='utf-8') as f:
#         # with open('data/zstp13_hfzw_NODERELNODE_CH_EN_out2.csv', 'a+', encoding='utf-8') as ff:
#             for row in fa:
#                 try:
#                     line=row.split(',')
#
#                     ss = datas[line[1]]
#                     for i in ['u3000','\\','<', '>', ';', ':', '：', '/', ',', '"', "'", '#', '!', "！", '.', '。', '？', '?', '[',
#                               ']', '{', '}', '【', '】', '`', '~', '@', '%', '&', '(', ')', '，']:
#                         ss = ss.replace(i, '')
#                     f.write(line[0]+','+line[1]+','+ss+','+line[2])
#                     # ttt=datas[line[1]]
#                 except:
#                     pass
#
# print('done')
# with open('data/zstp13_hfzw_NODERELNODE_CH_EN.csv', 'a+', encoding='utf-8') as f:
#     with open('data/zstp13_hfzw_NODERELNODE_CH_EN_out.csv', 'r', encoding='utf-8') as ff:
#         for i in ff:
#             f.write(i)
with open('data/zstp13_hfzw_NODERELNODE_CH_EN.csv', 'r', encoding='utf-8') as f:
    with open('data/zstp13_hfzw_NODERELNODE_CH_EN_END.csv', 'a+', encoding='utf-8') as ff:
        for i in f:
            line=i.split(',')
            ff.write(line[0]+','+line[1]+','+line[2].replace(' ','')+','+line[3])