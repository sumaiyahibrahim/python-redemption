with open("sample.txt", 'w') as f:
    f.write("Hello this is a text file\n")
    f.write("this is the second line\n")
    f.write("this is the third line\n")

with open("sample.txt", 'a') as f:
    f.write("this is the fourth line\n")

with open("sample.txt", 'r') as f:
    print(f.read())
