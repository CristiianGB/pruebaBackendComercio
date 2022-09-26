"""empty message

Revision ID: 335453748940
Revises: eb8401f46c3d
Create Date: 2022-09-23 18:05:42.702858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '335453748940'
down_revision = 'eb8401f46c3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('favorite')
    op.add_column('cart', sa.Column('product_quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'product_quantity')
    op.create_table('favorite',
    sa.Column('list_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], name='favorite_product_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorite_user_id_fkey'),
    sa.PrimaryKeyConstraint('list_id', name='favorite_pkey')
    )
    op.drop_table('favorites')
    # ### end Alembic commands ###