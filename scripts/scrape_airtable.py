import os
from tkinter import BASELINE
from pyairtable import Table
import pandas as pd
import time

API_KEY = os.environ["AIRTABLE_API_KEY"]
BASE_ID = "apptUkOtU3W8HxbQQ"
TABLE_NAME = "Organization List"

table = Table(API_KEY, BASE_ID, TABLE_NAME)
all_data = table.all()

df = pd.json_normalize(all_data, sep='_')

df_passed = df[df['fields_Urban Tech Screening'] == "Passed"]
df_passed = df_passed.reset_index()

current_time = round(time.time())
file_name = "../data/airtable_data_" + str(current_time) + ".csv"

df_passed.to_csv(file_name)
