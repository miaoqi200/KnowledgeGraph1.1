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





connection = "http://localhost:7474-neo4j-123456"
t = Neo4jGraph(connection)
t.con()
lastnode=''
lastcql=''



def chulitxt(string):
    s=string
    for i in list(r'''[]\;',./<>?:"{}|，。/；‘【】、《》？：“{}|！@#￥%……&*（）——+!@#$%^&*()+~` '''):
        s=s.replace(i,'')
    return s
with open('data/finall.csv', 'a+', encoding='utf-8') as f1:
    # with open('data/finallcql.csv', 'a+', encoding='utf-8') as f2:
        with open('data/new_ABC.csv','r',encoding='utf-8') as f:
            count_i=0
            for row in f:

                count_i+=1
                line = row.rstrip('\n').split(',')
                b1=chulitxt(line[0])
                b2=chulitxt(line[1])

                f1.write(b1+','+b2+','+line[2]+'\n')
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



