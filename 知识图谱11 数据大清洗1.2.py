with open('./data/zstp11_sjdqx_NODE_REL_NODE_NO.csv', 'a+', encoding='utf-8') as ff:
    with open('./data/zstp10_gxcz1d2_NODE_REL_NODE_NO.csv', 'r', encoding='utf-8') as f:
        for line in f:

            stt=line.strip('\n').replace(' ','').replace('"','').replace("'",'').split(',')
            if stt[0]!='' and stt[1]!='' and stt[2]!='':
                ff.write(stt[0]+","+stt[1]+","+stt[2])