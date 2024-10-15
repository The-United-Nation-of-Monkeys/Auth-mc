from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum

from db.configuration import Base
# from db.models import Table_Users


class Table_Roles(Base):
    __tablename__ = "roles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(unique=True)
    special: Mapped[bool] = mapped_column(default=False)
    
    user = relationship("Table_Users",
        back_populates="role", uselist=False
    )
    
    
    #добавить параметр важные роли или нет, надо подтверждение или нет 
    
class Base_Roles(Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"
