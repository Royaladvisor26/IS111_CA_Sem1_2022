<hr>
<h3>Q1</h3>
Write a program that prompts the user to enter his or her gender (M or F). If the user enters anything other than the two letters, the program will continue to prompt them until they have given a valid input.

The program should then display the salutation based on the gender (Mr. for M, Ms. for F)

Your output should look like one of these outputs when you run q1.py with the following inputs:
```
What is your gender? S
Wrong input, please enter your gender again!
What is your gender? Goma
Wrong input, please enter your gender again!
What is your gender? M
Got it! Thank you Mr.
```
```
What is your gender? Shelby 
Wrong input, please enter your gender again!
What is your gender? Uchiha
Wrong input, please enter your gender again!
What is your gender? F
Got it! Thank you Ms.
```
<hr>
<h3>Q2</h3>
Write a program that prompts the user for an integer. The program will then prompt the user to guess that number again.

If the user guesses a number that is lesser than the first prompt, the program will print "Your guess was too low."
if the user guesses a number that is higher than the first prompt, the program will print "Your guess was too high."

Incorrect guesses will cause the program to prompt the user to guess again. When the user guesses correctly, the program stops.

Sample output:
```
Enter a number to guess: 82  
Now forget all about that number, and try to guess it: 81
Your guess was too low.
Enter your guess again: 100
Your guess was too high.
Enter your guess again: 83
Your guess was too high.
Enter your guess again: 80
Your guess was too low.
Enter your guess again: 82
You got it!
```
<hr>
<h3>Q3</h3>
In a magic square, every row, column and diagonal add up to the same total. Here is a 3 by 3 magic square. The numbers 1 to 9 are placed in the grid such that no number is repeated and the sum of the three digits column-wise, row-wise and diagonal-wise is equal to 15. 

REFER TO THE IMAGE SENT IN FOLDER

The elements of the above magic square can be represented using a 2-dimensional list. The above square is represented by [[4,3,8], [9,5,1], [2,7,6]].

The following lists represent magic squares

[4,3,8],[9,5,1],[2,7,6],
[4,9,2],[3,5,7],[8,1,6],
[6,1,8],[7,5,3],[2,9,4]

while the following do not:
[5,5,5],[5,5,5],[5,5,5],
[2,6,7],[3,5,7],[8,1,6],
[10,4,1],[1,5,9],[4,6,5]

Write a function is_magic_square() that takes in a 2D list and returns True if the list contains all digits between 1 to 9 just once and if it forms a magic square, False otherwise. You can assume that a proper 3 by 3 - 2D list will be sent to the function.

Note: We suggest you design the program to contain another function that checks if only numbers from 1 to 9 are present in the list and make use of that function in is_magic_square.

Here is the expected output (for the test cases shown below):
[[4,3,8],[9,5,1],[2,7,6]] magic square? : True
[[4,9,2],[3,5,7],[8,1,6]] magic square? : True
[[6,1,8],[7,5,3],[2,9,4]] magic square? : True
[[5,5,5],[5,5,5],[5,5,5]] magic square? : False
[[2,6,7],[9,5,1],[4,3,8]] magic square? : False
[[10,4,1],[1,5,9],[4,6,5]] magic square? : False


<hr>
<h3>Q4</h3>
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a
single count and character. For example, the string "AAAABBBCCDAA"
would be encoded as "4A3B2C1D2A".

Given a string containing only digits and letters, implement run-length
encoding. To encode digits, you must encapsulate them in square
brackets to distinguish them from their respective counts.

Complete the function encode(string).

Examples:
encode("aaabbccc")
>>> "3a2b3c"
encode("AAaabBBBBcCCd")
>>> "2A2a1b4B1c2C1d"
encode("xxyxyx")
>>> "2x1y1x1y1x"
encode("111122")
>>> "4[1]2[2]"
encode("aa22b888cc")
>>> "2a2[2]1b3[8]2c"