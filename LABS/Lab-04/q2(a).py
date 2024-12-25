string = "Hello, World!"
punctuations = ",!"
empty = ""
for i in string:
    if i not in punctuations:
        empty += i
print(empty)