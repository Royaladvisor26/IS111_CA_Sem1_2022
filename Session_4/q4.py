from fileinput import filename


def get_nearest_ancestor(folder_system,filename1,filename2):
  return ''

#Test 1
print ("Test 1:")
print ("Expected: A")
print ("Actual: ",end='')
folder_system = {"A": ["B", "C", "D"],
                    "B": ["E", "F"],
                    "D": ["G", "H"],
                    "G": ["I", "J"],
                    "H": ["K"]
                }
filename1 = "B"
filename2 = "C"
print(get_nearest_ancestor(folder_system,filename1,filename2))

#Test 2
print ("Test 2:")
print ("Expected: G")
print ("Actual: ",end='')
folder_system = {
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}
filename1 = "I"
filename2 = "J"
print(get_nearest_ancestor(folder_system,filename1,filename2))

#Test 3
print ("Test 3:")
print ("Expected: D")
print ("Actual: ",end='')
folder_system = {
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}
filename1 = "I"
filename2 = "K"
print(get_nearest_ancestor(folder_system,filename1,filename2))

#Test 4
print ("Test 4:")
print ("Expected: D")
print ("Actual: ",end='')
folder_system = {
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}
filename1 = "D"
filename2 = "I"
print(get_nearest_ancestor(folder_system,filename1,filename2))

#Test 5
print ("Test 5:")
print ("Expected: G")
print ("Actual: ",end='')
folder_system = {
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}
filename1 = "G"
filename2 = "G"
print(get_nearest_ancestor(folder_system,filename1,filename2))