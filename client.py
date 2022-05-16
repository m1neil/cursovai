class Client:
    def __init__(self, fname="", lname="", email="", password="", repeat_password="", phone=""):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.password = password
        self.phone = phone
        
    def check_password(self, password):
        if self.password != password:
            return False
        else:
            return True