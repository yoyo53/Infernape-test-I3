class User:
    def __init__(self, name, email, address1, address2, city, zip_code, hiring_date, job_title):
        self.name = name
        self.email = email
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.zip_code = zip_code
        self.hiring_date = hiring_date
        self.job_title = job_title

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name
    
    def get_address1(self):
        return self.address1
    
    def get_address2(self):
        return self.address2
    
    def get_city(self):
        return self.city
    
    def get_zip_code(self):
        return self.zip_code
    
    def get_hiring_date(self):
        return self.hiring_date
    
    def get_job_title(self):
        return self.job_title 