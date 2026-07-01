
from repositories.document_repository import DocumentRepository
from models.document import Document

class DocumentService:
    def __init__(self,repository:DocumentRepository):
        self.repository = repository
    
    def document_by_id(self,doc_id):
        return self.repository.find_by_id(doc_id)
    
    def get_all_documents(self)->list[Document]:
        '''Nhận list từ repo để xử lý business'''
        docs = self.repository.get_all()
        
        return sorted(docs,key=lambda d: d.title)
    
    def delete_document(self,doc_id:int)->bool:
        '''truyền repository xử lý delete'''
        return self.repository.delete_by_id(doc_id)
               
    def create_document(self,
                        doc_id:int,
                        doc_title:str,
                        doc_content:str,
                        doc_author:str)-> bool:
        '''First check the id not in list
        - Second check the title not in list & not empty
        - Third create new doc
        - Four call repo to Add()
        -> The result True of False'''

        
        if self.repository.find_by_id(doc_id)!= None:
            return False        
        
        if not doc_title.strip():
            return False
        
        if self.repository.find_by_title(doc_title) != None:
            return False
        
        doc = Document(
            id = doc_id,
            title=doc_title,
            content =doc_content,
            author=doc_author
        )
        
        self.repository.add(doc)
        
        return True
    
    
    def update_title(self,document,new_title)->Document:
            document.title = new_title
            return document
        
    def update_content(self,document,new_content)->Document:
            document.content = new_content
            return document
            
    def update_author(self,document,new_author)->Document:
            document.author = new_author
            return document
        
        
        
    def load(self):         
        return self.repository.load()
    
    def save(self):
        return self.repository.save()