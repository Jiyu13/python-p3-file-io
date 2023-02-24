#  1. open a file, create an object name 'test'
test = open("../test.txt", encoding="utf-8", mode="r")

#  2. read a file
print(test.read())

# print out
# This is test file.
# Hello from the test file.

print(test.mode)
# r

# 3. close the file
test.close()