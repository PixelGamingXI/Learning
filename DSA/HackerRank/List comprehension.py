
if __name__ == '__main__':
    n = int(input())

    my_list =[num for num in range(n+1) if num % 2 == 0]
    print(my_list)
    sq_list = [num**2 for num in my_list]
    print(sq_list)