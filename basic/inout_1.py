## 문자열 쪼개기
s=input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

## 문자열 쪼개기_1
s=input()
print(s[0:2], s[2:4], s[4:6])

## 시:분:초 입력시 분 만출력
h,m,s=input().split(':')
print(m,sep=':')

## 문자열 합치기
s1,s2 = input().split()
s= s1+s2
print(s)

## 정수의 합 
i1,i2 = input().split()
c=int(i1)+int(i2)
print(c)

## 실수의 합 
f1= input()
f2= input()
c=float(f1)+float(f2)
print(c)

## 16진수(hexadecimal) 변환(소문자)
s=input()
h=int(s)
print('%x'%h)

## 16진수(hexadecimal) 변환(대문자)
s=input()
h=int(s)
print('%X'%h)

## 16진수 -> 8진수(octal)
a=input()
n=int(a, 16)
print('%o'%n)

## unicode -> 10진수
n=ord(input())
print(n)

## 정수 -> unicode
c=int(input())
print(chr(c))