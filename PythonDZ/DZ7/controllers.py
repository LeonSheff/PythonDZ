from request import action, db_view
from db import db_print, data_collector, db_save

def start_b():
    while (True):
        ansver = action()
        if ansver == 1:
            data = data_collector()
            db_save(data)
        elif ansver == 2:
            db_viev1 = db_view()
            db_print(db_view1)
        elif ansver == 3:
            break