'''
Get a string
Return number of lowercase and uppercase characters
'''

#Function to count the characters
def up_low(string):
    up = 0
    low = 0
    string1 = string.replace(' ', '') #To remove the whitespaces
    for i in string1:
        if i==i.upper():
          up = up + 1
        elif i==i.lower():
          low = low + 1
        else:
          pass
  
          
    return f"Uppercase characters:\t {up} \nLowercase characters: \t {low}"


a = input('Enter the string \n')
result = up_low(a)
print (result)
    
