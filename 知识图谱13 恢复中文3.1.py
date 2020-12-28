# with open('data/zstp13_hfzw3d1_NODERELNODE_CHEN_NoPunc.csv', 'a+', encoding='utf-8') as f1:
#     with open('data/zstp13_hfzw3d1_NODERELNODE_CHEN_HavePunc.csv', 'a+', encoding='utf-8') as f2:
#         with open('data/zstp13_hfzw2d1_NODERELNODE_CH_EN.csv', 'r', encoding='utf-8') as ff:
#             for i in ff:
#                 line=i.split(',')
#                 for pun in ['<', '>', ';', '\\', ':', '：', '/', ',', '"', "'", '#', '!', "！", '.', '。', '？', '?', '[',
#                           ']', '{', '}','【', '【', '】', '`', '~', '@', '%', '&', '(', ')', '，','+','“','”','+','-','*','《','》',
#                             '·','_','=','——','；','，']:
#                     if pun in line[1] or pun in line[2]:
#                         f2.write(i)
#                         break
#                 f1.write(i)

# with open('data/zstp13_hfzw3d1_NODERELNODE_CHEN_withoutPunc1.csv', 'a+', encoding='utf-8') as f1:
#     with open('data/zstp13_hfzw3d1_NODERELNODE_CHEN_HavePunc1.csv', 'a+', encoding='utf-8') as f2:
#         with open('data/zstp13_hfzw2d1_NODERELNODE_CH_EN.csv', 'r', encoding='utf-8') as ff:
#             for i in ff:
#                 line=i.split(',')
#                 gg=list(line[2])
#                 flag=1
#                 for pun in [' ','<', '>', ';', '\\', ':', '：', '/', ',', '"', "'", '#', '!', "！", '.', '。', '？', '?', '[',']', '{', '}','【', '【', '】', '`', '~', '@', '%', '&', '(', ')', '，','+','“','”','+','-','*','《','》','·','_','=','——','；','，']:
#                     if pun in gg:
#                         f2.write(i)
#                         flag=0
#                         break
#                 if flag:
#                     f1.write(i)