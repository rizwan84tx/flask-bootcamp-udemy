"""Created Models

Revision ID: ae983ea37a5d
Revises: 
Create Date: 2019-08-03 16:59:41.413415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae983ea37a5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('child',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cname', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('father',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.Text(), nullable=True),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['child.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('father')
    op.drop_table('child')
    # ### end Alembic commands ###
