mid = float(input("Midterm Note:"))
final = float(input("Final or Make-Up Note:"))

mid = (mid * 40) / 100
final = (final * 60) / 100

gradePoint = (mid + final)

print("Grade Point:", gradePoint)

if (gradePoint >= 0 and gradePoint <= 49):
    print("Note: FF")

elif (gradePoint >= 50 and gradePoint <= 59):
    print("Note: DD")

elif (gradePoint >= 60 and gradePoint <= 69):
    print("Note: DC")

elif (gradePoint >= 70 and gradePoint <= 74):
    print("Note: CC")

elif (gradePoint >= 75 and gradePoint <= 79):
    print("Note: CB")

elif (gradePoint >= 80 and gradePoint <= 84):
    print("Note: BB")

elif (gradePoint >= 85 and gradePoint <= 89):
    print("Not: BA")

elif (gradePoint >= 90 and gradePoint <= 100):
    print("Note: AA")

else:
    print("Invalid Input!")