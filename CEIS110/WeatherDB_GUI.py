import sqlite3
from tkinter import *
from tkinter import ttk

class App_GUI:

    # set file name for the database
    dbFile = "weather.db"

    def __init__(self,window):
        self.wind = window
        self.wind.title('CEIS110 - WeatherDB GUI ')

        self.tree = ttk.Treeview(self.wind)
        self.tree['columns'] = (
        'TimeStamp', 'WindSpeed', 'Temperature', 'RelativeHumidity', 'WindDirection', 'BarometricPressure',
        'Visibility', 'Description')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('TimeStamp', anchor=CENTER, width=170)
        self.tree.column('WindSpeed', anchor=CENTER, width=75)
        self.tree.column('Temperature', anchor=CENTER, width=75)
        self.tree.column('RelativeHumidity', anchor=CENTER, width=110)
        self.tree.column('WindDirection', anchor=CENTER, width=100)
        self.tree.column('BarometricPressure', anchor=CENTER, width=120)
        self.tree.column('Visibility', anchor=CENTER, width=60)
        self.tree.column('Description', anchor=CENTER, width=120)

        self.tree.heading('#0', text='', anchor=CENTER)
        self.tree.heading('TimeStamp', text='Time Stamp', anchor=CENTER)
        self.tree.heading('WindSpeed', text='Wind Speed', anchor=CENTER)
        self.tree.heading('Temperature', text='Temperature', anchor=CENTER)
        self.tree.heading('RelativeHumidity', text='Relative Humidity', anchor=CENTER)
        self.tree.heading('WindDirection', text='Wind Direction', anchor=CENTER)
        self.tree.heading('BarometricPressure', text='Barometric Pressure', anchor=CENTER)
        self.tree.heading('Visibility', text='Visibility', anchor=CENTER)
        self.tree.heading('Description', text='Description', anchor=CENTER)

        self.tree.pack()

        # Filling the Rows
        self.get_data()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.dbFile) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Data from Database
    def get_data(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = " SELECT * FROM observations ORDER BY timestamp; "
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text='', values=row)

if __name__ == '__main__':
    window = Tk()
    application = App_GUI(window)
    window.mainloop()