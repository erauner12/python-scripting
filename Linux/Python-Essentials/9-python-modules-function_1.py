#if you do not know how many arguments will be passed into the function, you can use "*" to specify this. All parameters will be stored in the num list
#adding msg argument
def multiply(msg,*num):
#if the user returns nothing, the result will always be 0
    if len(num) == 0:
        return 0

    result = 1
    for n in num:
        # long way
        # result = result * n
        # short way
        result *= n
    return msg + str(result)

#convert integer to string
print(multiply("The Answer is",5,2))

#can no longer use this function as it it does not have string parameter
#print(multiply(5))
