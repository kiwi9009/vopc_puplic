

class IStorage:
    def __init__(self,json_storage):
        self.documents = []
        self.json = json_storage
         
    def save(self,documents):
        return self.json.save(documents)
    
    def load(self):
        return self.json.load()