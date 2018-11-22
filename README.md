# Python programing basic & easy exercise



<b>Python programing basic & easy problems</b>는 표준 입출력을 이용한 간단한 파이썬 코딩 문제 풀이입니다.


2017년 겨울학기 파이썬 프로그래밍을 수강할 때 Python3로 작성했던 코드입니다.

각 문제별 .py파일의 상단에 풀이한 문제에 대한 설명을 요약하여 주석처리하였습니다.



**Readme Contents**

- [Example](#Example) - 코드 예시 (exercise9/problem5.py)
- [Basics](#Basics) 
  - [표준 입출력하기](#표준-입출력하기) 
  - [풀이 관련 내장 함수](#풀이-관련-내장-함수) 

- [Exercise별 구성 및 설명](#Exercise별-구성-및-설명) - exercise 별 problem 수, 파트 및 설명 



### Example
exercise9/problem5.py

```py
# 4번 문제를 상속받아서 두점을 입력 받고 두 점의 거리를 출력하기
# class 활용


import math

x1 =  int(input())
y1=  int(input())
z1 =   int(input())
x2=  int(input())
y2=  int(input())
z2=  int(input())

class plus:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        self.x  =self.x + other.x
        self.y = self.y + other.y


class plus3(plus):
    def __init__(self, x,y,z):
        super(plus3,self).__init__(x,y)
        self.z = z
    def __add__(self, other):
        super(plus3,self).__add__(other)
        self.z = self.z + other.z

class maxx(plus3):
    def bigger(self, other):
        self.x = max(self.x,other.x)
        
        self.y = max(self.y,other.y)
        
        self.z = max(self.z,other.z)

class eq(plus3):
    def eqq(self,other):
        if (self.x == other.x) and (self.y == other.y) and (self.z == other.z):
            print("eq")
        else:
            print("not eq")

class dist(eq):
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 +(self.y - other.y)**2 +(self.z - other.z)**2)

first = dist(x1,y1,z1)
second =dist(x2 y2,z2)
```
가장 상단에 문제에 관한 간략한 설명이 요약되어있습니다.

이후 해당 문제에 대한 작성코드를 확인할 수 있습니다.

---

### Basics
#### 표준 입출력하기

```py
# python3 표준 입력
input_ = input("표준 입력:") #python2에서는 raw_input() 사용

output_ = input_+1

# python3 표준 출력
print(output)
```

#### 풀이 관련 내장 함수

```py
temp = [1,2,3,1]

temp.append(4) 
#temp = [1,2,3,1,4]

temp.sort(temp) 
#temp = [1,1,2,3]

temp.reverse(temp) 
#temp = [1,3,2,1]

temp.index(3) 
#1

temp.remove(3) 
#temp = [1,2,1]

temp.pop(2) 
#temp = [1,3,1], return 2

len(temp) 
# retrun 4

temp.count(1) 
#retrun 2

temp.extend([3,4]) 
#temp = [1,2,3,1,3,4]


all(temp)
# 모두 True 인가?

any(temp) 
# True가 적어도 하나 있나?

chr(1)
# int 1을 char 1로

str(1)
#string으로 변환

divmod(5,2)
#modulus연산

max(temp)
#return 3

min(temp)
#return 1

pow(2,4)
#2의 4제곱

sorted(temp) 
#sort와 달리 list를 return

```
---
#### Exercise별 구성 및 설명
| exercise | 문제 수 | 파트 | 설명 |
| ---- | ---- | -------- | ----------- |
| 1 | 3 | Standard I/O| 자동 채점 방식의 문제 풀이를 위한 표준 입출렵 입니다. |
| 2 | 3| Operator | 기본 연산자들의 활용을 다룹니다. |
| 3 | 3 | List, Tuple, Dictionary | 리스트의 활용과 인덱싱을 다룹니다. |
|4|4|Internal modules|내장 함수들을 활용합니다.|
|5|3|For/While loop|반복문을 활용한 예제들의 코드를 작성하였습니다.|
|6|2|Function|함수의 활용을 다룹니다.|
|7|3|Midterm|class 및 file control을 제외한 종합적인 코드의 활용.|
|8|3|File control|파일의 입출력과 저장을 이용한 활용을 다룹니다.|
|9|5|Class|클래스의 활용 및 연산자 오버로딩, 오버라이딩을 다룹니다.|