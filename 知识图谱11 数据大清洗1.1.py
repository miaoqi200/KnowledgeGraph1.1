with open('./data/zstp11_sjdqx_ALL_LABLE.csv', 'w', encoding='utf-8') as ff:
    ff.close()
with open('./data/zstp11_sjdqx_ALL_LABLE.csv', 'a+', encoding='utf-8') as ff:
    with open('./data/zstp10_gxcz1d2_ALL_LABLE.csv', 'r', encoding='utf-8') as f:
        count=0
        for line in f:
            count+=1
            stt=line.strip('\n').replace(' ','').replace('"','').replace("'",'').split(',')
            if stt[0]!='' and stt[1]!='' and stt[2]!='':
                if count!=1:
                    ff.write(stt[0]+","+stt[1]+","+stt[2]+'\n')