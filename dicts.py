#Dictionaries are used to store key value pairs on a program
# It can be expressed as...
customer = {
    "name" : "David Don",
    "E-mail" : "Daviddon@gmail.com",
    "Phone" : 8131267643,
    "is_adult" : True
}
# To access the information in the dicts we either use square brackets
# or the .get function
print(customer["name"])
# or
# We can also add new key value pairs to a dictionary
customer.get('Birthdate', "Jan 1 1199")

print(customer.get('name'))
# Example to show how you can access the dictionary.r86586
# A program that converts digits to words
digits = input('Enter digits: ')
digit_conv = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' :'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
    '0' : 'Zero'
}
output = ""
for ch in digits:
    output += digit_conv.get(ch, "!") + ' '
print(output)


# Emoji converter
# we pair smiley faces with symbols so when we enter that symbol, the program
# outputs the smiley faces attached to that symbol.
message = input('Enter message: ')
words = message.split(" ")
emoji = {
    ":)" :   "😁",
    ":(" : "😢",
    "::" : "😠"
}
output = ""
for word in words:
    output = output + emoji.get(word, word) +  " "
print(output)