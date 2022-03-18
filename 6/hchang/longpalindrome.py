input_= 'babad'

checklist = list(input_)

answer = []
for i in range(len(input_)):
    for j in range(i,len(input_)):
        check = checklist[i:j]
        if check == check[::-1] and len(answer) < len(check):
            answer = checklist[i:j]

print(answer)