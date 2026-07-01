from typing import Optional
from models.document import Document


class DocValidator:
    
    @staticmethod
    def check_val(
                  prompt:str,
                  error_message:str,
                  strip:bool = False,
                  convert: Optional[callable]=None,
                  max:int=None,
                  min:int=None
        ):
        while True:
            try:
                user_input = input(prompt)
                
                if not user_input:
                    raise ValueError(error_message)                   
                
                user_input = user_input.strip() if strip else user_input
                
                if convert:
                    value = convert(user_input)
                    
                else:
                    value = user_input
                
                if max and user_input > max:
                    raise ValueError(f'Value can not bigger than {max} value ')
                
                if min and user_input < min:
                    raise ValueError(f'Value can not smaller than {min} value')
                
                
            except ValueError:
                continue
                          
            return value
        

    