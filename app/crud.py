from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User, Project, Course
from app.schemas import UserCreate, UserUpdate, ProjectCreate, ProjectUpdate, CourseCreate, CourseUpdate

# User CRUD
def get_user(db: Session, user_id: int):
    return db.get(User, user_id)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(User).offset(skip).limit(limit)).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.get(User, user_id)
    if db_user:
        for field, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.get(User, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Project CRUD
def get_project(db: Session, project_id: int):
    return db.get(Project, project_id)

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(Project).offset(skip).limit(limit)).all()

def create_project(db: Session, project: ProjectCreate):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: int, project: ProjectUpdate):
    db_project = db.get(Project, project_id)
    if db_project:
        for field, value in project.model_dump(exclude_unset=True).items():
            setattr(db_project, field, value)
        db.commit()
        db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.get(Project, project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project

# Course CRUD
def get_course(db: Session, course_id: int):
    return db.get(Course, course_id)

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(Course).offset(skip).limit(limit)).all()

def create_course(db: Session, course: CourseCreate):
    db_course = Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: CourseUpdate):
    db_course = db.get(Course, course_id)
    if db_course:
        for field, value in course.model_dump(exclude_unset=True).items():
            setattr(db_course, field, value)
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.get(Course, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course