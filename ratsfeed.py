r = int(input("number of rats"))
unit = int(input("the amount of food each rat consumes"))
n = int(input("number of house"))
arr = list(map(int, input().split()))
if arr is None:
    print(-1)
else:
    required = r * unit
    total = 0
    houses= 0
  for i in range(n):
        total += arr[i]
        if total >= required:
            houses= i + 1
            break
 print("HOUSES:",houses)
