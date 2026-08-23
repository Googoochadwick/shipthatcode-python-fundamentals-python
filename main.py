total = 0
# Read numbers and accumulate them until you see 0
while True:
    a = int(input())
    if a != 0:
        total += a
    else:
        print(total)
        break
