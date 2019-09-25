from invoice_manager import Invoice_manager
from contact_manager import Contact_manager
import os.path
import os


inv_mgr = Invoice_manager()
con_mgr = Contact_manager()
# Menu
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def auto_load():
    if(os.path.isfile(con_mgr.file_name)) == True:
        con_mgr.load_contacts()
        return True
    else:
        open(con_mgr.file_name, 'a').close()

def main_menu():
    clear_screen()
    
    if(auto_load() == True):
        print("Contact File Auto Loaded")
    
    print("Menu options:")
    print("1:\tContact Menu")
    print("2:\tInvoice Menu")

    input_option = input("Enter Option:\n")
    if (int(input_option) == 1):
        contact_menu()
    elif(int(input_option) == 2):
        main_menu()
    else:
        print("Invalid Selection")
    

def invoice_menu():
    pass
    
def contact_menu():
    clear_screen()
    print("Contact options:")
    print("1:\tCreate contact")
    print("2:\tView contacts")
    print("3:\tSave contacts")
    print("4:\tLoad contacts")
    print("5:\tModify contact")
    print("6:\tMain menu")
    
    input_option = input("Enter Option:\n")
    
    try:
        if(int(input_option) == 1):
            con_mgr.create_contact()
            print(con_mgr.contact_book)
            contact_menu()
        
        elif(int(input_option) == 2):
            con_mgr.display_contact()
        
        elif(int(input_option) == 3):
            con_mgr.save_contacts()
        
        elif(int(input_option) == 4):
            con_mgr.load_contacts()
            contact_menu()
        
        elif(int(input_option) == 5):
            user_input = input("Enter Contact ID\n")
            con_mgr.modify_contact(user_input)
            contact_menu()
        
        elif(int(input_option) == 6):
            main_menu()
        else:
            print("Invaild Option")
            main_menu()
            
    except:
        contact_menu()

main_menu()
