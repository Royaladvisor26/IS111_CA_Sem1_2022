### Q1 (*)
Write a function called `accept_login(users, username, password)` with three parameters: `users` (a dictionary of username keys and password values), `username` (a string for a login name) and `password` (a string for a password). The function should return `True` if the user exists and the password is correct and `False` otherwise.

### Q2 (**)
You are given a file in the same directory, q2.txt, which contains several encrypted messages, one on each line. The messages can be decrypted using a dictionary called `DECRYPT_DICT` which matches each character of the encrypted messages to its actual value. Write a program that decrypts the messages inside q2.txt and prints out these decrypted messages. Do make sure that the capitalisation stays the same. 

```
# Hint: The messages contain a pop culture reference ;)
```

### Q3 (***)
Given function `get_mine_count_grid` that takes in 1 parameter called `grid` which is a 2D list of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. Modify the function so that it returns a 2D list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally). Refer to the example below for the expected value.

```
num_grid = [
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["#", "-", "-", "-", "-"]
]

Expects return value of get_mine_count_grid(num_grid) to be 
[
  ["0", "0", "0", "1", "#"],
  ["0", "1", "1", "2", "1"],
  ["0", "1", "#", "1", "0"],
  ["1", "2", "1", "1", "0"],
  ["#", "1", "0", "0", "0"]
]
```

### Q4 (***)
Imagine a folder systems which is represented by dictionaries where the keys are folders `X` and the value at key `X` is the list of subfolders of `X`. For example, a folder system illustrated in the image below 
![image](https://user-images.githubusercontent.com/68893035/197354008-29aee5a8-ec20-4afc-97ee-bbf7eb255edc.png)
can be represented in a dictionary as 
```
{
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}
```
The function `get_nearest_ancestor` takes in 3 parameters `folder_system` (a dictionary of the folder system as seen previously),`filename1`(a string containing a file name),`filename2` (a string containing another file name). Modify this function so that it returns the "smallest" folder containing both `filename1` and `filename2` (the 2 files' closest ancestor). Note that `filename1` and `filename2` may not be in the same directory, but you can assume that there will always be an answer. All the files in the systems are named differently.
```
get_nearest_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B", "C") ➞ "A"

get_nearest_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "J") ➞ "G"

get_nearest_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "K") ➞ "D"

get_nearest_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "D", "I") ➞ "D"

get_nearest_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "G", "G") ➞ "G"
```