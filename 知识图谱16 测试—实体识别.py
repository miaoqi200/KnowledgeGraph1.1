import json
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
function_blue_colorflat=1
def blue(string):
    global function_blue_colorflat
    if function_blue_colorflat==0:
        # function_blue_colorflat=1
        return ('\033[0;35;48m'+string+'\033[0m')
    else:
        # function_blue_colorflat = 0
        return ('\033[0;34;48m' + string + '\033[0m')

connection = "http://localhost:7474-neo4j-123456"
graph = Neo4jGraph(connection)
graph.con()

def getNode(Parameters):
    cql = "match (n:Node{NodeId:'"+Parameters+"'})  return n"
    res=graph.cql(cql)
    return res
def getdescribe(Parameters):
    cql = "match (n:Node{NodeId:'"+Parameters+"'}) where n.describe is not null return n"
    res=graph.cql(cql)
    return res

'''
对段落从前向后分析

用指针p控制



'''


# def getWords(centence):
#     wordlist=[]
#     centence_len=len(centence)
#     for from_id in range(centence_len):
#         for to_id in range(from_id,len(centence)):
#             # word=centence[from_id:to_id+1]
#             word = centence[from_id:centence_len-to_id ]
#
#             node=getNode(word)
#             if len(node)!=0:
#                 wordlist.append(word)
#     return wordlist

def getWords(centence):
    wordlist=[]
    p=-1
    while p<len(centence):
        p+=1
        if p+7<=len(centence):
            for q in range(p+7, p, -1):
                node = getNode(centence[p:q])
                if len(node) != 0:
                    if len(centence[p:q])>=2:
                        wordlist.append(centence[p:q])
                    p = q
                    p -= 1
        else:
            for q in range(len(centence), p, -1):
                node = getNode(centence[p:q])
                if len(node) != 0:
                    if len(centence[p:q]) >= 2:
                        wordlist.append(centence[p:q])
                    p = q
                    p -= 1


    return wordlist




def priblue(centence,wordlist):
    centence1=centence
    centence2=''
    for i in wordlist:
        centence2+=i
    p=0
    q=0
    while p<len(centence1):
        if centence1[p:p+1]==centence2[q:q+1]:
            print(blue(centence1[p:p+1]),end='')
            p+=1
            q+=1
        else:
            print((centence1[p:p+1]),end='')
            p=p+1
    print('')





#
# # print((getNode('2323233')==[]))
centence=input("对段落实体识别：\n")
wordlist=getWords(centence)
print('\n识别实体：')
priblue(centence,wordlist)
print("\n实体列表：")
print(wordlist)


print("\n实体信息：")
for i in wordlist:
    describe=getdescribe(i)
    if len(describe)!=0:
        # js=json.loads(describe[0])
        n=str(describe[0]['n'])
        print(json.loads(f'"{n}"'))



