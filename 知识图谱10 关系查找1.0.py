def write(string):
    with open('./data/createrelation2020.csv', 'a+', encoding='utf-8') as f:
        f.write(string)
        print(string)
        f.close()

allnodes=[]

with open('./data/finall2020.csv','r',encoding='utf-8') as r:
    lastword=''
    for line in r:
        line=line.split(',')
        if line[0] !=lastword:
            lastword=line[0]
            allnodes.append(line[0])
        # break
print(len(allnodes))
with open('./data/finall2020.csv','r',encoding='utf-8') as r:
    for line in r:
        sttt=line.rstrip('\n').split(',')
        if sttt[2] in allnodes:
            write(line)

