##################
## simple_MR.py ##
##################

# author: Regis KLA (regis.kla@digital-brain.biz)

# tribute: https://mikecvet.wordpress.com/2010/07/02/parallel-mapreduce-in-python/
# tribute: https://stackoverflow.com/questions/14681609/create-a-2d-list-out-of-1d-list

# Run commands:

# (from interpreter and from the source code directory)
# >>> exec(open('simple_MR.py').read())

# (from command line)
# $ python simple_MR.py

from functools import reduce

###########
# to_2D()
###########

def to_2D(l):
    return [l[i:i+1] for i in range(0, len(l), 1)]

###############
# f1(), f2()
###############

f1 = lambda x: len(x)
f2 = lambda x,y: x+y

###########
# main()
###########

def main():
    print("[INFO] =============")
    print("[INFO] Main")
    print("[INFO] =============")

    print
    print("[INFO] Case 1: ")
    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    c = [8, 9, 1, 2, 3]	
    print("[INFO] a = {}, b = {}, c = {} ".format(a, b, c))
    L = map(f1, [a, b, c])
    n = reduce(f2, L)
    print("[INFO] We use MR to count the number of elements of a+b+c = {}".format(n))

    print
    print("[INFO] Case 2: ")
    # DON'T WORK
    # single = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    single = to_2D([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3])
    print("[INFO] single = {}".format(single))
    L = map(f1, single)
    n = reduce(f2, L)
    print("[INFO] We use MR to count the number of elements of single = {}".format(n))

    print
    print("[INFO] Case 3: ")
    strange = [[1], [2, 3, 4], [5], [6], [7, 8], [9], [1], [2], [3]]
    print("[INFO] strange = {}".format(strange))
    L = map(f1, strange)
    n = reduce(f2, L)
    print("[INFO] We use MR to count the number of elements of strange = {}".format(n))

    print
    print("[INFO] Case 4: ")
    W = to_2D(['So,', 'what', 'is', 'going', 'on', 'here', 'Well,', 'there', 'is', 
        'three', 'steps', 'to', 'this', 'process'])
    print("[INFO] W = {}".format(W))
    L = map(f1, W)
    n = reduce(f2, L)
    print("[INFO] We use MR to count the number of elements of W = {}".format(n))

    print
    print("[INFO] Case 5: ")
    strange = [[1], ['what', 'is', 'this'], [5], [6], [7, 8], [9], ['strange'], ['list'], [3]]
    print("[INFO] strange = {}".format(strange))
    L = map(f1, strange)
    n = reduce(f2, L)
    print("[INFO] We use MR to count the number of elements of strange = {}".format(n))


if __name__ == "__main__":
    main()

