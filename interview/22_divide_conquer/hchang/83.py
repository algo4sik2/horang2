input_ = [3,2,3]
output = 3

def solu(x):
    return sorted(x)[len(x)//2]

print(solu(input_)==output)