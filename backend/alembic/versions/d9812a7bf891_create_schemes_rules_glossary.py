"""create_schemes_rules_and_glossary_tables

Revision ID: d9812a7bf891
Revises: 6bc8a0b8826a
Create Date: 2026-09-23 07:51:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd9812a7bf891'
down_revision: Union[str, Sequence[str], None] = '6bc8a0b8826a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Create schemes table
    op.create_table(
        'schemes',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('scheme_code', sa.String(100), unique=True, nullable=False),
        sa.Column('name_english', sa.String(255), nullable=False),
        sa.Column('name_tamil', sa.String(255), nullable=False),
        sa.Column('name_transliteration', sa.String(255), nullable=False),
        sa.Column('department', sa.String(255), nullable=False),
        sa.Column('category', sa.String(100), nullable=False),
        sa.Column('description_english', sa.Text(), nullable=False),
        sa.Column('description_tamil', sa.Text(), nullable=False),
        sa.Column('benefit_amount', sa.String(255), nullable=False),
        sa.Column('source_url', sa.String(500), nullable=False),
        sa.Column('last_verified_date', sa.Date(), nullable=False),
        sa.Column('is_active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index('idx_schemes_code', 'schemes', ['scheme_code'])
    op.create_index('idx_schemes_dept_cat', 'schemes', ['department', 'category'])

    # 2. Create eligibility_rules table
    op.create_table(
        'eligibility_rules',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('scheme_id', sa.CHAR(36), sa.ForeignKey('schemes.id', ondelete='CASCADE'), nullable=False),
        sa.Column('field_name', sa.String(100), nullable=False),
        sa.Column('operator', sa.String(50), nullable=False),
        sa.Column('value', sa.String(255), nullable=False),
        sa.Column('applies_to', sa.String(50), nullable=False),
    )
    op.create_index('idx_eligibility_rules_scheme_id', 'eligibility_rules', ['scheme_id'])

    # 3. Create scheme_term_glossary table
    op.create_table(
        'scheme_term_glossary',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('tamil_term', sa.String(255), nullable=False),
        sa.Column('english_equivalent', sa.String(255), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index('idx_glossary_tamil_term', 'scheme_term_glossary', ['tamil_term'])


def downgrade() -> None:
    op.drop_index('idx_glossary_tamil_term', table_name='scheme_term_glossary')
    op.drop_table('scheme_term_glossary')

    op.drop_index('idx_eligibility_rules_scheme_id', table_name='eligibility_rules')
    op.drop_table('eligibility_rules')

    op.drop_index('idx_schemes_dept_cat', table_name='schemes')
    op.drop_index('idx_schemes_code', table_name='schemes')
    op.drop_table('schemes')
