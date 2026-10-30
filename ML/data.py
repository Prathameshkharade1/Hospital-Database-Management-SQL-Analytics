
import mysql.connector
import pandas as pd

def load_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pratham@mysql",
        database="hospital"
    )

    try:
        query = """
        SELECT *
        FROM hospital.vw_ml_hospital_mortality
        """
        df = pd.read_sql(query, db)
        return df
    finally:
        db.close()
