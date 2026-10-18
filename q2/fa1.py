class Publication:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
    def set_author(self, author):
        self.__author = age
    def set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def display_info(self):
        print(self.title)
        print(self.name)
        
class Book(Publication):
    def __init__(self,number_of_pages):
        self.__number_of_pages = 0
    def set_number_of_pages(self,number_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
    def get_number_of_pages(self,number_pages):
        return self.__number_of_pages
    
class Magazine(Publication):
     def __init__(self,issue_number):
        self.__number_of_pages = 0
    def set_number_of_pages(self,number_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
    def get_number_of_pages(self,number_pages):
        return self.__number_of_pages

    
               
pub1 = Publication("...","..."
print("Publication Information:")
pub1.diplay_info()
