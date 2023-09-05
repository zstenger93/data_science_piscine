import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy


def load(path, tableName):
    try:
        data = pd.read_csv(path)
        data_types = {
            "event_time": sqlalchemy.DateTime(),
            "event_type":  sqlalchemy.types.String(length=255),
            "product_id": sqlalchemy.types.Integer(),
            "price": sqlalchemy.types.Float(),
            "user_id": sqlalchemy.types.BigInteger(),
            "user_session": sqlalchemy.types.Uuid()
        }

        engine = create_engine("postgresql://zstenger:msp@localhost:5432/piscineds")
        data.to_sql(tableName, engine, index=False, dtype=data_types)
        engine.dispose()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    load("/goinfre/zstenger/subject/customer/data_2022_oct.csv", "data_2022_oct")