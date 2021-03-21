import pandas as pd
import json

def getKey(json):
    """In here we need to connect to the WS, pass parameters and get a new key"""
    key = "X86NOH6II01P7R24" # Tests
    return key

def getNumberOfRowsToShow(res, args):
    try:
        # pagination
        rows = args['records']              # Taking number of rows to show

        df = pd.DataFrame.from_dict(res.json())     # Convert to dataframe
        df = df.iloc[:int(rows)]                    # Create new dataframe with number of rows
        result = df.to_json(orient="index")         # Convert to JSON
        parsed = json.loads(result)                 
        result = parsed                             # Return number of rows requested
    except:
        result = res.json()

    return result