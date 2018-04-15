# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8

########################
## one_process_MR.py  ##
########################

# author: Regis KLA (regis.kla@digital-brain.biz)

# Run commands:

# (from interpreter and from the source code directory)
# >>> import sys
# >>> sys.argv = ['./input/text.txt']
# or
# >>> sys.argv = ['./input/sentence.txt']
# then
# >>> exec(open('one_process_MR.py').read())

# (from command line)
# $ python -c "import sys ; sys.argv = ['./input/sentence.txt'] ; exec(open('one_process_MR.py').read())"
# or
# $ python -c "import sys ; sys.argv = ['./input/text.txt'] ; exec(open('one_process_MR.py').read())"


import sys ; sys.stdout.flush()

from functools import reduce
from tools_MR import sanitize, load, to_2D

#############
# main()
#############

def main(path):
    
    print("[INFO]")
    print("[INFO] =================== ")
    print("[INFO] one_process_MR.py")
    print("[INFO] =================== ")
    print("[INFO]")

    W = load(path)
    W = sanitize(W)

    # debug
    print("[DEBUG] W (prepared) = {}".format(W))

    # mapreduce 
    n = reduce(lambda x,y:x+y, map(lambda x:len(x), W))
    print("[INFO] nb words for document [{}] = {}".format(path,n))

# footer

if __name__ == "__main__":
    main(sys.argv[0])

    
