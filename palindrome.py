'''
Palindrome string is a string which remains same when it is reversed
eg. 121
'''

#Function to check whether the string is palindrome or not
def palindrome(string):
    string = string.replace(' ','') #removing the whitespaces
    string = string.lower() #converting all the characters into lowercase
    if string == string[::-1]: #Reversing the string by slicing
        return f"The string {string} is a palindrome"
    else:
        return f"The string {string} is not a palindrome"

a = input('Enter a string\n ')
result = palindrome(a)
print (result)

