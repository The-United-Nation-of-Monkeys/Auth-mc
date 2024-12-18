from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import os, sys, datetime, uuid

sys.path.append(os.path.join(sys.path[0][:-9]))
from src.db.configuration import Base
# from db.models import Roles

class Users(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]
    name: Mapped[str] 
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    date_register: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    active: Mapped[bool] = mapped_column(default=False)
    banned: Mapped[bool] = mapped_column(default=False)
    
    role = relationship("Roles",
        back_populates="user", uselist=False
    )
