class Book():
    def __init__(self,title,author,pages):#init is the special method coz it called  automatically when you create the object
        self.title=title #self. attribute are created
        self.author=author
        self.pages=pages #pages that u pass in when you created your instance of ur book
    def __str__(self):#str is special method and that return not print
     return f"{self.title}by {self.author}" #
    def __len__(self):#len is specail method return
       return len(self.title)+len(self.author)
b=Book('Python rocks','jose',200)
print(b)
print(str(b)) 
print(len(b)) 
 