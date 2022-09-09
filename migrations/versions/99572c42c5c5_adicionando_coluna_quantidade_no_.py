"""Adicionando coluna quantidade no purchase_orders_items

Revision ID: 99572c42c5c5
Revises: 1ed64b239569
Create Date: 2022-09-09 17:03:14.266242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99572c42c5c5'
down_revision = '1ed64b239569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('purchase_orders_items', sa.Column('quantity', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('purchase_orders_items', 'quantity')
    # ### end Alembic commands ###
