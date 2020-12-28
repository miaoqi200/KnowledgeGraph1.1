class Neo4jGraph():
    def __init__(self, login):
        self.graph = None
        self._ip = login.split('-')[0]
        self._username = login.split('-')[1]
        self._password = login.split('-')[2]
        self.CQL = ''

    def con(self):
        from py2neo import Graph, Node, Relationship, NodeMatcher
        self.graph = Graph(self._ip, username=self._username, password=self._password)
        return self.graph

    def cql(self, string):
        return self.graph.run(string).data()

    def cqlclean(self):
        self.CQL = ''
        return self

    def go(self):
        tmp = self.CQL
        self.CQL = ''
        return self.graph.run(tmp).data()

    def GraphClean(self):
        self.graph.delete_all()

    def showcql(self):
        print(self.CQL)





connection = "http://localhost:7474-neo4-123456"
t = Neo4jGraph(connection)
t.con()
lastnode=''
lastcql=''
#
# def wr1(string):
#     with open('data/finall.csv', 'a+', encoding='utf-8') as f1:
#         f1.write(string)
#         f1.close()

# def wr2(string):
#     with open('data/finallcql.csv', 'a+', encoding='utf-8') as f2:
#         f2.write(string)
#         f2.close()
#
# def chulitxt(string):
#     s=string
#     for i in list(r'''[]\;',./<>?:"{}|，。/；‘【】、《》？：“{}|！@#￥%……&*（）——+!@#$%^&*()+~` '''):
#         s=s.replace(i,'')
#     return s
with open('data/testcql.csv', 'a+', encoding='utf-8') as f2:
    with open('data/ttttt.csv','r',encoding='utf-8') as f:
        count_i=0
        for row in f:

            count_i+=1
            line = row.rstrip('\n').split(',')
            # b1=chulitxt(line[0])
            # b2=chulitxt(line[1])

            # wr1(b1+','+b2+','+line[2]+'\n')
            # 如果出现新节点，则把cql写入，并且清空
            if lastnode != line[0]:
                lastcql+='});'
                if lastcql!='});' and count_i!=2:
                    f2.write(lastcql+'\n')
                lastcql='create (n:Node{NodeId:'+"'"+line[0]+"'"

                lastnode=line[0]
            # 如果是就节点，继续加入cql
            # (a:Node{NodeId:line.node})
            else:
                lastcql=lastcql+','+line[1]+":"+"'"+line[2]+"'"


        lastcql+='});'
        f2.write(lastcql+'\n')
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



