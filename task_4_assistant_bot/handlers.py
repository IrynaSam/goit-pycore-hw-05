from decorators import input_error

@input_error
def add_contact(args, contacts):
    if len(args)<2:
        raise ValueError 
    name, phone = args
    contacts[name] = phone

    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args)<2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    else: 
        raise KeyError
        
    return  "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        return contacts[name]
    else: 
       raise KeyError

@input_error
def show_all(contacts):
    if not contacts:
        raise ValueError
    
    max_name_length = max(len(name) for name in contacts)
    
    all_contacts = "Contact List:\n"+ "-"*(max_name_length + 15) + "\n"
    for name, phone in contacts.items():
        all_contacts +=f"{name.ljust(max_name_length)}: {phone}\n"
   
    return all_contacts.strip()
            