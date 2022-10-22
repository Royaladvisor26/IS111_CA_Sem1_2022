def accept_login(userList, userInput, pwdInput):
    return True

users = {
"Alice" : "helloworld",
"Ben" : "2444666668888888",
"Carlos" : "notapassword123",
"Daniel" : "noicenoicenoice",
"Emma" : "smortsmortsmort"
}

#Test 1
print ("Test 1:")
print ("Expected: Login failed...")
print ("Actual: ",end='')

if accept_login(users, "wronguser", "wrongpassword") :
    print("Login successful!")
else :
    print("Login failed...")
    
#Test 2
print ("Test 2:")
print ("Expected: Login successful!")
print ("Actual: ",end='')

if accept_login(users, "Daniel", "noicenoicenoice") :
    print("Login successful!")
else :
    print("Login failed...")
    
#Test 3
print ("Test 3:")
print ("Expected: Login failed...")
print ("Actual: ",end='')

if accept_login(users, "Ben", "12345678") :
    print("Login successful!")
else :
    print("Login failed...")