"""add_scheme_guidance_fields

Revision ID: f1293a1b9c44
Revises: e7104b2a8d33
Create Date: 2026-09-23 08:05:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f1293a1b9c44'
down_revision: Union[str, Sequence[str], None] = 'e7104b2a8d33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('schemes', sa.Column('required_documents', sa.JSON(), server_default='[]', nullable=False))
    op.add_column('schemes', sa.Column('application_office', sa.String(255), server_default='வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்', nullable=False))
    op.add_column('schemes', sa.Column('application_mode', sa.String(50), server_default='both', nullable=False))
    op.add_column('schemes', sa.Column('online_application_url', sa.String(500), nullable=True))
    op.add_column('schemes', sa.Column('processing_time_estimate', sa.String(100), server_default='15 முதல் 30 நாட்கள்', nullable=False))


def downgrade() -> None:
    op.drop_column('schemes', 'processing_time_estimate')
    op.drop_column('schemes', 'online_application_url')
    op.drop_column('schemes', 'application_mode')
    op.drop_column('schemes', 'application_office')
    op.drop_column('schemes', 'required_documents')
