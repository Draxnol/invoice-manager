import os
import os.path

from contactmanager import ContactManager

from invoicemanager import InvoiceManager

con_mgr = ContactManager()
inv_mgr = InvoiceManager()


# Menu


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def auto_load():
    if (os.path.isfile(con_mgr.file_name)) == True:
        con_mgr.load_contacts()
        return True
    else:
        open(con_mgr.file_name, 'a').close()


def main_menu():
    clear_screen()

    if auto_load() == True:
        print("Contact File Auto Loaded")

    print("Menu options:")
    print("1:\tContact Menu")
    print("2:\tInvoice Menu")

    input_option = input("Enter Option:\n")
    if int(input_option) == 1:
        contact_menu()
    elif int(input_option) == 2:
        invoice_manager_menu()
    else:
        print("Invalid Selection")


def invoice_manager_menu():
    clear_screen()
    print("1:\tSelect contact")
    print("2:\tCreate invoice")
    print("3:\tView selected contact")
    print("4:\tView selected invoice")
    print("5:\tExport Current invoice to text file")
    print("6:\tExport Current invoice to Docx Template")
    print("7:\tMain menu")
    input_option = input("Enter option:")

    try:
        pass
    except ValueError:
        print("Error: You probably input a non-number")
        input()
        main_menu()
    if int(input_option) == 1:
        user_contact_selection = input("Enter contact ID\n")
        inv_mgr.select_contact(con_mgr.select_contact(user_contact_selection))
        invoice_manager_menu()
    elif int(input_option) == 2:
        inv_mgr.create_invoice()
        input("Invoice Created")
        invoice_manager_menu()
    elif int(input_option) == 3:
        print(inv_mgr.get_selected_contact())
        input()
        invoice_manager_menu()
    elif int(input_option) == 4:
        print(inv_mgr.current_invoice.get_date())
        print(inv_mgr.current_invoice.get_invoice_number())
        input()
        invoice_manager_menu()
    elif int(input_option) == 5:
        inv_mgr.export_current_invoice()
    elif int(input_option) == 6:
        inv_mgr.export_current_invoice_word()
    elif int(input_option == 7):
        main_menu()


def contact_menu():
    clear_screen()
    print("Contact options:")
    print("1:\tCreate contact")
    print("2:\tView contacts")
    print("3:\tSave contacts")
    print("4:\tLoad contacts")
    print("5:\tModify contact")
    print("6:\tRemove contact")
    print("7:\tMain menu")

    input_option = input("Enter Option:\n")

    try:
        if int(input_option) == 1:
            con_mgr.create_contact()
            print(con_mgr.contact_book)
            contact_menu()

        elif int(input_option) == 2:
            con_mgr.display_contact()
            contact_menu()

        elif int(input_option) == 3:
            con_mgr.save_contacts()
            contact_menu()

        elif int(input_option) == 4:
            con_mgr.load_contacts()
            contact_menu()

        elif int(input_option) == 5:
            user_input = input("Enter Contact ID\n")
            con_mgr.modify_contact(user_input)
            contact_menu()

        elif int(input_option) == 6:
            con_mgr.remove_contact()
            contact_menu()

        elif int(input_option) == 7:
            main_menu()

        else:
            print("Invaild Option")
            main_menu()

    except ValueError:
        print("Error: You probably input a non-number")
        input()
        contact_menu()


main_menu()
