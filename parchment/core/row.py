from parchment.core.validation import is_valid_list_choice, is_valid_date_or_datetime
from parchment.core.block import Block
from parchment.core.choices import VALUE_TYPE_CHOICES


class Row:

    def __init__(self, name, value_type, value_decimals):
        if is_valid_list_choice(value_type, VALUE_TYPE_CHOICES):
            self.value_type = value_type
        self.value_decimals = value_decimals
        self.name = name
        self.block_order_list = list()
        self.block_dict = dict()

    def create_block(self, period_key, value):
        self.block_dict[period_key] = Block(period_key, value, self.value_type, self.value_decimals)
        self.block_order_list.append(period_key)
        self.block_order_list.sort(reverse=True)

        print(self.block_order_list)

    def update_row(self):
        for loop_index, block_order in enumerate(self.block_order_list):
            if loop_index == 0:
                if loop_index < len(self.block_order_list):
                    self.block_dict[block_order].compare_projected(self.block_dict[block_order + 1])



    def to_dict(self):
        row_list = list()
        for block_order in self.block_order_list:
            row_list.append(self.block_dict[block_order].to_dict())
        return row_list
