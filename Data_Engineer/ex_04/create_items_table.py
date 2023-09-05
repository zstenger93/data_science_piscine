import sqlalchemy
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, MetaData


def table_exists(engine, table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if table_name in metadata.tables:
        print(f"\033[1;32mTable {table_name} already exists\033[0;39m")
    return table_name in metadata.tables


def load(path, tableName):
    try:
        engine = create_engine("postgresql://zstenger:msp@localhost:5432/piscineds")
        if not table_exists(engine, tableName):
            print(f"\033[1;33mTable {tableName} doesn't exist, creating...\033[0;39m")
            data = pd.read_csv(path)
            data_types = {
                "pruduct_id": sqlalchemy.types.Integer(),
                "category_id": sqlalchemy.types.BigInteger(),
                "category_code": sqlalchemy.types.String(length=255),
                "brand": sqlalchemy.types.String(length=255)
            }
            total_rows = len(data)
            chunk_size = total_rows // 100
            chunk_count = total_rows // chunk_size
            remainder = total_rows % chunk_size
            with tqdm(total=total_rows, position=0, leave=True) as pbar:
                for i in range(chunk_count):
                    chunk = data.iloc[i * chunk_size:(i + 1) * chunk_size]
                    chunk.to_sql(tableName, engine, index=False, dtype=data_types, if_exists="append")
                    pbar.update(chunk_size)
                if remainder > 0:
                    remainder_chunk = data.iloc[chunk_count * chunk_size:]
                    remainder_chunk.to_sql(tableName, engine, index=False, dtype=data_types, if_exists="append")
                    pbar.update(remainder)
            tqdm.write(f"\033[1;32mTable {tableName} created\033[0;39m")
        engine.dispose()
    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    print("Getting next table for injection ...")
    load("/goinfre/zstenger/subject/item/item.csv", "items")
