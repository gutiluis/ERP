from decimal import Decimal

from app.extensions import (
    db,
    Mapped,
    mapped_column,
    BigInteger,
    String,
    Boolean,
    Numeric,
    TimeStampModel,
    Optional,
    Text
)


class Product(TimeStampModel):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    public_product_id: Mapped[str] = mapped_column(
        String(50), index=True, unique=True, nullable=False
    )

    product_name: Mapped[str] = mapped_column(
        String(200), unique=True, nullable=False
    )
    sku: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    brand: Mapped[str] = mapped_column(String(200), nullable=False)
    product_category: Mapped[str] = mapped_column(String(200), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    product_description: Mapped[str] = mapped_column(Text, nullable=False)
    # text cannot be indexed
    # If a column is unique=True or index=True, it must be String(n) in MySQL.
    # 3072 bytes = 768 characters in utf8mb4
    url: Mapped[str] = mapped_column(
        String(760), 
        unique=True, 
        nullable=True
    )
    url_tag: Mapped[str] = mapped_column(String(100), nullable=True)
    additional_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    children_variants = db.relationship(
        'ProductVariant',
        back_populates='parent',
        cascade='all, delete-orphan',
        lazy='select',
    )



class ProductVariant(TimeStampModel):
    __tablename__ = 'product_variants'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    product_fk_id: Mapped[int] = mapped_column(
        BigInteger, db.ForeignKey("products.id"), nullable=False, index=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    color: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    size: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    has_stock: Mapped[bool] = mapped_column(default=False, nullable=False)
    inventory_stock: Mapped[int] = mapped_column(BigInteger, nullable=False)

    parent = db.relationship('Product', back_populates='children_variants')