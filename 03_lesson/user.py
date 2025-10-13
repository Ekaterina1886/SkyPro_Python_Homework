class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lastName = last_name
    def get_name (self):
        return self.name
    def get_lastName (self):
        return self.lastName
    def get_fullName (self):
        return f"User: {self.name} {self.lastName}"    