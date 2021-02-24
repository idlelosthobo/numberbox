from datetime import date, datetime
import json
from calendar import monthrange


class Period:

    def __init__(self, date_or_datetime, iteration):
        self.data_dict = dict()
        if type(date_or_datetime) is date:
            self.data_dict['date'] = date_or_datetime
            self.data_dict['datetime'] = datetime.combine(date_or_datetime, datetime.min.time())
        elif type(date_or_datetime is datetime):
            self.data_dict['date'] = date_or_datetime.date()
            self.data_dict['datetime'] = date_or_datetime
        else:
            raise ValueError('Invalid period. Must be a datetime.date or datetime.datetime')

        self.data_dict['iteration'] = iteration

        if self.data_dict['iteration'] == 'year':
            self.data_dict['key'] = self.data_dict['datetime'].strftime('%Y0101')
            self.data_dict['verbose'] = self.data_dict['datetime'].strftime('%Y')
            self.data_dict['verbose_numeric'] = self.data_dict['datetime'].strftime('%Y-01-01')
        if self.data_dict['iteration'] == 'month':
            self.data_dict['key'] = self.data_dict['datetime'].strftime('%Y%m01')
            self.data_dict['verbose'] = self.data_dict['datetime'].strftime('%b %Y')
            self.data_dict['verbose_numeric'] = self.data_dict['datetime'].strftime('%Y-%m-01')
        if self.data_dict['iteration'] == 'day':
            self.data_dict['key'] = self.data_dict['datetime'].strftime('%Y%m%d')
            self.data_dict['verbose'] = self.data_dict['datetime'].strftime('%b %-d %Y')
            self.data_dict['verbose_numeric'] = self.data_dict['datetime'].strftime('%Y-%m-%d')

    def __str__(self):
        return self.data_dict['key']

    @property
    def key(self):
        return self.data_dict['key']

    def as_dict(self, verbose_only=False, json_dump=False):
        if verbose_only:
            return {
                'verbose': self.data_dict['verbose'],
                'verbose_numeric': self.data_dict['verbose_numeric'],
            }
        elif json_dump:
            return {
                'key': self.data_dict['verbose'],
                'verbose': self.data_dict['verbose'],
                'verbose_numeric': self.data_dict['verbose_numeric'],
            }
        else:
            return self.data_dict

    def as_list(self, verbose_only=False):
        data_list = list()
        for key, val in self.data_dict.items():
            data_list.append(val)
        return data_list

    def as_json(self, verbose_only=False):
        return json.dumps(self.as_dict())

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