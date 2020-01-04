#combining arguments
def multiply(msg,*num):
#if the user returns nothing, the result will always be 0
    if len(num) == 0:
        return 0

    result = 1
    for n in num:
        result *= n
    return msg + str(result)

print(multiply("The Answer is ",5,2))
