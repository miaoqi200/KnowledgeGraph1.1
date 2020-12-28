

'''
代码描述：把数据按照其段落数存储
'''
import time
Begin_time = time.time()
with open('./data/len_33.csv','a+',encoding='utf-8') as ff:
    with open('./data/len_3.csv','r',encoding='utf-8') as f:
        for line in f:
            data_list=(line.replace("'", ''))
            ff.write(str(data_list))
End_time = time.time()
time_s=(End_time-Begin_time)
time_m=int(time_s/60)
time_h=int(time_m/60)
print(time_h,'h',time_m%60,'m',int(time_s%60),'s')