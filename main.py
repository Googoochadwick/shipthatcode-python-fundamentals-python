score = int(input())
# Print the letter grade for this score

if score > 90:
    print('A')

if score < 90 and score >= 80:
    print('B')

if score < 80 and score >= 70:
    print('C')

if score < 70 and score >= 60:
    print('D')

if score < 60:
    print('F')