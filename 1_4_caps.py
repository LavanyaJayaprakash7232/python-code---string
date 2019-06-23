'''
Program to accept a string and return a string whose 1st and 4th letter capitalized
'''

#Function to capitalize
def lettercaps(string):
    if len(string) > 3: #Length should be greater the 4 since the criteria says 4th letter should be capitalized
        str1 = string[:4]
        str2 = string[4:]
        return str1.capitalize() + str2.capitalize()
    else:
        return "The name is too short"

a = input("Enter a string \n")
result = lettercaps(a)
print (result)
