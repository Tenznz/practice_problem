from addressbook import Addressbook
from contact import Contact


class Addressbook_operation:
    def __init__(self):
        self.addressbook_obj = Addressbook()

    def add_to_addressbook(self):
        first_name = input("Enter first name")
        last_name = input("Enter last name")
        phone = input("Enter phone number")
        city = input("Enter city")
        country = input("Enter country")
        state = input("Enter state")
        self.addressbook_obj.add_contact(Contact(first_name, last_name, phone, city, state, country))

    def get_from_addressbook(self):
        print([contact.__dict__ for contact in self.addressbook_obj.get_contacts().values()])

    def del_from_addressbook(self):
        key = input("Enter first name")
        self.addressbook_obj.del_contact(key)

    def update_from_addressbook(self):
        first_name = input("Enter your first name")
        update_field = int(input("Enter which field you want to update \n1.first_name\n2.last_name\n3.phone\n4.city,"
                                 "\n5.state\n6.country"))
        update_data = input("Enter update data")
        contact = self.addressbook_obj.get_contact(first_name)
        set_data = {
            1: contact.set_first_name,
            2: contact.set_last_name,
            3: contact.set_phone,
            4: contact.set_city,
            5: contact.set_state,
            6: contact.set_country
        }
        if update_field == 1:
            self.addressbook_obj.del_contact(first_name)
            first_name = update_data
        set_data.get(update_field)(update_data)
        self.addressbook_obj.update_contact({first_name: contact})
