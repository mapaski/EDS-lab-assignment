
int_list = []

while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	choice = input("Enter choice: ")
	
	if choice == '1':
		num_input = input("Integer: ")
		if num_input.isdigit() or (num_input.startswith('-') and num_input[1:].isdigit()):
			num = int(num_input)
			int_list.append(num)
			print("List after adding:", int_list)
		else:
			print("Invalid input")
	
	elif choice == '2':
		if not int_list:
			print("List is empty")
		else:
			num_input = input("Integer: ")
			if num_input.isdigit() or (num_input.startswith('-') and num_input[1:].isdigit()):
				num = int(num_input)
				if num in int_list:
					int_list.remove(num)
					print("List after removing:", int_list)
				else:
					print("Element not found")
			else:
				print("Invalid input")
	
	elif choice == '3':
		if not int_list:
			print("List is empty")
		else:
			print(int_list)
	elif choice == '4':
		break
	else:
		print("Invalid choice")
