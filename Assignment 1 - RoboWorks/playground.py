def manipulate(something):
    print(something[2])
    print(something[1])
    something[2] = something[1]
    return something
print(manipulate({1:"one",2:"two"}))