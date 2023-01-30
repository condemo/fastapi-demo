"""add foreign-key to posts table

Revision ID: a9cf8ddc469d
Revises: 51311db7b91d
Create Date: 2023-01-26 20:36:49.513432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9cf8ddc469d'
down_revision = '51311db7b91d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts', sa.Column('owner_id', sa.Integer(), nullable=False))

    op.create_foreign_key(
        'posts_users_fk', source_table='posts', referent_table='users',
        local_cols=['owner_id'], remote_cols=["id"], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users-fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
