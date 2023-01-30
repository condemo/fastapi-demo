"""add last few tables to post table

Revision ID: 27b191dd5dee
Revises: a9cf8ddc469d
Create Date: 2023-01-30 20:15:57.860218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27b191dd5dee'
down_revision = 'a9cf8ddc469d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
        sa.Column('published', sa.Boolean, nullable=False, server_default='TRUE'),)
    op.add_column('posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
