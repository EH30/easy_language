import random
user_input = list(str(input()))


characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]




user_length = len(user_input)
progress = 0
count = 0
length = 10
strs = ""

for x in user_input:
    progress += 1
    
    if x == " ":
        strs = strs[:-1]
        strs += x    
    else:
        strs+= x
        
        while count != length:
            strs += str(random.choice(characters))
            count += 1
            
        
        count = 0

        if progress == user_length:
            continue
        else:
            strs += "'"

print(strs)
