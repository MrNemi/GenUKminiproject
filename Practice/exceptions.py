import traceback

try:
    num = 1/0
except Exception as exc:
    traceback.print_exc()
    print (exc)
    print(type(exc))

var = [1,2,3,4,5,6,7,8,9]
try:
    for value in var:
        print(var[value + 2])
except:
    traceback.print_exc()
    print('Index out of range!!!')