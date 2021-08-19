import sys
sys.setrecursionlimit(int(1e9))  ## ---------------------> 파이썬에서 재귀함수를 사용하는 상항에서 런타임 에러가 발생하면, 재귀깊이의 제한때문일 수 있으므로 추가해주기!!

class tree:

    ## tree가 갖는 변수는 *3개*다
    ## --> 1. mid : 현재 노드의 x, y 좌표
    ## --> 2. left : 현재 노드의 왼쪽 노드들을 nodeinfo로 하는 트리
    ## --> 3 . right : 현재 노드의 오른쪽 노드들을 nodeinfo로 하는 트리
    
    def __init__(self, nodeinfo):
        ## y값이 가장 큰 노드의 x,y값을 저장
        self.mid = max(nodeinfo, key = lambda x : x[1])

        ## 그 노드를 기준으로 왼쪽, 오른쪽 노드의 리스트를 구하기
        leftList  = [node for node in nodeinfo if node[0] < self.mid[0]]
        rightList = [node for node in nodeinfo if node[0] > self.mid[0]]


        if len(leftList) != 0:
            self.left = tree(leftList)   ## --> self.__init__(leftList) 하면 안되는 이유는, self.__init__의 리턴갑이 없기 때문이다. 전체적인 재귀 구조를 만들기 위해서는 
                                         ##     클래스를 재귀적으로 사용해야 한다.
        else:
            self.left = None


        if len(rightList) != 0:
            self.right = tree(rightList)

        else:
            self.right = None


    ## 전위순회 구현
    def preorder(self):
        global preList

        preList.append(self.mid)

        if self.left != None:
            self.left.preorder()


        if self.right != None:
            self.right.preorder()


    ## 후위순회 구현
    def postorder(self):
        global postList

        if self.left != None:
            self.left.postorder()


        if self.right != None:
            self.right.postorder()


        postList.append(self.mid)


            
def solution(nodeinfo):
    global preList
    global postList

    preList = []
    postList = []

    root = tree(nodeinfo)

    root.preorder()
    root.postorder()

    preList = list(map(lambda x : nodeinfo.index(x) + 1, preList))
    postList = list(map(lambda x : nodeinfo.index(x) + 1, postList))

    answer = []
    answer.append(preList)
    answer.append(postList)

    return answer
