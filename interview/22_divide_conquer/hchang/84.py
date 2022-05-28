import re
input_ = "2*3-4*5"
# 2 * 3 - 4
# 6 - 4 * 5
# 2 * (-1) * 5

def solu(x):
    oper = set('*+-')
    operdic = {'*':lambda x, y: x*y,'+':lambda x,y:x+y,'-':lambda x,y:x-y}
    operdval = set(operdic.values())
    num = ''
    exp = []
    for i in x:
        if i in oper:
            exp.extend((eval(num),operdic[i]))
            num = ''
        else:
            num += i
    exp.append(eval(num))
    print(exp)
    def so(x):
        if len(x)==1: return x
        if len(x)==3: return [x[1](x[0],x[2])]
        answer = []
        for index, i in enumerate(x):
            if i in operdval:
                left = so(x[:index])
                right = so(x[index+1:])
                answer.extend([i(lt,rt) for lt in left for rt in right])
        return answer
        
    return so(exp)


    # if len(set(x) & set(oper))==0:
    #     return [eval(x)]

    # answer = []
    # for index, i in enumerate(x):
    #     if i in oper:
    #         left = solu(x[:index])
    #         right = solu(x[index+1:])
    #         answer.extend([eval(str(lt)+i+str(rt)) for lt in left for rt in right])
    # return answer
        # if expression.isdigit():
        #     return [eval(expression)]
        # answer = []
        # for index, i in enumerate(expression):
        #     if i in self.oper:
        #         left = self.diffWaysToCompute(expression[:index])
        #         right = self.diffWaysToCompute(expression[index+1:])
        #         answer.extend([eval(str(lt) + i + str(rt)) for lt in left for rt in right])
        # return answer

print(solu(input_))

                

    
    
        
        