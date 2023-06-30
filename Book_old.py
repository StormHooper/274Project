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

    def __lt__(self, a):
        '''
        This function allows to make direct comparison using the operator <
        '''
        return self.rank < a

    def __gt__(self, a):
        '''
        This function allows to make direct comparison using the operator >
        '''
        return self.rank > a

    def __str__(self):
        '''
        function returns a string containing the book information
        '''
        return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"
