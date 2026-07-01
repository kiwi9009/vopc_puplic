class Container:
    
    def document_contain(self):
        from repositories.document_repository import DocumentRepository
        from services.document_service import DocumentService
        from controller.document_controller import DocumentController   
        from presentation.input_handle import InputHandle
        from utils.validator import DocValidator
        from presentation.menu_ui import DisplayUi
        from storage.storage import IStorage
        from storage.json_storage import JsonStorage

        display=DisplayUi()
        validator = DocValidator()
        get_input = InputHandle(validator)
        json_storage = JsonStorage(IStorage)
        storage = IStorage(json_storage)
        repo = DocumentRepository(storage)
        service = DocumentService(repo)
        return DocumentController(service,get_input,display)