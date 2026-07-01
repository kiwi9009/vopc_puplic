


class Document:
    def __init__(self,
                 id,
                 title, 
                 content,
                 author
    ):
        self.id = id
        self.title = title
        self.content= content
        self.author= author


    def __str__(self)->str:
        '''hàm return string để in class'''
        return (
            f"ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Content: {self.content}\n"
            f"Author: {self.author}"
        )
      
   
    def to_dict(self)->dict:
        '''
        funt convert dataclass to dict
        return dict'''
        return {
            'id': self.id,
            'title':self.title,
            'content':self.content,
            'author':self.author
        }
        
    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            id = data['id'],
            title=data['title'],
            content=data['content'],
            author=data['author']
        )