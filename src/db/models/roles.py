from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum

from src.db.configuration import Base
# from db.models import Users


class Roles(Base):
    __tablename__ = "roles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    role: Mapped[str] = mapped_column(unique=True)
    special: Mapped[bool] = mapped_column(default=False)
    
    user = relationship("Users",
        back_populates="role", uselist=False
    )
    
    
class BaseRoles(Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"
