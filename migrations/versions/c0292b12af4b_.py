"""empty message

Revision ID: c0292b12af4b
Revises: 4b40f16b56be
Create Date: 2022-04-14 13:13:21.235847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0292b12af4b'
down_revision = '4b40f16b56be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie_list', sa.Column('new', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie_list', 'new')
    # ### end Alembic commands ###
