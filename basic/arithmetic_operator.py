"""
산술연산
"""
## 부호 변경
n=input()
n=int(n)
print(-n)

## 아스키문자표 다음 문자 출력
s=ord(input())
print(chr(s+1))

## 정수 차 계산 
a,b=input().split()
c = int(a)-int(b)
print(c)
'''
산술연산
'''

## 실수 곱 
a,b=input().split()
m = float(a)*float(b)
print(m)

## n 번 출력
w,n=input().split()
print(w*(int(n)))
n = input()
s = input()
print(int(n)*s)

## 거듭 제곱
a,b=input().split()
c = int(a)**int(b)
print(c)

a,b=input().split()
c = float(a)**float(b)
print(c)

## 몫, 나머지
a,b=input().split()
c=int(a)//int(b)
print(c)

a,b=input().split()
c=int(a)%int(b)
print(c)

# 소수점
a=input()
a=float(a)
print(format(a,".2f"))

a,b=input().split()
a=float(a)
b=float(b)
c=a/b
print(format(c,".3f"))

## 합, 차, 곱, 몫, 나머지 ,나눈 값
a,b=input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f"))

## 합, 평균 
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
print(a+b+c, format((a+b+c)/3, ".2f"))