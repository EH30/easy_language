user_input = list(str(input()))
strs = ""
count = 0

for x in user_input:
    if count == 0:
        strs += x
        count += 1
    elif x == " ":
        strs += " "
        count = 0
    elif x == "'":
        count = 0

print(strs)
