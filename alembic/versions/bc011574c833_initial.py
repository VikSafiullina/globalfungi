"""initial

Revision ID: bc011574c833
Revises: 
Create Date: 2023-11-12 17:23:36.436602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc011574c833'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with open('alembic/initial.sql') as file:
        op.execute(file.read())


def downgrade() -> None:
    pass
