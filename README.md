# Brute force password cipher.

Method parameters: bruteForce(user_name, salt, hashed_password, min, max)

Tests(password + salt):
1. min = 3, max = 7,
   0000000 + s - to test if method creates max digits

2. min = 3, max = 7,
   0000009 + s - to test if method reaches 9 for a digit

3. min = 3, max = 7,
   0000010 + s - to test if method changes previous digit after reaching 9
   
4. min = 3, max = 7,
   0000090 + s - to test if method reaches 9 on new digit

5. min = 3, max = 7,
   9000000 + s - to test if method reaches 9 for final digit
   
6. min = 3, max = 7,
   9999999 + s - to test if method reaches 9 on all digits
   
7. min = 3, max = 7,
   100 + s - to test if method changes can find min-digit number
   
8 min = 3, max = 7,
  9999 + s - to test if method changes finds password not of min or max size
