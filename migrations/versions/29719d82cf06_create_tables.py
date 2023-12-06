"""create tables

Revision ID: 29719d82cf06
Revises: 
Create Date: 2023-12-06 15:30:48.027370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '29719d82cf06'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('additional_health_statistics', 'year',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=4),
               existing_nullable=False)
    op.alter_column('additional_health_statistics', 'male',
               existing_type=mysql.FLOAT(),
               type_=sa.String(length=4),
               existing_nullable=False)
    op.alter_column('additional_health_statistics', 'female',
               existing_type=mysql.FLOAT(),
               type_=sa.String(length=4),
               existing_nullable=False)
    op.alter_column('health_statistics', 'year',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=4),
               existing_nullable=False)
    op.alter_column('health_statistics', 'male',
               existing_type=mysql.FLOAT(),
               type_=sa.String(length=4),
               existing_nullable=False)
    op.alter_column('health_statistics', 'female',
               existing_type=mysql.FLOAT(),
               type_=sa.String(length=4),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'all_women',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'non_hispanic_white',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'non_hispanic_black',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'hispanic',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'asian_and_pacific_islander',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'american_indian_alaska_native',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'other',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.create_foreign_key(None, 'location_health_statistics', 'health_statistics', ['all_women'], ['id'])
    op.drop_column('location_health_statistics', 'location')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location_health_statistics', sa.Column('location', mysql.VARCHAR(length=255), nullable=False))
    op.drop_constraint(None, 'location_health_statistics', type_='foreignkey')
    op.alter_column('location_health_statistics', 'other',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'american_indian_alaska_native',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'asian_and_pacific_islander',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'hispanic',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'non_hispanic_black',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'non_hispanic_white',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('location_health_statistics', 'all_women',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('health_statistics', 'female',
               existing_type=sa.String(length=4),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('health_statistics', 'male',
               existing_type=sa.String(length=4),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('health_statistics', 'year',
               existing_type=sa.String(length=4),
               type_=mysql.INTEGER(),
               existing_nullable=False)
    op.alter_column('additional_health_statistics', 'female',
               existing_type=sa.String(length=4),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('additional_health_statistics', 'male',
               existing_type=sa.String(length=4),
               type_=mysql.FLOAT(),
               existing_nullable=False)
    op.alter_column('additional_health_statistics', 'year',
               existing_type=sa.String(length=4),
               type_=mysql.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###