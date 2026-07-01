
class MenuContainer:
    
    def menu_selection(self,controller):
        while True:
            controller.load_doc()
            
            user_select_menu = int(input("Enter menu select: "))
            
            if user_select_menu not in range(1,5):
                print('Enter 1 -> 4 only')
                continue
            try:
                if user_select_menu == 1:

                    add_doc = controller.create_document()
                    if add_doc:
                        print('Document created ! ')
                        controller.save_doc()
                    else:
                        print('Document cant add!')

                
                elif user_select_menu == 2:
                    list_doc = controller.get_all_documents()
                    for doc in list_doc:
                        print(doc)
                    
                elif user_select_menu == 3:
                    delete_doc = controller.delete_document()
                    if delete_doc:
                        controller.save_doc()
                        print('Document deleted!')
                        
                    else:
                        print('Document can not delete!')
                        
                elif user_select_menu == 4:
                    controller.update_document()
                    controller.save_doc()
                    
                elif user_select_menu == 5:
                    controller.save_doc()
                
                    break

            except Exception as e:
                print(e)