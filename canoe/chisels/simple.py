import re


class Canoe(object):

    def __init__(self, words, invert=False):
        print words
        if hasattr(words, '__iter__'):
            esc = map(re.escape, words)
            print esc
            self._re = re.compile('(%s)' % '|'.join(esc))
        else:
            self._re = re.compile(words)
        self._invert = invert

    def __call__(self, line, buf):
        found = bool(self._re.search(line))
        if found != self._invert:
            print line
