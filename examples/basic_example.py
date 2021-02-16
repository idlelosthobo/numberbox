import parchments
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

my_grid = parchments.Grid(row_index)

my_grid.add_period(datetime(2020, 4, 1), period_data)
my_grid.add_period(datetime(2020, 5, 1), other_period_data)

my_grid.add_period(datetime(2021, 4, 1), other_period_data)
my_grid.add_period(datetime(2021, 5, 1), period_data)

my_grid_dict = my_grid.as_dict()

# for column in my_grid_dict['column_data']:
#     print(column)
#
# for row in my_grid_dict['row_data']:
#     print(row)
#
pprint.pprint(my_grid_dict)

# print(my_grid_dict['column_index'][0])
# print(my_grid_dict['row_data']['Debt'][0]['value']['verbose'])

