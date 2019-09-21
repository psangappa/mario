"""first migrate

Revision ID: 66407fbaa6a9
Revises: 
Create Date: 2019-09-21 13:03:49.282659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66407fbaa6a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('n', sa.Integer(), nullable=True),
    sa.Column('grid', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('remote_address', sa.String(length=30), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_data')
    # ### end Alembic commands ###