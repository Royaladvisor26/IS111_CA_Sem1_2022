def is_magic_square(d_list):
    # d_list = [[4,3,8], [9,5,1], [2,7,6]]
    
    # YOUR CODE GOES HERE
    if has_all_numbers(d_list):
        # Check row sum
        for row in d_list:
            if sum(row) != 15:
                return False
        # Check col sum
        for i in range(3): # i = 0, 1, 2
            col_sum = 0
            for row in d_list:
                col_sum += row[i]
            if col_sum != 15:
                return False 
        # Check diagonal sum 
        left_diag_sum = 0
        right_diag_sum = 0
        for i in range(3):
            left_diag_sum += d_list[i][i] 
            right_diag_sum += d_list[i][3-1-i] # 3 is the len of d_list[i]
        if left_diag_sum != 15 or right_diag_sum != 15:
            return False
    return True

# new_str = ''.join(list)

def has_all_numbers(d_list):
    return True
    
print(is_magic_square([[2,6,7],[3,5,7],[8,1,6]]))

