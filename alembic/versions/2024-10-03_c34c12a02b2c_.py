"""empty message

Revision ID: c34c12a02b2c
Revises: 
Create Date: 2024-10-03 19:30:54.731295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import enum


class Roles(enum.Enum):
    admin = "admin"


# revision identifiers, used by Alembic.
revision: str = 'c34c12a02b2c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    roles_enum = sa.Enum(Roles, name='roles')

    # Создание таблицы admins
    op.create_table(
        'admins',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role', roles_enum, nullable=False, default=Roles.admin),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('password', sa.LargeBinary, nullable=False)
    )


def downgrade() -> None:
    pass
