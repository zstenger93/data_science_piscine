import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
import sqlalchemy

def table_exists(engine, table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if table_name in metadata.tables:
        print(f"Table {table_name} already exist")
    return table_name in metadata.tables


def load(path, tableName):
    try:
        engine = create_engine("postgresql://zstenger:msp@localhost:5432/piscineds")
        if not table_exists(engine, tableName):
            print(f"Table {tableName} doesn't exist, creating...")
            data = pd.read_csv(path)
            data = pd.read_csv(path)
            data_types = {
                "event_time": sqlalchemy.DateTime(),
                "event_type": sqlalchemy.types.String(length=255),
                "product_id": sqlalchemy.types.Integer(),
                "price": sqlalchemy.types.Float(),
                "user_id": sqlalchemy.types.BigInteger(),
                "user_session": sqlalchemy.types.UUID(as_uuid=True)  # Corrected the data type
            }
            data.to_sql(tableName, engine, index=False, dtype=data_types)
            print(f"Table {tableName} created")
        engine.dispose()
    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    load("/goinfre/zstenger/subject/customer/data_2022_oct.csv", "data_2022_oct")