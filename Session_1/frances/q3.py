def holidaybush(n):
    # YOUR CODE GOES HERE
    for i in range(n):
        print(" "*(n-i-1), end="")
        print("*"*(2*i+1))

# DO NOT MODIFY THE BELOW TEST CASES
print('----Test Case 1----')
holidaybush(5)