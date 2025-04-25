import pandas as pd

def prepare_data(filepath='./data/animal_health_incidents.csv'): # this part does not make sence ask why tf this works
    df = pd.read_csv(filepath)
    df['date_reported'] = pd.to_datetime(df['date_reported'], errors='coerce')
    df['year'] = df['date_reported'].dt.year

    df['disease'] = df['disease'].str.strip()
    df['species'] = df['species'].str.strip()

    return df
