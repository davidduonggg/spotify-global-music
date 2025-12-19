from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/db")

track_data = pd.read_csv("track_data_final.csv")
track_data.to_sql('track_data', engine, if_exists='replace')

