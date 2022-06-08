"""
단어 리스트를 reverse 정령하여 같은 값이면 알파벳 순서가 빠른 것이 pop되도록 함
stack의 후입선출을 이용
"""

import sys

N = int(input())
words = []
words_dict = {}
a = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    words.append(word)
words = sorted(words, reverse=True)
max_num = 1

for word in words:
    if word in words_dict:
        num = words_dict[word] + 1
        words_dict[word] = words_dict[word] + 1
        if max_num <= num:
            max_num = num
            a.append(word)
    else:
        words_dict[word] = 1

if a:
    print(a.pop())
else:
    print(words.pop())

