"""
비교연산
"""

## 비트단위 시프트 연산자 <<, >>
n=int(input())
print(n<<1)  #10을 2배 한 값인 20(10X2의1승)
print(n>>1)  #10을 반으로 나눈 값인 5 
print(n<<2)  #10을 4배 한 값인 40 (10x2의2승)
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 

a,b = input().split()
a=int(a)
b=int(b)
print(a<<b) # a=2, b=3 : 2x2의 3승 16 

## 비교 연산자  <, >, <=, >=, ==, !=  return True or False
a,b = input().split()
a=int(a)
b=int(b)
print(a<b)
print(a==b)
print(b>=a)
print(a!=b)
    