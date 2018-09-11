"""changes made success

Revision ID: 2b8dba5b54ba
Revises: 262f0a4dd50b
Create Date: 2018-09-11 15:48:46.908664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b8dba5b54ba'
down_revision = '262f0a4dd50b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment_name', sa.String(length=255), nullable=True))
    op.drop_column('comment', 'comment_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment_id', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('comment', 'comment_name')
    # ### end Alembic commands ###
