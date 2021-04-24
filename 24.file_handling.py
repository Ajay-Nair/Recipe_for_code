# Write "Hello, World" in a file.

f = open("Hello World.txt","w")#create a file and write
f.write("Hello World")
f.close()
f = open("Hello World.txt","r")
print(f.read())


#"x" - Create - will create a file, returns an error if the file exist

#"a" - Append - will append to the end of the file, will create a file if the specified file does not exist

#"w" - Write - will overwrite any existing content, will create a file if the specified file does not exist
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist