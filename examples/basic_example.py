import parchment
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

new_box = parchment.Grid(row_index)
new_box.add_period(datetime(2020, 4, 1), period_data)
new_box.add_period(datetime(2020, 5, 1), other_period_data)
new_box.add_period(datetime(2020, 6, 1), period_data)
new_box.add_period(datetime(2020, 7, 1), other_period_data)
print(new_box.to_dict())
