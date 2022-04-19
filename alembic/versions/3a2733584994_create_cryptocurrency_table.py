"""create cryptocurrency table

Revision ID: 3a2733584994
Revises: 
Create Date: 2022-04-19 20:18:38.913767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a2733584994'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "cryptocurrency",
        sa.Column("id", sa.Integer(), primary_key=True),
        # TODO: more columns? :D
    )


def downgrade():
    op.drop_table("cryptocurrency")
