from sqlalchemy import Column, MetaData, String, Table, DateTime, Text

metadata = MetaData()
cryptocurrency = Table(
    "cryptocurrency",
    metadata,
    Column("id", String, primary_key=True),
    Column("symbol", String(length=10), nullable=False),
    Column("name", String, nullable=False),
    Column("description", Text, nullable=True),
    Column("created_at", DateTime),
)
