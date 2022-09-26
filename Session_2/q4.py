def count_numbers(num_list):
    # Write your code here
    pass

if __name__ == "__main__":
    print('Test 1')
    num_list = [4, 6, 8, 10, -3]
    result = count_numbers(num_list)
    print("Expected: 5")
    print('Actual  : ' + str(result))
    print()

    print('Test 2')
    num_list = [4, 6, [1,2] , 10, [-1 , -3]]
    result = count_numbers(num_list)
    print("Expected: 7")
    print('Actual  :' + str(result))
    print()