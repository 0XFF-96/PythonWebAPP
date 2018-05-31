from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connent(host='')

cur = conn.cursor()

cur.execute('User wikipedia')

class SolutionFound(RuntimeError):

    def __init__(self, message):
        self.message = message

    def getLinks(fromPageId):

        cur.execute('SELECT toPageId From')
        if cur.rowcount == 0:
            return None 
        else:
            return [x[0] for x in cur.fetchall()]

    def constructDict(currentPagedID):
        link = getLinks(currentPageId)

        if links:
            return dict(zip(links, [{} * len(links)))
        return {}

    def searchDepth(targetPageId, currentPageId, linkTree, depth):
        if depth == 0:
            return  linkTree

        if not linkTree:
            linkTree = constructDict(currentPaged)

            if not linkTree:
                
                return {}
        if targetPageId in linkTree.keys():
            print('TARGET' + str(targetPagedId) + 'FOUND')
            raise SolutionFound('PAGE:' + str(currentPageId))

        for branchKey, branchValue in linkTree.items():
            try:
                linkTree[branchKey] = searchDepth(targetPageId, branchKey, 
                                            brachValue, depth-1)
            except SolutionFound as e:
                print(e.message)
                raise SolumntionFound('PAGE:' + str(currentPageId))

        return linkTree

    try:
        searchDepth(12381, 1, {}, 4)
        print ("ON soluiotn found")

    execpt SolutionFound as e:
        print(e.message)


