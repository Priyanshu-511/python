f = open("file.txt",'w')
f.write('''
    hello guys! this will re-writable in file.txt
''')
f.close()

f = open("file.txt",'r')
text = f.read()
f.close()
print(text)