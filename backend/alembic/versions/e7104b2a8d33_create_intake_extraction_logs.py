"""create_intake_extraction_logs_table

Revision ID: e7104b2a8d33
Revises: d9812a7bf891
Create Date: 2026-09-23 08:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e7104b2a8d33'
down_revision: Union[str, Sequence[str], None] = 'd9812a7bf891'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'intake_extraction_logs',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('session_id', sa.String(100), nullable=False),
        sa.Column('raw_tamil_input', sa.Text(), nullable=False),
        sa.Column('target_field', sa.String(100), nullable=False),
        sa.Column('extracted_value', sa.Text(), nullable=False),
        sa.Column('confirmed_value', sa.Text(), nullable=True),
        sa.Column('is_valid', sa.Boolean(), server_default=sa.text('true'), nullable=False),
        sa.Column('error_message', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index('idx_intake_logs_session_id', 'intake_extraction_logs', ['session_id'])
    op.create_index('idx_intake_logs_field', 'intake_extraction_logs', ['target_field'])


def downgrade() -> None:
    op.drop_index('idx_intake_logs_field', table_name='intake_extraction_logs')
    op.drop_index('idx_intake_logs_session_id', table_name='intake_extraction_logs')
    op.drop_table('intake_extraction_logs')
