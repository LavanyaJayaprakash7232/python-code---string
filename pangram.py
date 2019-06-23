'''
Pangram is a string which contains all the alphabets from a-z
'''

import string #to get the alphabets 

#Function to check whether the string is pangram or not
def pangram(mystring, alphabet = string.ascii_lowercase):
    if set(alphabet) <= set(mystring):
        return f"The string {mystring} is a pangram"
    else:
        return f"The string {mystring} is not a pangram"

a = input('Enter the string \n')
result = pangram(a)
print (result)

