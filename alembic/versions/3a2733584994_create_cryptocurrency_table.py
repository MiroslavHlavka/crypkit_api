"""create cryptocurrency table

Revision ID: 3a2733584994
Revises: 
Create Date: 2022-04-19 20:18:38.913767

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3a2733584994'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "cryptocurrency",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("symbol", sa.String(length=10), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime()),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_cryptocurrency'))
    )


def downgrade():
    op.drop_table("cryptocurrency")
