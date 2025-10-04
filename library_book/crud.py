from sqlalchemy.orm import Session
from library_book import models, schemas


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.LBAuthor(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LBAuthor).offset(skip).limit(limit).all()


def get_author(db: Session, author_id: int):
    return db.query(models.LBAuthor).filter(models.LBAuthor.id == author_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.LBBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        packaging_type=book.packaging_type,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LBBook).offset(skip).limit(limit).all()


def get_books_by_author(db: Session, author_id: int):
    return db.query(models.LBBook).filter(models.LBBook.author_id == author_id).all()
