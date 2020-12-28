with open('data/finall2020.csv', 'a+', encoding='utf-8') as f1:
    # with open('data/finallcql.csv', 'a+', encoding='utf-8') as f2:
    with open('data/finall.csv', 'r', encoding='utf-8') as f:
        # count_i = 0
        for row in f:
            # count_i += 1
            line = row.rstrip('\n').split(',')


            f1.write(line[0] + ',' + line[1] + ',' + line[2].replace(' ','') + '\n')
            # 如果出现新节点，则把cql写入，并且清空
            # if lastnode != line[0]:
            # lastcql+='});'
            # if lastcql!='});' and count_i!=2:
            # f2.write(lastcql+'\n')
            # lastcql='create (n:Node{NodeId:'+"'"+b1+"'"

            # lastnode=line[0]
            # 如果是就节点，继续加入cql
            # (a:Node{NodeId:line.node})
            # else:
            # lastcql=lastcql+','+b2+":"+"'"+line[2]+"'"

        # lastcql+='});'
        # f2.write(lastcql+'\n')
        f.close()
    # t.cql(''' USING PERIODIC COMMIT 100
    #         LOAD CSV WITH HEADERS
    #         FROM "file:///Tools/main.csv"
    #         AS line
    #         create
    #         (a:Node{NodeId:line.node})
    #
    #          '''
    #       )

    # res=t.cql('''
    #         USING PERIODIC COMMIT 100
    #         LOAD CSV WITH HEADERS
    #         FROM "file:///ttttt.csv"
    #         AS line
    #         create (n:test{line.bb:line.cc})
    #          '''
    #       )
    # print(res)



