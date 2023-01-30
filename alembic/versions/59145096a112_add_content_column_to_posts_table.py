"""add content column to posts table

Revision ID: 59145096a112
Revises: c7f762cfc74f
Create Date: 2023-01-24 21:13:34.657504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59145096a112'
down_revision = 'c7f762cfc74f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
