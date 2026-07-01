from storage.storage import IStorage
import json
from models.document import Document

class JsonStorage(IStorage):
    
    def save(self,documents:list[Document]) -> bool:
        list_dict = []
        """create json and save document"""

        with open("document.json", "w") as file:

            list_dict = [doc.to_dict() for doc in documents]

            json.dump(list_dict, file, indent=4)
            
            return True
        
        return False
            
    def load(self)->list[Document]:
        """convert dict to dataclass from json
        add to list_doc"""
        
        documents = []
        try:
            with open("document.json", "r") as file:

                data = json.load(file)
                
                for item in data:
                    
                    document = Document.from_dict(item)

                    documents.append(document)
                    
                return documents
                   
            
        except FileNotFoundError:
            return []
        
        except json.JSONDecodeError:
            return []
    