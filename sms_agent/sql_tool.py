import random

from fun_topic import topics
from smolagents import tool, Tool
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    insert,
    text,
)


def insert_rows_into_table(rows, table, engine):
    for row in rows:
        stmt = insert(table).values(**row)
        with engine.begin() as connection:
            connection.execute(stmt)


def spin_up_server():
    engine = create_engine("sqlite:///:memory:")
    metadata_obj = MetaData()
    table_name = "topics"
    receipts = Table(
        table_name,
        metadata_obj,
        Column("topic_id", Integer, primary_key=True),
        Column("topic", String(80), primary_key=True),
    )
    metadata_obj.create_all(engine)
    rows = []
    for i, topic in enumerate(topics):
        i += 1
        rows.append({"topic_id": i, "topic": topic})
    insert_rows_into_table(rows, receipts, engine)

    return engine


class SQLEngine(Tool):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.engine = spin_up_server()
    name = "sql_engine"
    description = """
    Allows you to perform SQL queries on the Topic table which is full of fun topics.
    Returns a string representation of the result.
    The table is named 'topics'. Its description is as follows:
        Columns:
        - topic_id: INTEGER
        - topic: VARCHAR(80)

        """
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This needs to be well-formed SQL."
        }
    }
    output_type = "string"

    def forward(self, query) -> str:
        output = ""
        try:
            with self.engine.connect() as connection:
                rows = connection.execute(text(query))
                for row in rows:
                    output += "\n" + str(row)
        except Exception as e:
            # print(f"There was an exception! {e}")
            pass
        return output


@tool
def get_random_topic_id() -> int:
    """
    Gets a random, valid topic_id to use in querying the database!
        Columns:
        - topic_id: INTEGER
        - topic: VARCHAR(80)

    returns:
        A valid topic_id to use in the sql_database
    """
    return random.randint(0, len(topics))
