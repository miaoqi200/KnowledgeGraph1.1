'''
版本：莫要纠结版
函数描述：将收到的一行数据清洗
Parameter：datalist：一行数据
Returns:data_list：清洗后的数据
'''
def data_go(datalist):
    data_list = datalist
    while '' in data_list:
        data_list.pop(data_list.index(''))
    # 超过三个的情况
    # if len(data_list) > 3:
    #     tmp = []
    #     tmpstrin = ''
    #     for i in range(2, len(data_list)):
    #         tmpstrin += data_list[i]
    #     tmp.append(data_list[0])
    #     tmp.append(data_list[1])
    #     tmp.append(tmpstrin)
    #     data_list = tmp
    if len(data_list) != 3:
        return ['']
    else:
        if data_list[0][-1] in list('0123456789') and data_list[1][0] in list('0123456789'):
            return ['']


        elif data_list[1][-1] in list('0123456789') and data_list[2][0] in list('0123456789'):
            return ['']

    return data_list

'''
代码描述：把数据按照其段落数存储
'''
node1=''
node2=''
import time
Begin_time = time.time()
with open('./data/len_3.csv','a+',encoding='utf-8') as ff:
    with open('./data/ownthink_v2.csv','r',encoding='utf-8') as f:
        # i=-1

        for line in f:
            # i+=1
            # if i%10000==0:

                # time_s=(End_time-Begin_time)/((i+1)/140919784)-(End_time-Begin_time)
                # time_m=int(time_s/60)
                # time_h=int(time_m/60)
                # print(i/140919784*100,'%','用时：',int(int((End_time-Begin_time)/60)/60),'h',int((End_time-Begin_time)/60)%60,'m','剩余：',time_h,"h",time_m-time_h*60,"m")
            data_list=(line.rstrip("\n").replace('"', '').split(','))
            data_list=data_go(data_list)
            if data_list==['']:
                continue

            # print(str(data_list)[1:-1]+"\n")
            ff.write(str(data_list)[1:-1]+"\n")
End_time = time.time()
time_s=(End_time-Begin_time)
time_m=int(time_s/60)
time_h=int(time_m/60)
print(time_h,'h',time_m%60,'m',int(time_s%60),'s')