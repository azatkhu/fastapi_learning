from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Students(Base):
    
    __tablename__ = "Students"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column()
    inf_score: Mapped[int] = mapped_column(default = 0)
    math_score: Mapped[int] = mapped_column(default = 0)
    history_score: Mapped[int] = mapped_column(default = 0)
    