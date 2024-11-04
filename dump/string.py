n = input("Enter the name: ")
a = input("Enter the date: ")

letter = '''
    Dear Name,
    You are the person who learning python.
    I'm python interface.
    I'm glad to meet you.
    Date
'''

letter = letter.replace("Name",n)
letter = letter.replace("Date",a)

print(letter)