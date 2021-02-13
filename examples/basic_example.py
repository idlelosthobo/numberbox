import parchments
from datetime import datetime

row_index = (
    ('Debt', 'dollar', 2),
    ('Revenue', 'dollar', 2),
    ('Ratio', 'percentage', 4),
    ('Days', 'int', 0),
)

period_data = [
    200000.00,
    30000.00,
    0.7500,
    22,
]

other_period_data = [
    120000.00,
    60000.00,
    0.5000,
    14,
]

my_grid = parchments.Grid(row_index)

my_grid.add_period(datetime(2020, 4, 1), period_data)
my_grid.add_period(datetime(2020, 5, 1), other_period_data)

my_grid.add_period(datetime(2021, 4, 1), other_period_data)
my_grid.add_period(datetime(2021, 5, 1), period_data)

print(my_grid.get_row('Debt').as_dict())

