import parchments
from parchments.core.debug import execution_time
from datetime import datetime
import pprint


row_index = (
    ('Debt', 'dollar', 2),
    ('Revenue', 'dollar', 2),
    ('Ratio', 'percentage', 4),
    ('Days', 'int', 0),
    ('Active', 'bool', 0)
)

period_data = [
    200000.00,
    30000.00,
    0.7500,
    22,
    True,
]

other_period_data = [
    120000.00,
    60000.00,
    0.5000,
    14,
    False,
]

# row_index = (
#     ('Revenue', 'dollar', 2),
# )
#
# period_data = [
#     30000.00,
# ]
#
# other_period_data = [
#     50000.00,
# ]

@execution_time
def speed_test():
    my_grid = parchments.Grid(row_index, period_iteration='month')
    my_grid.add_period(datetime(2021, 4, 1), other_period_data)
    my_grid.add_period(datetime(2021, 5, 1), period_data)
    my_grid.project_future(datetime(2021, 7, 1), 'median')

speed_test()

# my_grid = parchments.Grid(row_index, period_iteration='month')

# my_grid.add_period(datetime(2020, 4, 1), period_data)
# my_grid.add_period(datetime(2020, 5, 1), other_period_data)

# my_grid.add_period(datetime(2021, 4, 1), other_period_data)
# my_grid.add_period(datetime(2021, 5, 1), period_data)

# my_grid.project_missing()

# my_grid.project_past(datetime(2019, 4, 1))

# my_grid.project_future(datetime(2021, 7, 1), 'median')

# my_grid_dict = my_grid.as_dict(verbose_only=True)

# for column in my_grid_dict['column_data']:
#     print(column)
#
# for row in my_grid_dict['row_data']:
#     print(row)
#
# pprint.pprint(my_grid.column_index[0].key)
# pprint.pprint(my_grid.column_index[0].next_period().key)
# pprint.pprint(my_grid.column_index[0].previous_period().key)

# pprint.pprint(my_grid_dict)

# print(my_grid_dict['column_index'][0])
# print(my_grid_dict['row_data']['Debt'][0]['value']['verbose'])

