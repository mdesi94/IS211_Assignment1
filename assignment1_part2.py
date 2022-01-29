
# create book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# function to display title/author
    def display(self):
        print(self.title + ' written by ' + self.author)

#call function
if __name__ == '__main__':

    book1 = Book('To Kill a Mockingbird', 'Harper Lee')
    book2 = Book('Of Mice and Men', 'John Steinbeck')

    book1.display()
    book2.display()
