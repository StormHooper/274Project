import Calculator
import BookStore
import ChainedHashTable
import DLList

def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable values
        3 Print expression with values
        4 Evaluate Expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option == "2":
            while True:
                variable = input("Enter a variable: ")
                value = input("Enter its value: ")
                calculator.set_variable(variable, value)
                bites_the_dust = input("Enter another variable? Y/N: ")
                if bites_the_dust.upper() == "N":
                    break
        elif option == "3":
            expression = input("Introduce the mathematical expression: ")
            if not calculator.matched_expression(expression):
                print("Invalid expression")
                menu_calculator()
            else:
                calculator.print_expression(expression)
        elif option == '4':
            exp = input('Enter the expression: ')
            bingo = calculator.print_expression(exp)
            for i in bingo:
                if i.isalpha():
                    print('Result: Error - Not all variable values are defined.')
                    return
            print(f'Evaluating expression: {bingo}\n\
            Result: {calculator.evaluate(exp)}')
        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search for best-seller with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == "6":
            bookStore.getCartBestSeller()
        elif option == "7":
            key = input("Enter book key: ")
            bookStore.addBookByKey(key)
        elif option == "8":
            bookStore.addBookByPrefix(input('Enter prefix: '))
        elif option == "9":
            bookStore.bestsellers_with(input('Enter infix: '), int(input('Enter structure (1 or 2): ')),
                                       int(input('Enter max number of titles: ')))
        elif option == "10":
            bookStore.sort_catalog(input(f"Choose an algorithm:\n\t"
                                         f"1 - Merge Sort\n\t"
                                         f"2 - Quick Sort (first element pivot)\n\t"
                                         f"3 - Quick Sort (random element pivot)\n"
                                         f"Your selection: "))
        elif option == "11":
            bookStore.display_catalog(input("Enter the number of books to display: "))

        ''' 
        Add the menu options when needed
        '''


def palindrome():
    race = DLList.DLList()
    car = input("Enter a word/phrase: ").lower()
    for parts in car:
        if not (parts.isalpha() or parts.isnumeric()):
            car = car.replace(parts, "")
    for n in car:
        race.append(n)
    if race.isPalindrome():
        print("Result: Palindrome")
    else:
        print("Result: Not a palindrome")


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)

        option = input()
        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            palindrome()


if __name__ == "__main__":
    main()
