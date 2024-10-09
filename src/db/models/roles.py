from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.configuration import Base


class Table_Roles(Base):
    __tablename__ = "roles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(unique=True)
    user = relationship("users",
        back_populates="id", uselist=False
    )
    