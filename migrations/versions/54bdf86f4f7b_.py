"""empty message

Revision ID: 54bdf86f4f7b
Revises: 427c29b164b1
Create Date: 2023-05-08 04:37:26.536981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54bdf86f4f7b'
down_revision = '427c29b164b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dt_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
        batch_op.add_column(sa.Column('dt_updated', sa.DateTime(), nullable=True))
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
        batch_op.alter_column('text',
               existing_type=sa.TEXT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.alter_column('text',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.drop_column('dt_updated')
        batch_op.drop_column('dt_created')

    # ### end Alembic commands ###