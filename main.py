def apply_all_func(int_list,*functions):
    result={}
    for f in functions:
        result[f.__name__]= f(int_list)
    return result
def sum(list):
    result=0
    for i in list:
        result +=i
    return result
def len_fun(list):
    return len(list)
def min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
def sort(list):
    return sorted(list)
print(apply_all_func([6, 20, 15, 9], max,min,sum,sort,len_fun))