from datetime import date, datetime
from numberbox.core.layer import Layer


class Box:

    PERIOD_ITERATION_CHOICES = [
        'year',
        'month',
        'day'
    ]

    LAYER_ITERATION_CHOICES = [
        'year',
        'month',
    ]

    period_iteration = None
    layer_iteration = None
    index = None
    layer_dict = dict()
    layer_index = list()

    def __init__(self, period_iteration, layer_iteration, index=None):
        if period_iteration in self.PERIOD_ITERATION_CHOICES:
            self.period_iteration = period_iteration
        else:
            raise SyntaxError('Invalid period iteration choices %s' % self.PERIOD_ITERATION_CHOICES)

        if layer_iteration in self.LAYER_ITERATION_CHOICES:
            self.layer_iteration = layer_iteration
        else:
            raise SyntaxError('Invalid layer iteration choices %s' % self.LAYER_ITERATION_CHOICES)

        if index:
            self.index = list(index)

    def update_layer(self, layer_key):
        if self.layer_does_not_exists(layer_key):
            self.create_layer(layer_key)

    def layer_does_not_exists(self, layer_key):
        if layer_key in self.layer_index:
            return False
        else:
            return True

    def create_layer(self, layer_key):
        if layer_key not in self.layer_dict:
            self.layer_dict[layer_key] = list()
            self.layer_dict[layer_key].append(Layer(layer_key))
        if layer_key not in self.layer_index:
            self.layer_index.append(layer_key)
        self.layer_index.sort(reverse=True)

    def add_period(self, period, period_list):
        if type(period) is date or type(period) is datetime:
            layer_key = period.year
            self.update_layer(layer_key)
            self.layer_dict[layer_key] =
        else:
            raise ValueError('Invalid period must be a date or datetime')