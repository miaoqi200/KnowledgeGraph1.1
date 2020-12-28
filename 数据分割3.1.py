
'''
代码描述：把三元组分割
'''
node1=''
# i = 0
import time
Begin_time = time.time()

with open('./data/from_3.csv','a+',encoding='utf-8') as f1:

    with open('./data/len_3.csv','r',encoding='utf-8') as f:

        for line in f:
            # i+=1
            data_list=line.split(',')
            aaa=data_list[0][1:-1]
            if aaa!=node1:
                f1.write(aaa+'\n')
                node1=aaa



End_time = time.time()
time_s=(End_time-Begin_time)
time_m=int(time_s/60)
time_h=int(time_m/60)
print(time_h,'h',time_m%60,'m',int(time_s%60),'s')