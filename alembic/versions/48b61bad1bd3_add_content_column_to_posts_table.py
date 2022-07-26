"""add content column to posts table

Revision ID: 48b61bad1bd3
Revises: 9f16fa6086d0
Create Date: 2022-07-25 17:48:14.083102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48b61bad1bd3'
down_revision = '9f16fa6086d0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
