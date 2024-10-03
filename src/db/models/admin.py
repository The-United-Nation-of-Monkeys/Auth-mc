from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, Enum
import os, sys

sys.path.append(os.path.join(sys.path[0][:-13]))
from src.db.configuration import Base
from src.db.roles import Roles

    
class Table_Admins(Base):
    __tablename__ = "admins"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[Roles] = mapped_column(Enum(Roles), default=Roles.admin.value)
    username: Mapped[str]
    password: Mapped[bytes]