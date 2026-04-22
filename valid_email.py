import re
email = input("Enter the email ID: ")

# For a valid email, there should be a @ character
# flg = -1
# for i in range(len(email)):
#     char = email[i]
#     if char == '@':
#         flg = i

# if flg != -1:        
#     print('@ is found, hence valid email')
# else:
#     print('@ not found, hence not a valid email')

# for i in range(len(email)):
#     if email[i] == '@':
#         print("Valid Email")
#         break
#     elif i == len(email) -1:
#         print("Not a valid Email")
#         break
#     else:
#         continue

# if email.find('@') != -1 and email.find('.') != -1:
#     print("Valid Email")
# else:
#     print("Invalid Email")

import re
pat = r'^\S[a-z0-9.]+@[a-z]+.[a-z]+'
result = re.match(pat, email)
if result != None:
    print("Valid Email")
else:
    print("Invalid Email")