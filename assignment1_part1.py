# function to check whether numbers is divisible by divide
def listDivide(numbers, divide = 2):
    total = 0
    for number in numbers:
        if number % divide == 0:
            total += 1
    return total

#create exception class
class listDivideError(Exception):
    pass


def testListDivide():
#Test listDivide function
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100], divide = 10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)

    except Exception:
        raise listDivideError("cannot divide numbers list by divide value")




if __name__ == "__main__":
    testListDivide()
