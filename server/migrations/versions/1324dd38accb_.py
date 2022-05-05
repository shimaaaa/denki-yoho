"""empty message

Revision ID: 1324dd38accb
Revises: 
Create Date: 2022-05-05 09:54:02.684873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1324dd38accb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('demand_forecast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area', sa.Enum('hokkaido', 'tohoku', 'tokyo', 'chubu', 'hokuriku', 'kansai', 'chugoku', 'shikoku', 'kyushu', 'okinawa', name='demand_forecast_area'), nullable=False),
    sa.Column('dt', sa.DateTime(), nullable=False),
    sa.Column('actual_result', sa.Integer(), nullable=False),
    sa.Column('forecast_demand', sa.Integer(), nullable=False),
    sa.Column('forecast_supply', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('area', 'dt')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('demand_forecast')
    # ### end Alembic commands ###