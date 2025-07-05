a = [1,2,3]
b = [4,5,6]
result = map(lambda x, y : x + y, a , b)
print("Addition of two lists: ")
print(list(result))

nums = [1,2,3,4]
def sq(n):
    return n**2

square = list(map(sq, nums))
print("Square nums in list: ", square)