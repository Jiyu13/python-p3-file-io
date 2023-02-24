from textwrap import dedent


with open("../test3.txt", "a") as file3:
    text = dedent("""
                Open test3.txt for appending at the end of the file without truncating it.\n
                Creates test3.txt if it does not exist.\n
    """).strip("")
    file3.write(text)

with open("../test2.txt", "a") as file2:
    file2.write('''Open test2.txt for appending at the end of the file without truncating it, \nusing ultipleline string.\n''')