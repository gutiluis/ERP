from __future__ import annotations # fix declarative mapping relationship with annotation from another file
from typing import TYPE_CHECKING # fix declarative mapping relationship with annotation from another file

from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum as PyEnum

from app.extensions import (
    db,
    Mapped,
    mapped_column,
    String,
    TimeStampModel,
    BigInteger,
    Numeric,
    DateTime,
    Optional,
    Text
)

if TYPE_CHECKING: # fix import relationship from another file
    from .customers import Customer
    from .payments import Payment




class InvoiceStatus(PyEnum):
    pending = 'pending'
    paid = 'paid'
    overdue = 'overdue'
    cancelled = 'cancelled'


class Invoice(TimeStampModel):
    __tablename__ = "invoices"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    public_invoice_id: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )
    # from customers table
    customer_fk_id: Mapped[int] = mapped_column(
        BigInteger, db.ForeignKey('customers.id'), nullable=False, index=True
    )

    customer: Mapped["Customer"] = db.relationship(
        "Customer", back_populates="invoices"
    )

    status: Mapped[InvoiceStatus] = mapped_column(
        String(20),
        nullable=False,
        default=InvoiceStatus.pending.value,
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False, default=Decimal('0.00'))

    # tax amount is derived not authoritative
    tax_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False, default=Decimal('0.00'))
    
    shipping_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False, default=Decimal('0.00'))
    
    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False, default=Decimal('0.00'))
    
    # after partial payments
    outstanding_balance: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), nullable=False, default=Decimal('0.00'))

    invoice_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    
    invoice_due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    # an invoice is not always fully paid.
    date_fully_paid: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True
    )

    items: Mapped[list["InvoiceItem"]] = db.relationship(
        "InvoiceItem", back_populates="invoice", cascade="all, delete-orphan"
    ) # cascade to delete if invoice is deleted everything
    
    
    payments: Mapped[list["Payment"]] = db.relationship(
        "Payment", back_populates="invoice",
        lazy='selectin',
        cascade='all, delete-orphan' # delete an invoice to delete all payments
    )
    
    # see invoicetaxes relationship annotated mapping
    taxes: Mapped[list["InvoiceTax"]] = db.relationship(
        "InvoiceTax", back_populates="invoice", cascade="all, delete-orphan", lazy="selectin"
    )

    additional_notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)



class InvoiceItem(TimeStampModel):
    __tablename__ = "invoice_items"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    invoice_fk_id: Mapped[int] = mapped_column(
        BigInteger, db.ForeignKey("invoices.id"), nullable=False, index=True
    )
    product_fk_id: Mapped[int] = mapped_column(
        BigInteger, db.ForeignKey("products.id"), nullable=False, index=True
    )

    quantity: Mapped[int] = mapped_column(BigInteger, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    line_total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    invoice: Mapped["Invoice"] = db.relationship(
        "Invoice", back_populates="items"
    )


class InvoiceTax(TimeStampModel):
    __tablename__ = 'invoice_taxes'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    invoice_fk_id: Mapped[int] = mapped_column(
        BigInteger, db.ForeignKey("invoices.id"), nullable=False, index=True
    )
    # Percentage, e.g. 8.5 for 8.5%, 13 for 13%. Use (rate_percent / 100) for calculations.
    tax_rate_percent: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    tax_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    # by adding the annotation we know whether its one to one or one to many
    # by adding the annotation. we know wheter it's optional or not
    # one invoice belongs to one customer
    # use list[class_model] only on the many side of a relationship
    invoice: Mapped["Invoice"] = db.relationship(
        "Invoice", back_populates="taxes"
    )