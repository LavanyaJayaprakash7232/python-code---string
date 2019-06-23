'''
Program to accept a string and return the reversed string
'''

#Function uses slcing to reverse the string
def master_yoda(string):
    str1 = string.split()
    str2 = str1[::-1]
    return ''.join(str2)

a = input("Enter a string \n")
print (master_yoda(a))
