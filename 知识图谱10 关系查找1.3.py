'''
“zstp10_gxcz1d2_ALL_LABLE.csv”：节点标签
“zstp10_gxcz1d2_ALL_DESCRIBE.csv”：节点描述
“zstp10_gxcz1d2_NODERELNODE.csv”：节点——连接——>节点
“zstp10_gxcz1d2_NODE_REL_NODE_NO.csv”：节点和属性
'''
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

# connection = "http://localhost:7474-neo4j-123456"
# t = Neo4jGraph(connection)
# t.con()


# 1.“zstp10_gxcz1d2_ALL_LABLE.csv”：节点标签:要用cql
# def A():
#   pass
# A()

# 2.“zstp10_gxcz1d2_ALL_DESCRIBE.csv”：节点描述
# def B():
#     connection = "http://localhost:7474-neo4j-123456"
#     t = Neo4jGraph(connection)
#     t.con()
#     t.cql(''' USING PERIODIC COMMIT 100
#                 LOAD CSV
#                 FROM "file:///FORTEST.csv"
#                 AS line
#                 merge (n:test{NodeId:line[0]})
#                 set n.describe=line[2]''')
# B()

# 3.“zstp10_gxcz1d2_NODERELNODE.csv”：节点——连接——>节点
def C():
    pass
    connection = "http://localhost:7474-neo4j-123456"
    t = Neo4jGraph(connection)
    t.con()
    t.cql('''CREATE INDEX ON:Node(NodeId)''')
    t.cql('''
    USING PERIODIC COMMIT 100
                    LOAD CSV WITH HEADERS
                    FROM "file:///zstp10_gxcz1d2_NODERELNODE.csv"
                    AS line
                    merge (a:Node{NodeId:line.实体})
                    merge (b:Node{NodeId:line.值})
                    create (a)-[c:Relationship{RelId:line.attribute}]->(b)
                    ''')

# def D():

# C()







