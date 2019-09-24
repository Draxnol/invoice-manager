from invoice_manager import Invoice_manager
from Contact_manager import Contact_manager


inv_mgr = Invoice_manager()
con_mgr = Contact_manager()
# Menu


def main_menu():
    print("options should be:")
    print("1:\tCreate contact")
    print("2:\tView contacts")
    print("3:\tSave contacts")
    print("4:\tload contacts")
    print("5:\tmodify contact")
    input_option = input("Enter Option:\n")
    
    
    if(int(input_option) == 1):
        con_mgr.create_contact()
        print(con_mgr.contact_book)
        main_menu()
        
    if(int(input_option) == 2):
        print("launched 2")
        con_mgr.display_contact()
    
    if(int(input_option) == 3):
        con_mgr.save_contacts()
    
    if(int(input_option) == 4):
        con_mgr.load_contacts()
        main_menu()
        
    if(int(input_option) == 5):
        user_input = input("Enter Contact ID\n")
        con_mgr.modify_contact(user_input)
        main_menu()
    
    else:
        print("invalid selection")
        main_menu()


main_menu()
