#book class
class Book:
    #init constructor
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year


    #del constructor
    def __del__(self):
        print(f'Deleting {self.title}')


    #str constructor
    def __str__(self):
        return f'{self.title} by {self.author}, published in {self.year}'
    

    #actual repr constructor
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"