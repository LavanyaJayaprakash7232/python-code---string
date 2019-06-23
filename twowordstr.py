'''
Get a two word string
Return True = When the first letter of two words is same
else return False
'''

#Function definition - animal_crackers
def animal_crackers(str1):
    str2 = str1.split()
    return str2[0][0] == str2[1][0]

#User input
a = input("Enter the string\n ")
output = animal_crackers(a)
print (output)
      
    
