class Book:
    '''
    Class: Book contains the detail of the books. It allows comparing 
    two instances according to the rank.
    for example b1 < b2 if  b1.rank < b2.rank 
    '''

    def __init__(self, key, title, group, rank, similar):
        self.key = key
        self.title = title
        self.group = group
        self.rank = int(rank)
        self.similar = similar

    def check(self, a):
        book1 = self.title.lower()
        book2 = a.title.lower()
        for i in range(min(len(book1), len(book2))):
            if book1[i] != book2[i]:
                return i
        return -1

    def __lt__(self, a):
        '''
        This function allows to make direct comparison using the operator <
        '''
        checked = self.check(a)
        return ord(self.title[checked]) < ord(a.title[checked])

    def __le__(self, a):
        '''
        This function allows to make direct comparison using the operator <=
        '''
        checked = self.check(a)
        return ord(self.title[checked]) <= ord(a.title[checked])

    def __gt__(self, a):
        '''
        This function allows to make direct comparison using the operator >
        '''
        checked = self.check(a)
        return ord(self.title[checked]) > ord(a.title[checked])

    def __ge__(self, a):
        '''
        This function allows to make direct comparison using the operator >=
        '''
        checked = self.check(a)
        return ord(self.title[checked]) >= ord(a.title[checked])

    def __eq__(self, a):
        '''
        This function allows to make direct comparison using the operator ==
        '''
        return (self.title.lower() == a.title.lower()) and (self.key == a.key)

    def __str__(self):
        '''
        function returns a string containing the book information
        '''
        return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"
