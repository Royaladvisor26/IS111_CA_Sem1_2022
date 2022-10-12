from re import I


def encode(n):
    # Your code here
    count = 0
    output = ""
    
    for i in range(len(n)):
        if i == 0:
            count = 1
            continue
        if n[i] == n[i-1]:
            count += 1
        else:
            if n[i].isnumeric():
                output += str(count) + "["+n[i-1]+"]" 
            else:
                output += str(count) + n[i-1]
            count = 1
    if n[i].isnumeric():
        output += str(count) + "["+n[i]+"]" 
    else:       
        output += str(count) + n[i]
    return output



econded = encode("aa22b888cc")
print(econded)