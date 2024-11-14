
first_num = 10
second_num = 20
def calk(num):
    print(num+second_num)

calk(first_num)

def sum_all(*args):
    result = 0
    for i in args:
        result += i
    return result
print(sum_all(1,2,3))

def price_list(**kwargs):
    print(kwargs)
    for product in kwargs.items():
        prod, coast = product
        print(prod, coast)

price_list(iphone = 100, samsung = 10, nokia = 1)
    
