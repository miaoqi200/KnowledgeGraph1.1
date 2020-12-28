with open('data/NODERELNODE.csv', 'r', encoding='utf-8') as f:
    with open('data/zstp11_sjdqx_NODERELNODE_YES.csv','a+', encoding='utf-8') as ff:
        # count=0
        for row in f:
            # count+=1
            line=row.strip('\n').replace('"','').replace("'",'').split(',')
            # string="merge (a:Node{NodeId:'"+line[0]+"'}) merge (b:Node{NodeId:'"+line[2]+"'}) merge (a)-[c:"+line[1]+"]->(b);"
            if line[0]!='' and line[1]!='' and line[2]!='':
                # print((line[0]+','+line[1]+','+line[2]+'\n'))
                ff.write(line[0]+','+line[1]+','+line[2]+'\n')
