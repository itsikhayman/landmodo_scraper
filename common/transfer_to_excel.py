# common/transfer_to_excel

from datetime import datetime
import pandas as pd
import os
import pyinputplus as pyip

class TransferToExcel:
    def __init__(self):
        pass

    def save_to_excel(self, property_details):
        # Save all collected property details to an Excel file
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        df = pd.DataFrame(property_details)
        file_name = f"landmodo_report_{current_time}.xlsx"
        file_path = file_name  # This will create the file in the current directory (main)
        df.to_excel(file_path, index=False, sheet_name='Property Details')
        print(f"Property details have been saved to Excel file '{file_name}'")

        # Ask the user if they want to open the Excel file
        user_input = pyip.inputYesNo(prompt="Do you want to open the Excel file now? (y/n): ")
        if user_input == 'yes' or user_input == 'y':
            os.startfile(file_path)
