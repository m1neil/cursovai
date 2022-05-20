class Client:
    def __init__(self):
        self._id = None
        self._first_name = ""
        self._last_name = ""
        self._email = ""
        self._password = ""
        self._phone = ""
        self._age = 0
        self._work_place = ""
        self._work_position = ""
        self._salary = 0.0
        self._credit = 0.0
        self._sum_use_credit = 0.0
        self._credit_days = 0,
        self._regular_client = 0
    
    # get
    def get_fname(self):
        return self._first_name
    def get_lname(self):
        return self._last_name
    def get_email(self):
        return self._email
    def get_phone(self):
        return self._phone
    def get_age(self):
        return self._age
    def get_work_place(self):
        return self._work_place
    def get_work_position(self):
        return self._work_position
    def get_salary(self):
        return self._salary
    def get_credit(self):
        return self._credit
    def get_sum_user_credit(self):
        return self._sum_use_credit
    def get_credit_days(self):
        return self._credit_days
    
    # set
    def set_id(self, user_id):
        self._id = user_id
    def set_fname(self, user_fname):
        self._first_name = user_fname
    def set_lname(self, user_lname):
        self._last_name = user_lname
    def set_email(self, user_email):
        self._email = user_email
    def set_password(self, user_password):
        self._password = user_password
    def set_phone(self, user_phone):
        self._phone = user_phone
    def set_age(self, user_age):
        self._age = user_age
    def set_work_place(self, user_work_place):
        self._work_place = user_work_place
    def set_work_position(self, user_work_position):
        self._work_position = user_work_position
    def set_salary(self, user_salary):
        self._salary = user_salary
    def set_credit(self, user_credit):
        self._credit = user_credit
    def set_sum_use_credit(self, user_sum_use_credit):
        self._sum_use_credit = user_sum_use_credit
    def set_credit_days(self, user_credit_days):
        self._credit_days = user_credit_days
    def set_regula_client(self, yes_or_no):
        self._regular_client = yes_or_no
    
        
        
        

