import hashlib

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
	
def bruteForce(user_name, salt, hashed_password, min, max, digits = "0"):
	#Generate string of min length
	if digits == "0":
		digits = "0" * min
	
	#current digit count at max characters
	at_max = False
	
	while not at_max:
		if min>max:
			exit()
		#Check current digits
		if hashed_password == hash_with_sha256(digits+salt):
			print("The password for " + user_name + " is: " + digits)
			return
		else: 
			if digits == "9" * min: #exit if at last number
				at_max = True
			else:# Increase digit count
				digits = increase_digit(digits)
	#Recursive call with one more digit
	bruteForce(user_name, salt, hashed_password, min+1, max)
	
def increase_digit(digits): # increases digits using different cases
	#index
	i = len(digits) - 1
	while i >= 0:
			
		if digits[i] < "9": #if less than 9 increase
				
			if i == len(digits)-1: #Case 1: Targer is last index
				left_range = digits[:-1]
				
				#increase target digit
				target = int(digits[i]) + 1
				return left_range + str(target)

				
			elif i == 0: #Case 2: target is first index
				#increase target digit
				target = int(digits[i]) + 1
				right_range = digits[(i+1):] 

				#print(str(target) + right_range)
				return str(target) + right_range
					
			else: # Case 3: Target is not and edge
				
				if i+1 == len(digits)-1: #if right range are same numbers
					right_range = digits[i+1]
				else:
					right_range = digits[i+1:]
				
				if i-1 == 0: #if left range are same numbers
					left_range = digits[0]
				else:
					left_range = digits[:i]
					
				target = int(digits[i]) + 1
				return left_range + str(target) + right_range
			
		else:#else next digit

			if i == len(digits)-1: # Case 1 - index = last digit
				left_range = digits[:-1]
				digits = left_range + "0"
				i -= 1
			elif i == 0: # Case 2 - index = first digit
				right_range = digits[1:]
				digits = "0" + right_range
				i -= 1
			else: # Case 3 - index not an edge
				
				if i+1 == len(digits)-1: #if right range are same numbers
					right_range = digits[i+1]
				else:
					right_range = digits[i+1:]
				
				if i-1 == 0: #if left range are same numbers
					left_range = digits[0]
				else:
					left_range = digits[:i]
				digits = left_range + "0" + right_range
				i -= 1

def main():
	#Read all lines from file and pass to bruteForce
	with open("password_file.txt") as f:
		for line in f:
			current_line = line.split(",")
			hashed_password = current_line[2].rstrip('\n')
			bruteForce(current_line[0], current_line[1], hashed_password, 3, 7)
main()