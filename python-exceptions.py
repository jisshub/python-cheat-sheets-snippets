# python excepition

# try:
#     num1 = int(input("Number: "))
#     print(f"Square of {num1} is: {num1**2}")
# except Exception:
#     print("is not an integer")
# finally:
#     print("execution finished")


# raising a custom exception
def func(num, num2):
    try:
        if not num / num2 :
            raise ZeroDivisionError
        else:
            return f"{num} is divisible by {num2}"
    except ZeroDivisionError:
        return f"num2 should not be 0"
    finally:
        print("finished")
print(func(56, 20))

# in functions finaly block is executed before the function returns