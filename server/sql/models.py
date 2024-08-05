from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Template(Base):
    """
    # Filter
    dir: str  # Path
    id: str  # Template's ID
    name: str  # Template's Name
    author: str  # Template's Author
    severity: str  # Template's Severity
    tags: str  # Template's Tags
    """
    __tablename__ = "templates"
    id = Column(Integer, primary_key=True)
    dir = Column(String)
    content = Column(String)
    content_base64 = Column(String)
    # Filter
    filter_id = Column(String, default="")
    filter_name = Column(String, default="")
    filter_author = Column(String, default="")
    filter_severity = Column(String, default="")
    filter_tags = Column(String, default="")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
