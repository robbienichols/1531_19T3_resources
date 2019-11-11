
class Fib():
    def __init__(self):
        self._lower = 0
        self._upper = 1
    
    def __next__(self):      
        self._result = self._lower + self._upper
        self._lower = self._upper
        self._upper = self._result
        if self._result > 1000:
            raise StopIteration
        return self._result
    
    def __iter__(self):
        return self
fib = Fib()

for number in fib:
    print(number)   

fib1 = Fib()
for number in fib1:
    print(number)





