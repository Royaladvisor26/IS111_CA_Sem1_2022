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
                count = 1 
            else:
                output += str(count) + n[i-1]
                count = 1
    # if n[i].isnumeric():
    #     output += str(count) + "["+n[i]+"]" 
    # else:       
    output += str(count) + n[i]
    return output

print(encode("aa22b888cc"))

# print(encode("aaabbccc") == "3a2b3c")
# print(encode("AAaabBBBBcCCd") == "2A2a1b4B1c2C1d")
# print(encode("xxyxyx") == "2x1y1x1y1x")
# print(encode("111122") == "4[1]2[2]")
# print(encode("aa22b888cc") == "2a2[2]1b3[8]2c")