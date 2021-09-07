from RPA.Browser.Selenium import Selenium
from RPA.Dialogs import Dialogs
from RPA.HTTP import HTTP
from RPA.Tables import Tables

import csv

class Orders:
    
    def open_website_and_close_modal(self, url):
        browser = Selenium()
        browser.open_available_browser(url)
        browser.click_button_when_visible('css:.btn.btn-dark')
        
    def get_orders(self):
        dialog = Dialogs()
        http = HTTP()
        tables = Tables()

        dialog.add_heading('Upload CSV File')
        dialog.add_text_input(label='Give URL for CSV-file', name='url')
        response = dialog.run_dialog()

        http.download(response.url, overwrite=True)

        with open('orders.csv') as csvFile:
            csvReader = csv.reader(csvFile)
            table = list(csvReader)
            return table
        
            #table = tables.read_table_from_CSV('orders.csv', header=True)