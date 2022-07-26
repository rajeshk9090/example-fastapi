"""add users table

Revision ID: 4089377bceef
Revises: 48b61bad1bd3
Create Date: 2022-07-25 18:01:09.334274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4089377bceef'
down_revision = '48b61bad1bd3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
