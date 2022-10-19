fileReader = open("dummy.txt", "rt")

text = fileReader.read()
print(text)

lines = text.split("\n")

counter = 1
for line in lines:
    print(str(counter) + ": " + line)
    counter += 1
