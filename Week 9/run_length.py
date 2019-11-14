from hypothesis import given, strategies

def encode(string):
    char = string[0]
    count_repeats = 0
    for character in string:
        #if the new character is unique, return the existing tuple
        if character != char:
            yield char, count_repeats
            char = character
            count_repeats = 1
        #current character is same as previous character
        else:
            count_repeats += 1
    yield char, count_repeats

def decode(tuple_encoded):
    result = ""
    #looks like c, 5 in (c, 5)
    for char, count in tuple_encoded:
        result += char * count
    return result


string = "hooolllaambb"
encoder1 = encode(string)
for i in encoder1:
    print(i)

print(decode(encode(string)))

# the above loop is logically equivalent to
print("-----Manual next() calls----")
encoder = encode(string)
print(next(encoder))
print(next(encoder))
print(next(encoder))
print(next(encoder))
print(next(encoder))
print(next(encoder))

@given(strategies.text())
def test_round_trip(string):
    assert decode(encode(string)) == string 