from models.document import Document


class DocumentRepository:

    def __init__(self,storage):
        self.documents = []
        self.storage = storage

    def load(self)->bool:
        self.documents = self.storage.load()
        if self.documents:
            return True
        return False
    
    def save(self):
        self.storage.save(self.documents)
        
           
    def add(self, document:Document) -> None:
        """
        Thêm document vào list Document"""

        return self.documents.append(document)

    def get_all(self) -> list[Document]:
        """Trả về list tổng hợp document đã thêm"""

        return self.documents.copy()

    def find_by_id(self,doc_id:int) -> Document | None:
        """
        Tìm kiếm doc trong list docs"""
        for document in self.documents:
            if doc_id == document.id:
                return document

        return None
    
    
    def find_by_title(self,doc_title:str)->Document | None:
        for document in self.documents:
            if doc_title == document.title:
                return document
            
        return None
    

    def delete_by_id(self,doc_id:int) -> bool:
        """Tìm kiếm doc trong docs -> Xóa
        - Trả về True nếu tìm thầy và xóa thành công.
        - Trả về False nếu không tìm thấy doc"""

        document= self.find_by_id(doc_id)
        
        if document is None:
            return False
                 
        self.documents.remove(document)
        return True


