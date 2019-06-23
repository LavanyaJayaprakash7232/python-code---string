'''
Get a string
If first word is 'Is' - return the string as it is
else - return Is + string
'''

mystring = input("Enter the string\n")
lmystring = mystring.split()
if lmystring[0] == 'Is':
    print(mystring)
else:
    print('Is ' + mystring + '?')
   
