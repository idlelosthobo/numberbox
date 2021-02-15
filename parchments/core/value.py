from decimal import Decimal


class Value:

    def __init__(self, value, value_type, decimals=2):
        self.data_dict = {
            'raw': value,
            'clean': value,
            'verbose': self.verbose(value, value_type),
            'type': value_type,
            'decimals': decimals,
        }

    def __truediv__(self, other):
        return self.data_dict['raw'] / other.data_dict['raw']

    def __mul__(self, other):
        return self.data_dict['raw'] * other.data_dict['raw']

    def __add__(self, other):
        return self.data_dict['raw'] + other.data_dict['raw']

    def __sub__(self, other):
        return self.data_dict['raw'] - other.data_dict['raw']

    def verbose(self, value, value_type):
        if value == 0 or value == 0.0 or value == Decimal(0.0):
            return '-'
        elif value_type == 'dollar':
            return '${:,.2f}'.format(value)
        elif value_type == 'percentage':
            return '{:,.4f}%'.format((value * 100))
        elif value_type == 'int':
            return '{:,.0f}'.format(value)
        else:
            return value

    def as_dict(self):
        return self.data_dict

    def as_list(self):
        value_list = list()
        for key, val in self.data_dict.items():
            value_list.append(val)
        return value_list

