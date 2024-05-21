import pandas as pd
import random
import string
from components.constants import EXCEL_FILE

def create_excel(entity_count):
    data = []
    # Create some data as a DataFrame
    for i in range(entity_count):
        row = { 
            "Name": random_string(),
            "Age": random.randint(1, 100),
            "Gender": random.choice(["Male", "Female"]),
            "Option": random.randint(0,4)
        }
        data.append(row)
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file
    df.to_excel(EXCEL_FILE, index=False)

def random_string():
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for i in range(random.randint(3, 10)))