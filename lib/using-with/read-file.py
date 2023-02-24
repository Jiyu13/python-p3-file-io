#  with statement, automatically call test_file.close()
with open("../test.txt", encoding="utf-8") as test_file:
    test = test_file.read()
    print(test)

    # This is test file.
    # Hello from the test file. 