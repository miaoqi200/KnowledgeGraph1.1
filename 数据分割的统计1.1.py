import time

Begin_time = time.time()

count_dic = {}
i=-1
with open('./data/len_3.csv','r',encoding='utf-8') as f:
    for line in f:
        i+=1
        spline = line.split(",")
        p = spline[1]
        count = count_dic.get(p,0)
        count_dic[p] = count + 1
with open('data/datapart/relations_3.csv', 'a+', encoding='utf-8') as file:
    stt=''
    for a,b in count_dic.items():
        stt=a
        break
    count_dic[stt] = i
    for a,b in count_dic.items():
        file.write(a[1:-1]+','+str(b)+'\n')


End_time = time.time()
time_s=(End_time-Begin_time)
time_m=int(time_s/60)
time_h=int(time_m/60)
print(time_h,'h',time_m%60,'m',int(time_s%60),'s')