from sqlalchemy import select, func

from app.database import Base, engine, SessionLocal
from app.models.students import Students


DEFAULT_USERS = [
    ("JOHN", 80, 90, 95),
    ("ALEX", 90, 93, 87),
    ("TOM", 91, 89, 90),
    ("DONAL", 78, 87, 100),
    ("NICK", 34, 91, 76),
    ("SON", 10, 23, 82),
    ("JORDAN", 45, 64, 83),
    ("MICHAEL", 98, 88, 36),
    ("JAMAL", 86, 24, 16),
]

def init_db():
    Base.metadata.create_all(engine)
    
    with SessionLocal() as db:
        if db.scalar(select(func.count()).select_from(Students)) == 0:
            
            for name, inf, math, history in DEFAULT_USERS:
                db.add(Students(name = name, inf_score = inf, math_score = math, history_score = history))
        
        db.commit()
        