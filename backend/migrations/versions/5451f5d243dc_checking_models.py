"""Checking models

Revision ID: 5451f5d243dc
Revises: eeb0a2ae530d
Create Date: 2025-02-10 18:44:23.843266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5451f5d243dc'
down_revision: Union[str, None] = 'eeb0a2ae530d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
