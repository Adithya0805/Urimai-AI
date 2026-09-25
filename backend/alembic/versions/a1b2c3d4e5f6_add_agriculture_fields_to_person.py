"""add_agriculture_fields_to_person

Revision ID: a1b2c3d4e5f6
Revises: f1293a1b9c44
Create Date: 2026-09-23 08:15:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = 'f1293a1b9c44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('persons', sa.Column('land_holding_acres', sa.Numeric(6, 2), server_default='0.0', nullable=True))
    op.add_column('persons', sa.Column('crop_type', sa.String(100), nullable=True))


def downgrade() -> None:
    op.drop_column('persons', 'crop_type')
    op.drop_column('persons', 'land_holding_acres')
