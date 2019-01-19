"""Add proposal URLs

Revision ID: 9483c0756933
Revises: 5c2416202824
Create Date: 2018-09-09 20:01:54.689906

"""

# revision identifiers, used by Alembic.
revision = '9483c0756933'
down_revision = '5c2416202824'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposal', sa.Column('c3voc_url', sa.String(), nullable=True))
    op.add_column('proposal', sa.Column('thumbnail_url', sa.String(), nullable=True))
    op.add_column('proposal', sa.Column('youtube_url', sa.String(), nullable=True))
    op.add_column('proposal_version', sa.Column('c3voc_url', sa.String(), autoincrement=False, nullable=True))
    op.add_column('proposal_version', sa.Column('thumbnail_url', sa.String(), autoincrement=False, nullable=True))
    op.add_column('proposal_version', sa.Column('youtube_url', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposal_version', 'youtube_url')
    op.drop_column('proposal_version', 'thumbnail_url')
    op.drop_column('proposal_version', 'c3voc_url')
    op.drop_column('proposal', 'youtube_url')
    op.drop_column('proposal', 'thumbnail_url')
    op.drop_column('proposal', 'c3voc_url')
    # ### end Alembic commands ###