N = 7
corse = [[1,0],[3,6],[4,2],[3,6],[6,0],[7,1],[1,4],[0,4],[2,3]]

from collections import defaultdict
class Solution:
    def check(self, N, corse):
        graph = defaultdict(set)
        for i,j in corse:
            graph[i].add((i,j))
        # print(graph)
        def recurent_check(startpoint: int, exe_list: list):

            for fr,to in graph[startpoint]:
                if (fr,to) in exe_list: # return True로 끝내면 되지만 뭐가 순환되는 지 확인
                    print('\n\n')
                    print(exe_list)
                    print(startpoint, (fr,to))
                    return True
                exe_list.append((fr,to))
                if recurent_check(to, exe_list): return True # 재귀구조 안쓰고 해보려고 했는데, 실패했다...
                exe_list.pop()
            return False
        task_list = list(graph.keys())
        print(graph)
        print(task_list)
        exe_list = []
        for startpoint in task_list:
            if recurent_check(startpoint, exe_list): return '순환구조!'
        return '비순환 구조ㅎㅎ'


sol = Solution()

print(sol.check(N,corse))
        
