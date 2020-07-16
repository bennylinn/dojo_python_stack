def square(num):
    return num**2

def invoker(callback, x):
    print(callback(x))

invoker(lambda x: x + 3, 2)

my_arr = [1,2,3,4,5]
list(map(lambda x: print(x*2), my_arr))

print(list(map(lambda x: x ** 2, my_arr)))
