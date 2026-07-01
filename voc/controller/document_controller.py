from models.document import Document

UPDATE_TITLE = 1
UPDATE_CONTENT =2 
UPDATE_AUTHOR =3
EXIT = 4


class DocumentController:
    
    def __init__(self,doc_services,input_doc,display):
        self.doc_services = doc_services
        self.input_doc = input_doc
        self.display = display
        
    def update_document(self)->bool:
        doc_id = self.input_doc.get_id()
        
        document = self.doc_services.document_by_id(doc_id)
              
        if document:
            while True:
                self.display.update_doc()
                user_choice = self.input_doc.get_interger(max_val=4,min_val=1)
                
                if user_choice == UPDATE_TITLE:
                    new_title = self.input_doc.get_title()
                    self.doc_services.update_title(document,new_title)
                    print('Update successfully!')
                        
                elif user_choice == UPDATE_CONTENT:
                    new_content=self.input_doc.get_content()
                    self.doc_services.update_content(document,new_content)
                    print('Update successfully!')
                        
                elif user_choice == UPDATE_AUTHOR:
                    new_author = self.input_doc.get_author()
                    self.doc_services.update_author(document,new_author)
                    print('Update successfully!')
                        
                elif user_choice == 4:
                        print('Exit & Save changed!')
                        return 
            
            
    
    def get_all_documents(self)->list[Document]:
        
        return self.doc_services.get_all_documents()
    
    
    def create_document(self)->bool:
        doc_id = self.input_doc.get_id()
        doc_title = self.input_doc.get_title()
        doc_content = self.input_doc.get_content()
        doc_author = self.input_doc.get_author()
        
        result = self.doc_services.create_document(doc_id,doc_title,doc_content,doc_author)
        return result
    
    
    def delete_document(self)->bool:
        doc_id = self.input_doc.get_id()      
        return self.doc_services.delete_document(doc_id)
    
    
    def load_doc(self):
        
        return self.doc_services.load()
    
        
    def save_doc(self):
        
        return self.doc_services.save()
    
    
    
     