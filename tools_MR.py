# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8

####################
## tools_MR.py
####################

import os
import sys ; sys.stdout.flush()
import itertools

from multiprocessing import Pool
from multiprocessing import Pool

###########
## to_2D
###########

# tribute: https://stackoverflow.com/questions/14681609/create-a-2d-list-out-of-1d-list 

def to_2D(l):
    return [l[i:i+1] for i in range(0, len(l), 1)]

###########
# load()
###########

"""
Load the contents the file at the given
path into a big list of string (e.g. words) and return it.

@param path the full path of the file
@return the list version of the file

"""

def load(path):
 
    word_list = []
    f = open(path, "r")
    for line in f:
        # print("[DEBUG] line = ", line)
        word_list.append (line)
 
    # Efficiently concatenate Python string objects
    return (''.join(word_list)).split ()

# ==================
# chunks()
# ==================

"""
A generator function for chopping up a given list into chunks of length n.

Ex.

[See http://sametmax.com/comment-utiliser-yield-et-les-generateurs-en-python/]
"""

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
 
# ==================
# tuple_sort()
# ==================
  
"""
Sort tuples by term frequency, and then alphabetically.
a and b share the format (w,freq).
"""

def tuple_sort (a, b):
    
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return cmp(a[0], b[0])

# ====================
# sanitize_word()
# ====================

"""
Sanitize a single word independently from the others.
Apply the Business Rules (BR) defined in the sanitize()
function.

@param w the word to be sanitized
@return a list of strings for the sanitized version of the word. This list can be a singleton or can have more elements

"""

def sanitize_word(w):

    print("w={}".format(w))

    if not w.isalnum():
        # ex. what's, ...
        i = w.find("'")
        if i != -1:
            p1 = w[0:i]
            if w[i+1:] == 's':
                p2 = 'is'
            elif w[i+1:] == 'll':
                p2 = 'will'
            # PUT other transformation rules here
            return [p1,p2]
        else:
            if len(w) > 0:
               # Strip punctuation from the front or the back
               if not w[0].isalnum():
                   return [w[1:]]

               if not w[-1].isalnum():
                   return [w[:-1]]

            else:
                return []

    # the word isalnum()
    return [w]

# ===================
# sanitize()
# ===================


"""
New version: work on a copy of text

BR1: 
If a token has been identified to contain
non-alphanumeric characters, such as punctuation,
assume it is leading or trailing punctuation
and trim them off.

BR2:
For internal punctuation,
what's => what is
I'll => I will
...

@param text the text as a list of words
@return a sanitized version of the text. 

"""

def sanitize(W):	
	# to return a 2D list 
	return [sanitize_word(w) for w in W]
	# to convert to 1D list 
	# return list(itertools.chain.from_iterable([sanitize_word(w) for w in W]))
			
			

# ======================
# wordcount_mapper()
# ======================

"""
The combo mapper will define a (complex) map function.
Here, from a list of words, each word w is sanitized and one or several tuples
(w_1,1) ... (w_n, 1)  are emitted when the sanitization of w produced [w_1, ..., w_n]

@param L the list of words
@return [(w_1,1) ... (w_n, 1)] list of intermiate result formated as tuples
"""

def wordcount_mapper(L):

    print("[DEBUG] wordcount_mapper in process id = {}".format(os.getpid()))

    try: 

        results = []
        for w in L:
            res = sanitize_word(w)
            # N cases here: [e] or [e1,e2] or [e1,e2, ...]
            for r in res:
                results.append((r, 1))

        return results

    except:
        print("[ERROR] In wordcount_mapper() = ", sys.exc_info()[0])

    return []

# ======================
# wordcount_shuffle()
# ======================
    
"""
Group the sublists of (token, 1) pairs into a term-frequency-list
map, so that the Reduce operation later can work on sorted
term counts.

Notice that the term-frequency here is always equal to 1.

@param LL a list of list with the structure:

    [
       [('So', 1), ('what', 1), ('is', 1), ...],     => the tuples for doc 1
       [('The', 1), ('man', 1), ... ],               => the tuples for doc 2
       ...
    ]

@return a dictionary with the structure {token : [(token, 1), ...], ... }
"""

def wordcount_shuffle(L):

    print("[DEBUG] wordcount_shuffle() in process id = {}".format(os.getpid()))
    
    try:
        
        tf = {}
        for sublist in L:
            for p in sublist:
                # Append the tuple to the list in the map
                try:
                    tf[p[0]].append(p)
                except KeyError:
                    # the 1st time the key is encountered
                    tf[p[0]] = [p]
        return tf

    except:
        print("[ERROR] In partition() = ", sys.exc_info()[0])

    return {}
 
# ======================
# wordcount_reducer()
# ======================


"""
Given a (token, [(token, 1) ...]) tuple, collapse all the count tuples from the Map
operation into a single term frequency number for this token

@param emit_dict_entry the list of intermediate results for a given token. format = (token, [(token, 1) ...])
@return a final tuple (token, frequency) with frequency = sum of all frequency of the intermediate results

"""

def wordcount_reducer(emit_dict_entry):
        
    print("[DEBUG] wordcount_reducer in process id = {}".format(os.getpid()))
    return (emit_dict_entry[0], sum(pair[1] for pair in emit_dict_entry[1]))




		
		


