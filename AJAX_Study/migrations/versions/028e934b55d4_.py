"""empty message

Revision ID: 028e934b55d4
Revises: 
Create Date: 2019-04-16 13:39:22.609063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '028e934b55d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('province',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pname', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cname', sa.String(length=32), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pid'], ['province.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    op.drop_table('province')
    # ### end Alembic commands ###
