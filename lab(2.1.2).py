# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}
print("Original Dictionary:", student)

insert_key = int(input())
insert_value = input()
student[insert_key] = insert_value
print("After Insertion:", student)

update_key = int(input())
update_value = input()
if update_key in student:
	student[update_key] = update_value
print("After Update:", student)

delete_key = int(input())
if delete_key in student:
	student.pop(delete_key)
print("After Deletion:", student)

print("Traversing Dictionary:")
for key, value in student.items():
	print(f"{key} : {value}")
