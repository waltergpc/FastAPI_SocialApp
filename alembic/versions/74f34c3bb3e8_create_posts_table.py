"""create posts table

Revision ID: 74f34c3bb3e8
Revises: 
Create Date: 2022-01-13 23:31:55.660342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "74f34c3bb3e8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
