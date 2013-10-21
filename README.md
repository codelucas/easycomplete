easycomplete
============

Want to add a dynamic & responsive autocomplete bar
to your python webapp? Easycomplete is here! Easycomplete
is a python module which generates you a generic autocomplete
result set by utilizing google's autocomplete along with the english
dictionary and potentially more in the future.

Our goal is to create a general autocompletion system which a
broad scope of webapps can use.

This is the first release so the API isn't super user friendly
but it works. You can tailor your settings with a few params.

Below are examples. I intend on updating this module frequently.
One big update I have in mind is to write a wrapper to sync this
directly with Twitter's frontend typeahead! So users can literally
generate an autocomplete on their search bars with zero work.

Please feel free to join in!

Example usage
=============

```python
>>> from easycomplete import easycomplete

# quite a bit of memory, on my webapps I call this once
# and push all the results into static json urls to save RAM.
# automated functionality for this can be added later

map = easycomplete.get_mapper()

>>> print mapper['adam']
[u'adam levine', u'adam sandler', u'adam carolla', u'adam lambert' ... ] # limited to 10 results

# Demo of the firstperson settings
>>> map1 = easycomplete.get_mapper(firstperson=False)
>>> map1['how']
[u'howards']

>>> map2 = easycomplete.get_mapper()
>>> map2['how']
[u'how i met your mother', u'how to tie a tie', u'how to take a screenshot on a mac'

# We also have a few more setting options. Check the internal get_mapper()'s params!
```

TODO
====

- [ ] *** Add a fontend wrapper so users can easy sync this python
      module to twitter's typeahead module
- [ ] Fix up the retriever.py API so users can
      update their google autocomplete results with ease
- [ ] Clean this entire repo up
- [ ] Add more settings functionality to the mapper params


More to come soon! Happy coding!


http://codelucas   - Blog
http://wintria.com - Startup