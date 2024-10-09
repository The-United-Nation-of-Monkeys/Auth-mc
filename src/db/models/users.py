from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import text, ForeignKey
import os, sys, datetime

sys.path.append(os.path.join(sys.path[0][:-9]))
from db.configuration import Base

class Table_Users(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]
    role_id: Mapped[str] = mapped_column(ForeignKey("roles.id"))
    role = relationship("roles",
        back_populates="id", uselist=False
    )
    date_register: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
