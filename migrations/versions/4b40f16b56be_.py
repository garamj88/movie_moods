"""empty message

Revision ID: 4b40f16b56be
Revises: 13d02d996199
Create Date: 2022-04-13 23:23:49.256076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b40f16b56be'
down_revision = '13d02d996199'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie_list', sa.Column('mood', sa.String(length=200), nullable=False))
    op.add_column('movie_list', sa.Column('director', sa.String(length=140), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie_list', 'director')
    op.drop_column('movie_list', 'mood')
    # ### end Alembic commands ###
