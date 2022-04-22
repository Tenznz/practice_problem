class Addressbook:
    def __init__(self):
        self.contact_dict = dict()

    def add_contact(self, contact_data):
        self.contact_dict.update({contact_data.first_name: contact_data})

    def get_contacts(self):
        return dict(contact for contact in self.contact_dict.items())

    def del_contact(self, key):
        self.contact_dict.pop(key)

    def __str__(self):
        return self.contact_dict

    def update_contact(self, update_dict):
        self.contact_dict.update(update_dict)

    def get_contact(self, key):
        return self.contact_dict.get(key)
