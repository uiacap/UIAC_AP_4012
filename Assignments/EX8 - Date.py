class DateError(Exception):
    pass


class Date():
    days_of_months = [0, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]

    def __init__(self, year=1, month=1, day=1) -> None:
        if not(type(year) == int and \
               type(month) == int and \
               type(day) == int):
            raise DateError
        self.year = year
        self.month = month
        self.day = day
        self.checker()
        
    def is_valid(self):
        return self.day <= Date.days_of_months[self.month] and self.month <= 12

    def checker(self):
        while not self.is_valid():
            if self.day > Date.days_of_months[self.month]:
                self.day -= Date.days_of_months[self.month]
                self.month += 1

            if  self.month > 12:
                self.year += 1
                self.month -= 12

    def __str__(self) -> str:
        return f"{self.year}/{self.month}/{self.day}"
        
    def __add__(self, other):
        if isinstance(other, int):
            self.day += other
            self.checker()
            return self

    def __sub__(self, other):
        if isinstance(other, Date):
            return self.all_days() - other.all_days()
            
    def all_days(self):
        _days = ((self.year - 1) * 365) + self.day
        _days += (self.month - 1) * 31 if self.month < 8 else 186 + (self.month - 7) * 30
        return _days
    
    def convert2miladi(self):
        days = self.all_days() + 622 * 365 + 78
        years = days // 365
        days %= 365
        
        # Feb - Jan - Mar - Apr - May - Jun - Jul - Aug - Sep - Oct - Nov - Dec
        miladi_days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        months = 0
        next_month = 0
        for i in miladi_days_of_months:
            next_month = days // i
            if next_month == 0:
                break
            days -= i
            months += 1
        return f'{months + 1}.{days + 1}.{years}'

    def __iter__(self):
        self.iter_starting_day = 1
        self.iter_starting_month = 1
        return self
    
    def __next__(self):
        self.iter_starting_day += 1
        while True:
            res = Date(self.year, self.iter_starting_month, self.iter_starting_day - 1)
            if res.month == self.month and res.day > self.day:
                raise StopIteration
            return res
    

d1 = Date(1382, 1, 23)
d2 = Date(1402, 2, 23)

print(d1.convert2miladi())
