nums = [1,2,3]

def subsets(nums):
    result = []

    def dfs(index, path):
        # 매번 결과 추가
        result.append(path) # 빈 []도 결과에 추가

        # 경로를 만들면서 dfs
        for i in range(index, len(nums)): # 0 ~ 3까지
            dfs(i+1, path + [nums[i]])

    dfs(0, [])

    return result

subsets(nums)