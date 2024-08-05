import base64
import yaml

from . import models, schemas, db


def create_template(template: schemas.SyncTemplate):
    content = base64.b64decode(template.content).decode('utf-8')
    template_dict: dict = yaml.safe_load(content)

    tmpTemplate = models.Template(dir=template.dir, content=content, content_base64=template.content)
    tmpTemplate.filter_id = template_dict.get("id", "")
    tmpTemplate.filter_name = template_dict.get("name", "")
    tmpTemplate.filter_author = template_dict.get("author", "")
    tmpTemplate.filter_severity = template_dict.get("severity", "")
    tmpTemplate.filter_tags = template_dict.get("tags", "")

    db.add(tmpTemplate)
    db.commit()
    db.refresh(tmpTemplate)
    return tmpTemplate

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
