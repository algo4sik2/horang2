import re
input_ = "2*3-4*5"

def solu(x):
    oper = set('*/+-')
    if len(set(x) & set(oper))==0:
        return [eval(x)]
    answer = []
    for index, i in enumerate(x):
        if i in oper:
            left = solu(x[:index])
            right = solu(x[index+1:])
            answer.extend([eval(str(lt)+i+str(rt)) for lt in left for rt in right])
    return answer

print(solu(input_))

                

    
    
        
        