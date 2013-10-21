easycomplete
============

Want to add a dynamic & responsive autocomplete bar
to your webapp? Easycomplete is here! This is a python module 
which generates generic autocomplete results set by utilizing 
google's autocomplete along with the english dictionary. 
Potentially more sources to come in the future!

The goal is to create a general autocompletion system which a
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

>>> print map['adam']
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

FAQ
===
Q: My google autocomplete results are out of date!
A: There is a python file called retriever.py which automatically
   updates your google autocomplete. But you will need to do some
   dirtywork yourself for now as the API is still rough for users.
   Read the comments in that file for more directions, I intend on
   making this process much more user friendly once I have time!


TODO
====

- [ ] Add a fontend wrapper so users can easy sync this python
      module to twitter's typeahead module
- [ ] Fix up the retriever.py API so users can
      update their google autocomplete results with ease
- [ ] Clean this entire repo up
- [ ] Add more settings functionality to the mapper params


More to come soon! Happy coding!


http://codelucas   - Blog
http://wintria.com - Startup
