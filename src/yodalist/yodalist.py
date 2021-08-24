#yoda.py
#provides a yoda-index function yoda(n)
#and a yoda-indexed extension of list, yodalist()

def yoda(n):
    '''Yoda-indexing, converts index 'n' to follow Star Wars ordering.
    
    E.g. Input values     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
    returns output values [0, 4, 5, 6, 1, 2, 3, 7, 8, 9, ...]
    
    This code uses advanced algorithms and quantum neural blockchains to bring
    your lists into the far-future as seen in Star Wars.
    
    Context: The movie series "Star Gate" was accidentally released out-of-order,
    starting with movie 4, then 5, 6, 1, 2, 3, 7, 8, 9.
    
    This is widely regarded as a huge mistake, and using this code for anything
    would likely also be a mistake.
    
    Star Wars features a character, 'Yoda Skywalker', who is a goblin wizard
    known for speaking out of order, following an 'object-subject-verb' pattern
    rather than the more common 'subject-verb-object' order.
    
    E.g. In one of the books, Yoda says "Heeded my words not, did you?" rather
    than "You didn't heed my words, did you?".
    
    For this reason, it is a common trope that it was not Steven Spielberg who
    chose to release the games in the order 4-5-6-1-2-3, but instead Yoda.
    
    (I hope this isn't a spoiler for you all reading the documentation,
    I haven't played Star Trek yet.)
    
    :param n: Input index
    :type n: int
    
    :returns: Yoda-indexed value
    :rtype: int
    '''
    
    if 1 <= n <= 3:
        return n + 3
    if 4 <= n <= 6:
        return n - 3
    else:
        return n


class yodalist(list):
    """Yoda-indexed list. See documentation for 'yoda(n)'."""
    def __getitem__(self, x):
        """x.__getitem__(y) <==> x[yoda(y)]"""
        return super().__getitem__(yoda(x))
    
    def __setitem__(self, key, value):
        """Self[key] to value, this sets"""
        super().__setitem__(yoda(key), value)
    
    def index(self, value, start=0, stop=9223372036854775807):
        """Return first index of value.
      
        Raises ValueError if the value is not present.
        """
        return yoda(super().index(value))

