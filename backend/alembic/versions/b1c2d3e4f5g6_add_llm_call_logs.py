"""Add llm_call_logs table

Revision ID: b1c2d3e4f5g6
Revises: a1b2c3d4e5f6
Create Date: 2026-09-23

"""
from alembic import op
import sqlalchemy as sa

revision = 'b1c2d3e4f5g6'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'llm_call_logs',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('call_type', sa.String(50), nullable=False),
        sa.Column('session_id', sa.String(100), nullable=True),
        sa.Column('person_id', sa.String(36), nullable=True),
        sa.Column('scheme_code', sa.String(100), nullable=True),
        sa.Column('prompt_text', sa.Text, nullable=False),
        sa.Column('retrieved_context', sa.Text, nullable=True),
        sa.Column('retrieval_score', sa.Float, nullable=True),
        sa.Column('used_rag', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('llm_output', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True),
                  server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_llm_call_logs_call_type', 'llm_call_logs', ['call_type'])
    op.create_index('ix_llm_call_logs_session_id', 'llm_call_logs', ['session_id'])
    op.create_index('ix_llm_call_logs_person_id', 'llm_call_logs', ['person_id'])
    op.create_index('ix_llm_call_logs_scheme_code', 'llm_call_logs', ['scheme_code'])


def downgrade() -> None:
    op.drop_table('llm_call_logs')
