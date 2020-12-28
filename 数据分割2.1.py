
'''
代码描述：把三元组分割
'''
node1=''
node2=''
relation = []
relation_count = []
import time

Begin_time = time.time()

with open('./data/from_3.csv','a+',encoding='utf-8') as f1:
    with open('./data/to_3.csv', 'a+', encoding='utf-8') as f2:

        with open('./data/len_3.csv','r',encoding='utf-8') as f:
            i=-1

            for line in f:
                i+=1
                data_list=(line.rstrip("\n").split(','))


                if data_list[1] not in relation:
                    relation.append(data_list[1])
                    relation_count.append(1)
                else:
                    relation_count[relation.index(data_list[1])]=relation_count[relation.index(data_list[1])]+1


                f1.write(data_list[0]+'\n')

                f2.write(data_list[2]+'\n')

            relation_count[0]=i
            with open('data/datapart/relations_3.csv', 'a+', encoding='utf-8') as file:
                for string_id in range(len(relation)):
                    file.write(relation[string_id]+','+str(relation_count[string_id])+'\n')


End_time = time.time()
time_s=(End_time-Begin_time)
time_m=int(time_s/60)
time_h=int(time_m/60)
print(time_h,'h',time_m%60,'m',int(time_s%60),'s')