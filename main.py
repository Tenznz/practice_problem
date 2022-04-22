from curd_operation import Addressbook_operation


def menu(option):
    ad_obj = Addressbook_operation()
    while True:
        addressbook_menu = {
            1: ad_obj.add_to_addressbook,
            2: ad_obj.get_from_addressbook,
            3: ad_obj.del_from_addressbook,
            4: ad_obj.update_from_addressbook,
            5: exit
        }
        if addressbook_menu.get(option)() == 5:
            break


if __name__ == "__main__":
    user_input = int(input("Enter 1.Add contact 2.display 3.delete 4.update 5.exit"))
    menu(user_input)
