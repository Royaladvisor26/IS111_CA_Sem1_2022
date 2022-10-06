### Q1
Implement a function called `get_cheapest_product()` . The function takes in 1 parameter, `product_list` (type: `list`). Each value is a tuple, and is of the format (name, price). Price is stated in cents. The function returns the cheapest product (i.e. minimum price) in the list. if there are 2 products with the same minimum price, return the one with the larger index (in the list).

### Q2
Implement a function called `count_odd_len()` . The function takes in 1 parameter, `str_list` (type: `list`). The function returns the number of strings whose length is odd.

### Q3
Write a program that gets 10 integer inputs from the user. The program should then display the minimum, maximum and median of all numbers entered.

**Note:**  
The median is the middle of list of numbers. For example, median of numbers 12, 4, 5 is 5. In case of odd amount of numbers, the median is the exact middle number of numbers when arranged sorted.

In case of even amount of numbers, we would get a pair of middle numbers. The median is half way between them. As an example, median of numbers 5, 12, 4, 10 is 8 (6 + 10) 2 because when placed in order the middle numbers would be 6 and 10.

**Hint:**
1. This is how you can sort a list.
```
>>> numbers = [4, 10, 1, 3, -2] 
>>> numbers. sort()
>>> numbers
[-2, 1, 3, 4, 10]
```

Sample Run:
```
Enter num 1:-9 
Enter num 2:4 
Enter num 3:-11 
Enter num 4:19 
Enter num 5:5 
Enter num 6:17
Enter num 7:1 
Enter num 8:2 
Enter num 9:8 
Enter num 10:1
Minimum of numbers: -11 
Maximum of numbers: 19 
Median of numbers: 4.0
```

### Q4
Write a function called `count_numbers` that takes in a list containing numbers and returns the count of numbers in the list. Your program has to cater to the possibility of having a list of numbers as element(s) in the input parameter. You can assume that the input parameter is at the most a 2-dimensional list.

<br>

Example 1: When the function is called as:
```
print ("Count of numbers", count_numbers([4, 6, 8, 10, -3]))
```

the expected output is:
```
Count of numbers:5
```

Example 2: When the function is called as:
```
print ("Count of numbers", count_numbers( [4, 6, [1,2] , 10, [-1 , -3] ] ) )
```

the expected output is:
```
Count of numbers:7
```