
from presentation.menu_ui import DisplayUi
from container.document_container import Container
from container.menu_container import MenuContainer



def main():
    menu_container = MenuContainer()
    container = Container()
    controller = container.document_contain()
    display = DisplayUi()
    display.doc_menu()
    
    menu_container.menu_selection(controller)
            
if __name__ == '__main__':
    main()