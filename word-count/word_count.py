import re

class WordOccurrences:

    def __init__ ( self ):
        self._occ = {}

    def add( self, word ):
        try:
            self._occ[word] += 1
        except KeyError:
            self._occ[word] = 1

    def get_dictionary (self):
        return self._occ

def word_count(word_sequence):
    occ = WordOccurrences()
    for w in re.findall(r"\w(?:[\w']*\w)?", word_sequence):
        occ.add(w.lower())
    return occ.get_dictionary()
