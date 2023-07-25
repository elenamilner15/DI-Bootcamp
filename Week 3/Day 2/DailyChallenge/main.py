import math
class Pagination:
    def __init__(self, items= [], pageSize=10):
      
        self.items = items
        self.pageSize = int(pageSize)      
        self.totalPages = math.ceil(len(self.items)/self.pageSize)    
      
    currentPage = 1  

    def getVisibleItems(self):        
        f_index = (self.currentPage - 1) * self.pageSize
        l_index = f_index + self.pageSize            
        return self.items[f_index:l_index]
        
    def prevPage(self):
        if self.currentPage > 1:
            prevPage = self.currentPage - 1
            self.currentPage = prevPage            
        else:
            prevPage = self.currentPage
            self.currentPage = prevPage
            print("First page does not have previous page")
    
    def nextPage(self):
        if self.currentPage < self.totalPages:
            nextPage = self.currentPage + 1
            self.currentPage = nextPage           
        else:
            nextPage = self.currentPage
            self.currentPage = nextPage
            print("Last page does not have next page")      

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, page_number):
        if page_number > self.totalPages:
            print("This number is too big")
            self.currentPage = self.totalPages
            
            
        elif page_number < 1:  
            print("The number should not be less than 1")          
            self.currentPage = 1
        else:
            self.currentPage = page_number           
        return self

# Example usage:
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

p.prevPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())

p.firstPage()
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems())
p.prevPage()

print(p.getVisibleItems())
p.goToPage(10)
print(p.getVisibleItems())
p.goToPage(-2)
print(p.getVisibleItems())
p.goToPage(2)
print(p.getVisibleItems())
