'''
Call google_download() if you'd like to update your autocomplete results
with the latest google autocomplete results. Please note that the crawler
may break at certain points in time though.

There is not a fully functional API built on this, so if you want to do anything
you really have to study the code for now... Until someone fixes it.

This is a brief library which uses Google's autocomplete data found publicly and
conveniently packages it into a python importable for your own custom applications.

>>> 26*26
676
>>> 26*26*26
17576

We are stopping here, unless someone wants
to help with multi treading/coring this

>>> 26*26*26*26
456976
>>> 26*26*26*26*26
11881376

Our logic revolves behind not making too many requests to google
We request all permutations of 3 characters, with all 26 lowercase
english letters. aaa, aab, etc

We store a set of every single auto complete result, these are "top results"
For each of these results, we expand them, ex:
    amazon -> a -> amazon
              am -> amazon
              ama -> amazon

This isn't just it though, I will add two param flags for the user.
One allows the user to disable all first person-ish phrases. We know the
infamous google auto complete: how can I ...
                               why do X people ...

Another flag will allow users to add the entire unix (english) dictionary
into their autocomplete results.

More flags will be added in the future.

In the future I will add a module/option allowing users to refresh
their autocomplete systems by resyncing with google. The frequency
of this will be based off your app'''

__author__ = 'Lucas Ou-Yang'
__date__ = 'July 4th, 2013'
__version__ = '0.0.1'

# -*- coding: utf-8 -*-

import urllib2
import itertools # lifesaver
import json
import codecs
import time
import random

url = lambda x: 'http://suggestqueries.google.com/complete/search?client=firefox&q=%s' % x

combos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Google does treat uppercase and lower case letters differently!
# We will be ignorant of uppercase and special characters for this build.

DELIM = u"^^"
SAVE_CHECKPOINT = 500

# Comment out gen_4 and change itertools.chain to remove gen_4 if
# you feel permutations of 4 characters are too many.
# For me, 3 chars takes a few hrs to crawl, 4 takes 1-2 days.

gen_1 = itertools.product(combos, repeat=1) # a, b, c, d, ... , z
gen_2 = itertools.product(combos, repeat=2) # aa, ab, ac, ad, ... , zz
gen_3 = itertools.product(combos, repeat=3)
gen_4 = itertools.product(combos, repeat=4) # aaaa, aaaz, ... , zzzz

total = itertools.chain(gen_1, gen_2, gen_3, gen_4)

def google_download():
    """After you succesfully run this method, merge your
     suggestions_unmerged.txt into the real suggestions.txt.
     When I have time I will configure this method so it behaves
     more like a real API. For now, you may have to edit the code
     yourself!"""
    results = codecs.open('suggestions_unmerged.txt', 'w+', 'utf-8')
    errors = codecs.open('errors.txt', 'w+', 'utf-8')

    # cnt of itertools.product(combos, repeat=4)
    # >>> (cnt * 0.2) / 3600
    # 25.387555555555558 hours

    count = 0
    for perm in total:
        strung = unicode(''.join(perm))
        try:
            time.sleep(random.randint(0,1)*.231467298)
            listing = json.loads(urllib2.urlopen(url(strung), timeout=3).read())[1]
            line = DELIM.join([strung] + listing)

            results.write(line + u'\r\n')
            print line
        except Exception, e:
            print str(e)
            errors.write('Error on query: ' + strung + '\r\n')
            print strung

        # Just to be safe, incase we get blocked and lose our code
        if count % SAVE_CHECKPOINT == 0:
            results.close()
            errors.close()
            results = codecs.open('suggestions_unmerged.txt', 'a+', 'utf-8')
            errors = codecs.open('errors.txt', 'a+', 'utf-8')
        count += 1

    results.close()
    errors.close()


if __name__ == '__main__':
    google_download()




