import os
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


def load(path, tableName, overall_progress_bar):
    try:
        engine = create_engine("postgresql://zstenger:msp@localhost:5432/piscineds")
        if not table_exists(engine, tableName):
            print(f"\033[1;33mTable {tableName} doesn't exist, creating...\033[0;39m")
            data = pd.read_csv(path)
            data_types = {
                "event_time": sqlalchemy.DateTime(),
                "event_type": sqlalchemy.types.String(length=255),
                "product_id": sqlalchemy.types.Integer(),
                "price": sqlalchemy.types.Float(),
                "user_id": sqlalchemy.types.BigInteger(),
                "user_session": sqlalchemy.types.UUID(as_uuid=True)
            }

            total_rows = len(data)
            chunk_size = total_rows // 100
            chunk_count = total_rows // chunk_size
            remainder = total_rows % chunk_size

            with tqdm(total=total_rows, position=1, leave=True, bar_format="{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]") as pbar:
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
        overall_progress_bar.update(1)
    except Exception as error:
        print(f"An error occurred: {error}")


def create_tables(folder_path):
    table_creation_count = 0
    total_tables = len([filename for filename in os.listdir(folder_path) if filename.endswith(".csv")])

    with tqdm(total=total_tables, position=0, leave=True, bar_format="\033[1;31mOverall progress:\033[0;39m {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]") as overall_pbar:
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                table_name = os.path.splitext(filename)[0]
                file_path = os.path.join(folder_path, filename)
                print("Getting next table for injection ...")
                load(file_path, table_name, overall_pbar)
                table_creation_count += 1


if __name__ == "__main__":
    folder_path = "/goinfre/zstenger/subject/customer/"
    create_tables(folder_path)
