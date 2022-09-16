class DVD:
    def __init__(self, name:str, id:int, creation_year:int, creation_month:str, age_restriction:int):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.id = id
        self.name = name
        self.is_rented=False

    @staticmethod
    def num_to_month(month_number:int):
        month_to_number = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12}

        for name, number in month_to_number.items():
            if number==month_number:
                return name



    @classmethod
    def from_date(cls, id:int, name:str, date:str, age_restriction:int):
        day, month_as_number, year=date.split(".")
        month_as_number=int(month_as_number)
        month=cls.num_to_month(month_as_number)
        year=int(year)
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status="rented"
        else:
            status="not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
