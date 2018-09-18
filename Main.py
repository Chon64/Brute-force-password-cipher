import hashlib

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def bruteForce(u, salt, hPass, min, max, digits):
	
	if len(digits)< max: #Gets max 0s
		bruteForce(u, salt, hPass, min, max, digits + "0")
	
	if hPass == hash_with_sha256(digits+salt): #Checks password
		print("The password for " + u + " is: " + digits)
		exit()
	
	#Gets current digit for check then creates a copy of digits without last digit
	currentDigit = int(digits[-1])
	newDigits = digits[:-1]
	
	#Increases current digit unless it is 9
	if currentDigit >= 9:
		return
	else:
		bruteForce(u, salt, hPass, min, max, newDigits + str(currentDigit+1))
		return

def main():
	
	testHex = "b49eb4ff02053d8b8ab54378053d90515f4b47858512f35553141edcb9849559" #hash_with_sha256('012s')
	bruteForce("Test1", "jqejia", testHex, 3, 7, "")

main()