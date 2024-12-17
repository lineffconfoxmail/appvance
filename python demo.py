import math

def multiplication_table():
    multiplicator_list_one = [1,2,3,4,5,6,7,8,9]
    multiplicator_list_two = [1,2,3,4,5,6,7,8,9]
    for a in multiplicator_list_one:
        for b in multiplicator_list_two:
            # print(a)
            # print(b)
            c = a*b
            print(f"{a} * {b} = {c}")

def test(a,b):
    c = a*b
    print(c)


if __name__ == '__main__':
    # result = multiplication_table()
    test(3,5)
    # print(result)
    multiplication_table()