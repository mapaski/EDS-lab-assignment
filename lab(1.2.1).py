# Input number of courses
n = int(input())

# Input marks
marks = list(map(int, input().split()))

# Check if any mark is less than 40
fail = False
for m in marks:
	if m < 40:
		fail = True
		break

if fail:
	print("Fail")
else:
	aggregate = sum(marks) / n
	print(f"Aggregate Percentage: {aggregate:.2f}")
	if aggregate > 75:
		grade = "Distinction"
	elif aggregate >= 60:
		grade = "First Division"
	elif aggregate >= 50:
		grade = "Second Division"
	else:
		grade = "Third Division"
	print(f"Grade: {grade}")
