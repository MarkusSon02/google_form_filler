import pandas as pd
import random
import string
from components.constants import EXCEL_FILE
from components.name_generator import Name_Generator

def create_excel(entity_count):
    data = []
    # Generates a list of random names
    name_generator = Name_Generator()
    name_list = name_generator.generate()
    # Create some data as a DataFrame
    for i in range(entity_count):
        row = { 
            "Name": name_list[i],
            "Age": random.randint(1, 100),
            "Gender": random.choice(["Male", "Female"]),
            "Option": random.randint(0,4)
        }
        data.append(row)
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file
    df.to_excel(EXCEL_FILE, index=False)
