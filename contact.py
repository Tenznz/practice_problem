class Contact:
    def __init__(self, first_name, last_name, phone, state, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return self.first_name, self.last_name, self.phone, self.city, self.state, self.country

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_phone(self, phone):
        self.phone = phone

    def set_state(self, state):
        self.state = state

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.country = country
