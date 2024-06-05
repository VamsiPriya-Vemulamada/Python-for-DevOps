# for file handling,in python we can use any kind of file like csv or txt or any binary text file
# for file to read, write, append or enter the data along the files we will use the following with open() function

# Opening and reading the files
file = open('Metlife.txt', 'r')
print(file.read())
print(file.readline(1))
# print(file.readlines())

# Opening and Writing the files
file = open('Metlife.txt', 'w')
file.write("I'm adding more digits \n" " 5 \n" "\n 6")
# the above statement also overrides the existing statements

# Opening and appending the files
file = open('Metlife.txt', 'a')
file.write("\n one more")



