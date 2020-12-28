import zhconv
import sys
import os
with open('data/zstp13_hfzw3d1_NODERELNODE_CHEN_withoutPunc33.csv', 'a+', encoding='utf-8') as ff:
    with open('data/zstp13_hfzw3d1_NODERELNODE_CHEN_HavePunc1.csv', 'r', encoding='utf-8') as f:
        for i in f:
            line = i.split(',')
            s=line[2]
            for pun in [';', ':', '：', ',', '"', "'", '#', '!', "！", '.', '。', '？', '?', '[',
                        ']', '{', '}', '【', '【', '】', '`',  '@','&', '，', '“', '”'
                , '《', '》', '·', '_', '=', '——', '；', '，','（','）',' ']:
                s=s.replace(pun,'')
            ff.write(line[0]+','+line[1]+','+s+','+line[3])
