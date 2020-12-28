with open('./data/from_3.csv','r',encoding='utf-8') as f:
    for row in f:
        line=(row.split(','))
        print(line[0])
