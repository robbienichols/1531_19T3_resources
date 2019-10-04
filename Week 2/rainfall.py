'''
Compute the average of only the positive elements in the list.

assumptions:
    not counting non-positive numbers as entries either i.e. they don't add to the list length
    average of non-numeric input = None
'''
def rainfall(integers):
    if type(integers) == list:
        #lambda structure-> arguments : expression
        #filer takes in:
            #iterable object (in this case a list)
            #function with a true/false return: t/f is how we accept or reject variables from the iterable
        posNumbers = list(filter(lambda x: x > 0, integers))
        if len(posNumbers) > 0:
            return sum(posNumbers) / len(posNumbers)
    return None

def test_rainfall_1():
    assert rainfall([1,2,3]) == 2

def test_rainfall_2():
    assert rainfall([1]) == 1

def test_rainfall_3():
    assert rainfall([]) == None

def test_rainfall_4():
    assert rainfall("hi") == None

def test_rainfall_5():
    assert rainfall([-1,-4,-3]) == None

def test_rainfall_6():
    assert rainfall([2,-2,3,-3]) == 2.5

if __name__ == '__main__':
    print(rainfall([1,2,5,6,7,8,9,3,4,5]))