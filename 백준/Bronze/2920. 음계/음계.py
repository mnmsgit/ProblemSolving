import sys
s = sys.stdin.readline().strip()
s = s.replace(" ", "")
if s == "12345678":
    print("ascending")
elif s == "87654321":
    print("descending")
else:
    print("mixed")
