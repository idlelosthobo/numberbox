from datetime import date, datetime
from calendar import monthrange


class Period:

    def __init__(self, date_or_datetime, iteration):
        if type(date_or_datetime) is date:
            self.datetime = datetime.combine(date_or_datetime, datetime.min.time())
        elif type(date_or_datetime is datetime):
            self.datetime = date_or_datetime
        else:
            raise ValueError('Invalid period. Must be a datetime.date or datetime.datetime')

        self.iteration = iteration

        if self.iteration == 'year':
            self.key = self.datetime.strftime('%Y0101')
        if self.iteration == 'month':
            self.key = self.datetime.strftime('%Y%m01')
        if self.iteration == 'day':
            self.key = self.datetime.strftime('%Y%m%d')

    def next_period(self):
        if self.iteration == 'year':
            return Period(datetime(self.datetime.year + 1, self.datetime.month, 1), self.iteration)
        if self.iteration == 'month':
            return Period(
                datetime(self.datetime.year + int(self.datetime.month / 12), ((self.datetime.month % 12) + 1), 1),
                self.iteration)
        if self.iteration == 'day':
            if self.datetime.day + 1 > monthrange(self.datetime.year, self.datetime.month)[
                    1] and self.datetime.month != 12:
                return Period(datetime(self.datetime.year, self.datetime.month + 1, 1), self.iteration)
            elif self.datetime.day + 1 > monthrange(self.datetime.year, self.datetime.month)[
                    1] and self.datetime.month == 12:
                return Period(datetime(self.datetime.year + 1, 1, 1), self.iteration)
            else:
                return Period(datetime(self.datetime.year, self.datetime.month, self.datetime.day + 1), self.iteration)

    def previous_period(self):
        if self.iteration == 'year':
            return Period(datetime(self.datetime.year - 1, self.datetime.month, 1), self.iteration)
        if self.iteration == 'month':
            if self.datetime.month - 1 == 0:
                return Period(datetime(self.datetime.year - 1, 12, 1), self.iteration)
            else:
                return Period(datetime(self.datetime.year, self.datetime.month - 1, 1), self.iteration)
        if self.iteration == 'day':
            if self.datetime.day - 1 == 0 and self.datetime.month == 1:
                return Period(datetime(self.datetime.year - 1, 12, monthrange(self.datetime.year - 1, 12)[1]), self.iteration)
            elif self.datetime.day - 1 == 0 and self.datetime.month != 1:
                return Period(datetime(self.datetime.year, self.datetime.month - 1, monthrange(self.datetime.year - 1, 12)[1]), self.iteration)
            else:
                return Period(datetime(self.datetime.year, self.datetime.month, self.datetime.day - 1), self.iteration)