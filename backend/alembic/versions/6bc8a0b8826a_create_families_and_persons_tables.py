"""create_families_and_persons_tables

Revision ID: 6bc8a0b8826a
Revises: 
Create Date: 2026-09-22 13:12:35.732120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bc8a0b8826a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create families table
    op.create_table(
        'families',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('composition_type', sa.String(50), nullable=False),
        sa.Column('district', sa.String(), nullable=False),
        sa.Column('taluk', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('ration_card_type', sa.String(50), nullable=False),
        sa.Column('total_household_income', sa.Numeric(12, 2), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index('idx_families_district_taluk', 'families', ['district', 'taluk'])

    # Create persons table
    op.create_table(
        'persons',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('family_id', sa.CHAR(36), sa.ForeignKey('families.id', ondelete='CASCADE'), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('age', sa.Integer(), nullable=False),
        sa.Column('gender', sa.String(50), nullable=False),
        sa.Column('education_level', sa.String(50), nullable=False),
        sa.Column('occupation', sa.String(50), nullable=False),
        sa.Column('occupation_detail', sa.String(), nullable=True),
        sa.Column('marital_status', sa.String(50), nullable=False),
        sa.Column('caste_category', sa.String(50), nullable=False),
        sa.Column('disability_status', sa.Boolean(), server_default=sa.text('false'), nullable=False),
        sa.Column('disability_type', sa.String(), nullable=True),
        sa.Column('special_flags', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index('idx_persons_family_id', 'persons', ['family_id'])


def downgrade() -> None:
    op.drop_index('idx_persons_family_id', table_name='persons')
    op.drop_table('persons')
    op.drop_index('idx_families_district_taluk', table_name='families')
    op.drop_table('families')

