"""add foreign key to post table

Revision ID: 03e6dddf5b73
Revises: d4200f756a62
Create Date: 2022-01-13 23:59:24.889994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "03e6dddf5b73"
down_revision = "d4200f756a62"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
