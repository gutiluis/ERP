from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, BigInteger, Numeric, Text, Boolean, DateTime
from decimal import Decimal
from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

class TimeStampModel(db.Model):
    __abstract__ = True
    created: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), 
        onupdate=lambda: datetime.now(timezone.utc)
    )