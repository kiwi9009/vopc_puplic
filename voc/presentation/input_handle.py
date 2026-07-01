from typing import Optional

class InputHandle:
    def __init__(self,validator):
        self.validator = validator
    
    def get_id(self)->int:
        return self.validator.check_val("Enter document ID: ", "id must be integer", convert=int)       
        
    def get_title(self)->str:
        return self.validator.check_val("Enter document Title: ", "Title can not be empty", True)
    
    def get_content(self)->str:
        return self.validator.check_val("Enter content: ", "Content can not be empty", True)
        
    def get_author(self)->str:
        return self.validator.check_val("Enter document author: ", "Author can not be empty", True)

        
    def get_interger(self,max_val:int=None,min_val:int=None)->int:
        
        value= int(input('Enter menu number: '))
        
        if max_val and value> max_val:
            print(f'Value can not bigger than {max_val}')
        elif min_val and value < min_val:
            print(f"Value can not smaller than {min_val}")
            
        return value
        
            
       