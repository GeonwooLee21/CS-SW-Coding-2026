# Floating Point Precision
total = 0.0
for i in range(1000):
    total += 0.001

print(total)
# 정확히 1을 출력하지 못한다 -> 오차가 누적된다! 
# 이는 파이썬 언어의 한계가 아니다. 이진수로 실수 표현을 하는 컴퓨터 시스템의 한계로 발생하는 문제이다.
# python은 decimal이란 기능을 통해 위와 같은 오차를 핸들링한다.


# f-string : formatted string
print('{total}')
print(f'합계는 {total}입니다.')

# enumerate() : 리스트, 튜플, 문자열 등 반복 가능한(iterable) 객체를 입력받아, 각 요소의 인덱스(순번)값을
#               순서쌍(tuple)으로 반환하는 python 내장 함수이다. 주로 for문에 인덱스가 필요할 때 사용하며,
#               수동으로 인덱스를 관리하는 것보다 더 안전하고 가독성 있는 코드를 작성할 수 있다.
# 기본 사용 예시
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits): # enumerate(iterable, start=n)을 통해 인덱스를 n부터 시작할 수 있다.
    print(index, fruit)
# 출력: 1 apple, 2 banan 3 cherry # 출력: 0 apple, 1 banana, 2 cherry

# input으로 입력받은 데이터는 기본적으로 string type으로 저장된다.
a = input("Enter a number : ") # a = int(input("Enter a number : "))
print(type(a))
