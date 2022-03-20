s = list(input())
input_arr = []
d = 0
for i in s: # 받은 문자열 반복문으로 돌리기
    if i == '<' or d == 1: #태그 시작 
        if input_arr:
            input_arr.reverse()
            print(''.join(a), end='')
            input_arr = []
        if i == '>':
            print(i,end='')
            d = 0
        else:
            print(i,end='')
            d = 1     
    else:                 #단어 시작
        if i == ' ':
            input_arr.reverse()
            print(''.join(input_arr)+' ', end='')
            input_arr = []
        else:
            input_arr.append(i)
if input_arr:
    input_arr.reverse()
    print(''.join(input_arr), end='')

        

    