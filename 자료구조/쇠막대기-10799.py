s = list(input())
s_arr =[]
stack_arr = []
count = 0
c = 0
for idx,val in enumerate(s):
    if val == '(' and idx < len(s):
        if s[idx+1] == ')':
            s_arr.append('()')
        else:
            s_arr.append(val)
    else:
        if val == ')' and s[idx-1] == '(':
            continue
        else:
            s_arr.append(val)

for val in s_arr:
    if val == '(':
        stack_arr.append(val)
    elif val == ')':
        c+=1
        stack_arr.pop()
    elif val == '()' and stack_arr:
        count += len(stack_arr)

print(count+c)






    