"""last columns

Revision ID: 26e55b05b409
Revises: 03e6dddf5b73
Create Date: 2022-01-14 13:28:07.695523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "26e55b05b409"
down_revision = "03e6dddf5b73"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
