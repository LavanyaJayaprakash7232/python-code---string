'''
Get a string
Triple each character in the string
'''

#Function 
def paper_doll(string):
    output = ''
    for i in string:
        output=output + i *3 #triple and concatenate
    return output

a = input('Enter the string \n')
result = paper_doll(a)
print (result)
