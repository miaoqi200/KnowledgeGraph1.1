datas={}
with open('data/relation_all.csv','r',encoding='utf-8') as fa:
    for row1 in fa:
        a=row1.rstrip("\n").split(',')
        ss = a[1]
        for i in ['<','>',';',':','：',',','"' ,"'", '#', '!', "！", '.', '。', '？', '?', '[', ']', '{', '}', '【', '】', '`',  '@', '%','，']:
            ss = ss.replace(i, '')
        datas[ss]=a[0]
    fa.close()
print('done')
with open('data/zstp14_NO_other3.csv','r',encoding='utf-8') as fa:
    with open('data/zstp14_ownthink_ON.csv', 'a+', encoding='utf-8') as f:
        with open('data/zstp14_NO_other4.csv', 'a+', encoding='utf-8') as ff:
            for row in fa:
                try:
                    line=row.split(',')
                    ss = datas[line[1]]

                    for pun in [';', ':', '：', ',', '"', "'", '#', '!', "！", '.', '。', '？', '?', '[',
                                ']', '{', '}', '【', '【', '】', '`', '@', '&', '，', '“', '”'
                        , '《', '》', '·', '_', '=', '——', '；', '，', '（', '）', ' ']:
                        ss = ss.replace(pun, '')


                    f.write(line[0]+','+line[1]+','+ss+','+line[2])
                except:
                    ff.write(row)

# print('done')
# with open('data/zstp13_hfzw2d1_NODERELNODE_CH_EN.csv', 'a+', encoding='utf-8') as f:
#     with open('data/zstp13_hfzw_NODERELNODE_CH_EN_out.csv', 'r', encoding='utf-8') as ff:
#         for i in ff:
#             f.write(i)
