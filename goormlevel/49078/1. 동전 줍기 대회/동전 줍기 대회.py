N = int(input())  
C_i = list(map(int, input().split()))  

current_sum = 0  
max_sum = float('-inf')  

for num in C_i:
    current_sum = max(num, current_sum + num)  
    max_sum = max(max_sum, current_sum)  

print(max(0, max_sum)) 