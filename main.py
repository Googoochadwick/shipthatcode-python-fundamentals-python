year = int(input())

# A year is leap if divisible by 4 AND (not divisible by 100 OR divisible by 400)
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("leap")
else:
    print("not leap")
