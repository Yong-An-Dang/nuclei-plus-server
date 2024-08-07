import base64
import logging

import yaml

from . import models, schemas, db
from .schemas import SyncFilter

logger = logging.getLogger(__name__)


def create_template(template: schemas.SyncTemplate):
    content = base64.b64decode(template.content).decode('utf-8')
    template_dict: dict = yaml.safe_load(content)

    tmpTemplate = models.Template(
        dir=template.dir, content=content, content_base64=template.content)
    info: dict = template_dict.get("info", None)
    if info:
        tmpTemplate.filter_id = info.get("id", "")
        tmpTemplate.filter_name = info.get("name", "")
        tmpTemplate.filter_author = info.get("author", "")
        tmpTemplate.filter_severity = info.get("severity", "")
        tmpTemplate.filter_tags = info.get("tags", "")

    db.add(tmpTemplate)
    db.commit()
    db.refresh(tmpTemplate)
    return tmpTemplate


def get_templates(template_filter: SyncFilter, skip: int = 0, limit: int = 10):
    logger.debug(template_filter)
    filters = []

    if template_filter.dir:
        filters.append(models.Template.dir.like(f"%{template_filter.dir}%"))
    if template_filter.id:
        filters.append(models.Template.filter_id == template_filter.id)
    if template_filter.name:
        filters.append(models.Template.filter_name.like(
            f"%{template_filter.name}%"))
    if template_filter.author:
        filters.append(models.Template.filter_author.like(
            f"%{template_filter.author}%"))
    if template_filter.severity:
        filters.append(models.Template.filter_severity.like(
            f"%{template_filter.severity}%"))
    if template_filter.tags:
        filters.append(models.Template.filter_tags.like(
            f"%{template_filter.tags}%"))

    return db.query(models.Template).filter(*filters).offset(skip).limit(limit).all()

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
