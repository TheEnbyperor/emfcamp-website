"""Add unique constraint for village membership

Revision ID: 4a595f83788b
Revises: d756698d5d75
Create Date: 2022-05-19 19:22:00.190364

"""

# revision identifiers, used by Alembic.
revision = '4a595f83788b'
down_revision = 'd756698d5d75'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_village_member_user_id'), 'village_member', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_village_member_user_id'), 'village_member', type_='unique')
    # ### end Alembic commands ###