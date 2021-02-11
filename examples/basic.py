import numberbox
import datetime

new_box = numberbox.Box('month', 'year')

new_box.add_period(datetime.datetime.now(), [2000, 2000, 2000, 2000])