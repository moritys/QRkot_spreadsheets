"""Create abstract base

Revision ID: d6c1f7fc7755
Revises: b0b2a9124eeb
Create Date: 2023-09-18 17:25:54.923652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6c1f7fc7755'
down_revision = 'b0b2a9124eeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('charityproject', 'full_amount',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('donation', 'full_amount',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('donation', 'full_amount',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('charityproject', 'full_amount',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###