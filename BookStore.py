import Book_old
import ArrayList
import ArrayQueue
# import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
# import AdjacencyList
import time
import MaxQueue
import algorithms


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()  # MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                # self.bookIndices.add(key, self.bookCatalog.size() - 1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s}) \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt: int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        x = 0
        for book in self.bookCatalog:
            if infix in str(book.title):
                print(book)
                x += 1
            if x >= cnt:
                break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        '''
        getCartBestSeller: returns best-seller amongst the rest of the books in the cart
        '''
        print(f"getCartBestSeller returned")
        print(self.shoppingCart.max().title)
        return self.shoppingCart.max().title()

    def addBookByKey(self, key):
        start_time = time.time()
        indicies = self.bookIndices.find(key)
        if indicies == None:
            print("Book not found.")
        else:
            dicies = self.bookCatalog.get(indicies)
            self.shoppingCart.add(dicies)
            print(f"Added title: {dicies.title}")
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        book = self.sortedTitleIndices.find_smallest_right_node(prefix)
        if book.k[0:len(prefix)] == prefix:
            if len(prefix) > 0:
                self.shoppingCart.add(self.bookCatalog.get(book.v))
                print("Added first matched title: " + book.k)
            else:
                print("Error: Prefix was not found.")
        else:
            print("Error: Prefix was not found.")

    def bestsellers_with(self, infix, structure, n=0):
        if infix == "":
            print("Invalid infix.")
        elif n < 0:
            print("Invalid number of titles.")
        elif structure != 1 and structure != 2:
            print("Invalid data structure.")
        else:
            start_time = time.time()
            if structure == 1:
                best_seller = BinarySearchTree.BinarySearchTree()
                for books in self.bookCatalog:
                    if infix in books.title:
                        best_seller.add(books.rank, books)
                results = best_seller.in_order()
                results.reverse()
                for pages, result in enumerate(results):
                    if pages >= n > 0:
                        break
                    print(result.v)
            elif structure == 2:
                best_seller = BinaryHeap.BinaryHeap()
                for books in self.bookCatalog:
                    if infix in books.title:
                        books.rank *= -1
                        best_seller.add(books)
                for jam in range(best_seller.size()):
                    if jam >= n > 0:
                        break
                    jelly = best_seller.remove()
                    jelly.rank *= -1
                    print(jelly)

            elapsed_time = time.time() - start_time

            print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")

    def sort_catalog(self, s):
        start_time = time.time()
        if s == '1':
            algorithms.merge_sort(self.bookCatalog)
        elif s == '2':
            algorithms.quick_sort(self.bookCatalog, 0)
        elif s == '3':
            algorithms.quick_sort(self.bookCatalog, 'hallo')
        else:
            print('Invalid algorithm')
            return False
        elapsed_time = time.time() - start_time
        print(f'Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds')
        return True

    def display_catalog(self, n):
        for logs in range(int(n)):
            print(self.bookCatalog.get(logs))
