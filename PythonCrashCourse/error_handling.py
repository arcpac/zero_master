#Error Handling
def fn_try():
    boolean = True

    while boolean:
        try:
            age = int(input("Enter age: "))
            10/age
        except ValueError:
            raise ValueError
            # print("invalid input")
        except ZeroDivisionError:
            print("Zero is not valid")
        else:
            boolean = False

def sum(n1, n2):
    try:
        return n1 + n2
    except TypeError as err:
        print("Please enter numbers (" + err )
    # except (TypeError, ZeroDivisionError):
    #     print("Ooops")

def raise_error():
    boolean = True
    while boolean:
        try:
            age = int(input("Enter age: "))
            10/age
        except ValueError:
            print("invalid input")
            continue
        except ZeroDivisionError:
            print("Zero is not valid")
            break
        else:
            break
        finally:
            print('DONE')

raise_error()
