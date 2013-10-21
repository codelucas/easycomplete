__author__ = 'Lucas Ou-Yang'
__date__ = 'July 28th, 2013'
__version__ = '0.0.1'

# -*- coding: utf-8 -*-

import os
import itertools

ENG_LIB = 'english_lib.txt'
GOOG_SUGGEST = 'suggestions.txt'
SUG_DELIM = u'^^'

combos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

gen_1 = itertools.product(combos, repeat=1) # a, b, c, d, ... , z
gen_2 = itertools.product(combos, repeat=2) # aa, ab, ac, ad, ... , zz
gen_3 = itertools.product(combos, repeat=3)
total = [ unicode(''.join(perm)) for perm in itertools.chain(gen_1, gen_2, gen_3) ]

# This really should not be hardcoded, refer to
# the nltk module and it's wordnet library in future.
first_person = [
    'how ',
    'who ',
    'what ',
    'when ',
    'where ',
    'why ',
    'which ',
    'can i',
    'can my',
]

def get_mapper(firstperson=True, dictionary=False, fourperms=False):
    ''' Returns, in dictionary form, a mapping of inputs to
    autocomplete suggestions, thanks to Google's autocomplete and
    the english dictionary. The span of inputs ranges from all permutations
    of 1-4 length inputs. So: a, b, ..., aaz, ... zzzy, zzzz
    A few of the combinations don't have autocomplete results due to google
    restrictions.

    If the user has lots of memory and can handle all autocompletes of 4 perms
    you can set the param to true, get_mapper()['aaaz'] = ['it exists!']

    Set dictionary=True, if you want the english dictionary results in your
    autocomplete. Set firstperson=False if you don't want first person results
    in your autocomplete eg. mapper["ho"] -> u'how to get rid of acne' is
    good for some cases but bad for many more!'''
    try:
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        sug_obj = open(GOOG_SUGGEST, 'r')
        suggestions = sug_obj.read().split('\r\n')
        sug_obj.close()
    except Exception,e:
        print 'Potential IOError, check that your OS and the ' \
              '\\n, \\r\\n split code corresponds, permissions, etc'
        print str(e)
        return None

    mapper = {}

    for s in suggestions[:-1]: # Skip blank line at end
        s = s.decode('utf-8')
        l = s.split(SUG_DELIM)
        key, sugges = l[0], l[1:]
        new_sugges = []

        if not fourperms and len(key) > 3:
            continue

        if not firstperson:
            for s in sugges:
                bad=False
                for fst in first_person:
                    if s.startswith(fst):
                        bad=True
                        break
                if not bad:
                    new_sugges.append(s)

            sugges = new_sugges

        mapper[key] = sugges


    if dictionary:
        eng_obj = open(ENG_LIB, 'r')
        english_lib = [ word for word in eng_obj.read().split('\n') if len(word) > 2 ]
        for word in english_lib:
            stem = word[:2]
            for c in word[2:]: # we are safe, words filtered to len > 2
                mapper.setdefault(stem, []).append(word)
                stem += c
        eng_obj.close()

    # We store a set of every single auto complete result, these are "top results"
    # For each of these results, we expand them, ex:
    #    amazon -> a -> amazon
    #              am -> amazon
    #              ama -> amazon

    exems = [ k for k in mapper.keys() if len(k) <= 3 ]
    terms = []

    for e in exems:
        terms.extend(mapper[e])

    terms = list(set(terms))

    total_failed = []
    for strung in total:
        if not mapper.get(strung):
            total_failed.append(strung)

    for t in terms:
        if len(t) == 0:
            continue
        base=t[0]
        for char in t[1:]:
            base += char

            # our google scrape missed a few permutations
            if base in total_failed or len(base) > 3:
                q=mapper.get(base)
                if not q:
                    q = [t]
                else:
                    # too bad
                    q.insert(0, t)
                q = list(set(q))
                mapper[base] = q

    # for k,v in mapper.items():
    #    mapper[k] = sorted(mapper[k], key=lambda x:len(x))

    return mapper



if __name__ == '__main__':
    mapper = get_mapper()
    print mapper['a']
    print mapper['abc']
    print mapper['adam']
    print mapper['war']
    print mapper['am']
    print mapper['ama']
    print mapper['amaz']
    print mapper['amazo']
    print mapper['how']
    print mapper['how ']
    print mapper['gui']
    print mapper['xxx']

    # cnt = 0
    # for perm in total:
    #     strung = unicode(''.join(perm))
    #     if not mapper.get(strung):
    #         print strung, 'failed'
    #         cnt += 1
    #
    # print cnt, 'elements have no mapping'
    # print len(mapper.keys())
