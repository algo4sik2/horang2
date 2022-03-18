input_list = ['hello','Hannah']
input_list = list(map(list, input_list))


def reversestring(lst:list) -> None:
    left, right = 0, len(lst)-1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

print(input_list)

for i in input_list:
    reversestring(i)
print('함수 통과 후')

print(input_list)