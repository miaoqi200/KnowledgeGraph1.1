datas={}
with open('data/relation_all.csv','r',encoding='utf-8') as fa:
    for row1 in fa:
        a=row1.rstrip("\n").split(',')
        datas[a[0]]=a[1]
    fa.close()
with open('data/left_ABC.csv','a+',encoding='utf-8') as fff:
    with open('data/new_ABC.csv','a+',encoding='utf-8') as ff:
        with open('data/len_3.csv','r',encoding='utf-8') as f:
            count_n=0
            # c=0
            for row in f:
                count_n+=1
                # if count_n==1:
                #     print('实体,attribute,值')
                line=row.rstrip("\n").split(',')

                # break
                try:
                    ff.write(line[0]+','+datas[line[1]]+','+line[2]+'\n')
                    # c+=1
                    # print(c)
                    # break
                except:
                    try:
                        ff.write(line[0]+','+datas[line[1].replace(' ','')]+','+line[2]+'\n')
                        # c+=1
                        # print(c)
                    except:
                        fff.write(row)
                        print(count_n)
                        # c += 1
                        # print(str(c)+line[1])

