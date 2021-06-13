class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def reformate_date(cls, date):
        new_list = date.split('-')
        day = int(new_list[0])
        month = int(new_list[1])
        year = int(new_list[2])
        return day, month, year

    @staticmethod
    def check_date(day, month, year):
        if (day > 0 and day < 32) and (month > 0 and month < 13) and (year > 0 and year < 2022):
            print('дата введена правильно')
        else:
            print('дата введена неправильно')


if __name__ == '__main__':
    Date.check_date(31, 12, 2021)
    print(Date.reformate_date('02-11-2020'))
    first = Date('01-01-2020')
    print(first.reformate_date('03-03-2020'))
