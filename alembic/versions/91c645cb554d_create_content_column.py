"""create content column

Revision ID: 91c645cb554d
Revises: 74f34c3bb3e8
Create Date: 2022-01-13 23:44:22.093941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "91c645cb554d"
down_revision = "74f34c3bb3e8"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
