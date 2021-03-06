"""empty message

Revision ID: 13d02d996199
Revises: ed5316755c16
Create Date: 2022-04-13 23:18:44.388648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13d02d996199'
down_revision = 'ed5316755c16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie_list', sa.Column('release_year', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie_list', 'release_year')
    # ### end Alembic commands ###
