from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text
import os, sys, datetime

sys.path.append(os.path.join(sys.path[0][:-13]))
from src.db.configuration import Base


class Table_Cats(Base):
    __tablename__ = "cats"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[int]
    color: Mapped[str]
    description: Mapped[str]
    breed: Mapped[str] = mapped_column(default=None, nullable=True)
    date_register: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    data_update: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )