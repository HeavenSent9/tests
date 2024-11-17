my_list = [1,2,3,4,5]
new_list = map(lambda x: x*2, my_list)
print(list(new_list))



my_list_2 = [1,2,3,4,5,6,7,8,9]

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
new_list_2 = filter(is_even, my_list_2)
print(list(new_list_2))

my_list_3 = [1,2,3,4,5,6,7,8,9]

def is_even(x):
    return x % 2 == 0
new_list_3 = filter(is_even, my_list_3)
print(list(new_list_3))

my_list_4 = [1,2,3,4,5,6,7,8,9]

new_list_4 = filter(lambda x: x % 2 == 0, my_list_4)
print(list(new_list_4))