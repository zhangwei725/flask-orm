"""empty message

Revision ID: cdb6cee29ccf
Revises: 023f514c810d
Create Date: 2018-12-04 16:38:27.364071

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cdb6cee29ccf'
down_revision = '023f514c810d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('t_user', 'username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    op.create_index(op.f('ix_t_user_username'), 't_user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_t_user_username'), table_name='t_user')
    op.alter_column('t_user', 'username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###
