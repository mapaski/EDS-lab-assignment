import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

# 1. Print all student details
print("All student Details:\n", a)

# 2. Total students
print("Total Students:", a.shape[0])

# 3. Roll numbers
print("All Student Roll Nos", a[:, 0])

# 4. Subject 1 marks
print("Subject 1 Marks", a[:, 1])

# 5. Minimum marks in Subject 2
print("Min marks in Subject 2", np.min(a[:, 2]))

# 6. Maximum marks in Subject 3
print("Max marks in Subject 3", np.max(a[:, 3]))

# 7. All subject marks (excluding roll numbers)
print("All subject marks:", a[:, 1:])

# 8. Total marks of each student
print("Total Marks", np.sum(a[:, 1:], axis=1))

# 9. Average marks of each student
print(np.round(np.mean(a[:, 1:], axis=1), 1))

# 10. Average marks of each subject
print("Average Marks of each subject", np.round(np.mean(a[:, 1:], axis=0), 1))

# 11. Average marks of S1 and S2
print("Average Marks of S1 and S2", np.round(np.mean(a[:, 1:3], axis=0), 1))

# 12. Average marks of S1 and S3
print("Average Marks of S1 and S3", np.round(np.mean(a[:, [1, 3]], axis=0), 1))

# 13. Roll no with max marks in Subject 3
print("Roll no who got maximum marks in Subject 3", a[np.argmax(a[:, 3]), 0])

# 14. Roll no with min marks in Subject 2
print("Roll no who got minimum marks in Subject 2", a[np.argmin(a[:, 2]), 0])

# 15. Roll no who got 24 marks in Subject 2
print("Roll no who got 24 marks in Subject 2", a[a[:, 2] == 24][:, [0]])

# 16. Count of students with S1 < 40
print("Count of students who got marks in Subject 1 < 40", np.sum(a[:, 1] < 40))

# 17. Count of students with S2 > 90
print("Count of students who got marks in Subject 2 > 90:", np.sum(a[:, 2] > 90))

# 18. Count of students in each subject with marks >= 90
print("Count of students in each subject who got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=0))

# 19. Count of subjects per student with marks >= 90
print("Roll no:", a[:, 0])
print("Count of subjects in which student got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=1))

# 20. Print S1 marks in ascending order
print(np.sort(a[:, 1]))

# 21. Print students who scored between 50 and 90 in Subject 1
filtered = a[(a[:, 1] >= 50) & (a[:, 1] <= 90)]
print(filtered)
print(a)

# 22. Print index positions where S1 = 79
print(np.where(a[:, 1] == 79))
