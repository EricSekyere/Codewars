'''
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, 
with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. 
It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]


Ivalid Arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

comp(a,b) returns false because in b 36100 is not the square of any number of a.



'''

def comp(a, b):
    if not (type(a) == list and type(b) == list):
        return False
    elif not a and not b:
        return True
    else:
        a.sort()
        b.sort()
        value = sum([0 if i**2 == j else 1 for (i, j) in zip(a, b)])
        return True if value == 0 else False
