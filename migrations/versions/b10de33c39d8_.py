"""empty message

Revision ID: b10de33c39d8
Revises: a25c3f557d23
Create Date: 2021-08-24 17:20:27.507412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b10de33c39d8'
down_revision = 'a25c3f557d23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'todo', 'user', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    # ### end Alembic commands ###