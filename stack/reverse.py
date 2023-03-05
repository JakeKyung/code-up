## 입력된 숫자 역순 출력
def reverse(n):
    s = list(map(int,str(n)))
    s.reverse()
    num =''
    for i in s:
        num += str(i)    
    return num

# input 123456
n = int(input())
# output 654321
print(reverse(n))