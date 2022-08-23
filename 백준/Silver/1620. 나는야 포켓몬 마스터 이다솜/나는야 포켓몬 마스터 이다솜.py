import sys
N, M = map(int, sys.stdin.readline().split())
pokemon_arr = [""]
pokemon_dict = {}
for i in range(1, N+1):
    pokemon = sys.stdin.readline().strip()
    pokemon_arr.append(pokemon)
    pokemon_dict[pokemon] = i

for _ in range(M):
    line = sys.stdin.readline().strip()
    if line[0].isalpha():
        print(pokemon_dict[line])
    else:
        print(pokemon_arr[int(line)])
