#contact lib
contact_lib = {}
#add a contact by first assigning an id
contact_id = "test1"
contact_lib[contact_id] = {}
contact_id = "test2"
contact_lib[contact_id] = {}
print(contact_lib)
contact_lib["test1"]["contact_name"] = ""
contact_lib["test2"]["contact_name"] = ""
print("..................")
print(contact_lib)
