from app.extensions import (
    db,
    Mapped,
    mapped_column,
    String,
    BigInteger,
    Boolean,
    TimeStampModel,
    Optional,
    Text
)


class User(TimeStampModel):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    email: Mapped[str] = mapped_column(
        String(200), unique=True, nullable=False, index=True
    )
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False, index=True
    )
    is_admin: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    additional_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)