#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Book:
    def __init__(self, author, title):
        self.title = title
        self.author = author

if __name__ == "__main__":        
    def display(self):
        print(self.title + ' , written by ' + self.author)
        
    book1 = Book("John Steinbeck", "Of Mice and Men")
    book2 = Book("Harper Lee", "To Kill a Mockingbird")
        
    display(book1)
    display(book2)

