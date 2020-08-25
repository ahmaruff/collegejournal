"""empty message

Revision ID: b1a207a0981e
Revises: 06a5d7db67d2
Create Date: 2020-08-22 22:54:12.694288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1a207a0981e'
down_revision = '06a5d7db67d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'confirmed')
    # ### end Alembic commands ###