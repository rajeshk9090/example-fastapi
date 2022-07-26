"""add foreign-key to posts table

Revision ID: 509a414c63e0
Revises: 4089377bceef
Create Date: 2022-07-25 18:29:07.550037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '509a414c63e0'
down_revision = '4089377bceef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
