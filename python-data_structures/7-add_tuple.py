#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    a1, a2 = tuple_a if len(tuple_a) >= 2 else tuple_a + (0, ) * (2 - len(tuple_a))
    b1, b2 = tuple_b if len(tuple_b) >= 2 else tuple_b + (0, ) * (2 - len(tuple_b))

    return (a1 + b1, a2 +b2)
