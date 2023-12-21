from pydantic import BaseModel
from typing import Optional, TypeVar, Annotated
from datetime import datetime
from fastapi import Depends
from repository.auth_repo import verify_token

T = TypeVar("T")


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


# Authentication

class RegisterSchema(BaseModel):
    username: str
    email: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


user_dep = Annotated[dict, Depends(verify_token)]


# User

class UserSession(BaseModel):
    last_session_entry: datetime
    last_session_exit: datetime | None


class UserQuizzes(BaseModel):
    quiz_id: int
    quiz_name: str
    quiz_picture: bytes | None


class UserAnswers(BaseModel):
    question: int
    is_successful: bool
    time: datetime


class UserQuizzesResults(BaseModel):
    quiz: UserQuizzes
    result: int
    time: datetime


class UserExperience(BaseModel):
    user_answers: tuple[UserAnswers]
    user_quizzes_results: tuple[UserQuizzesResults]


class UserSchema(BaseModel):
    username: str
    avatar: bytes
    email: str
    session: UserSession
    likes: tuple[UserQuizzes]
    user_experience: UserExperience


# Questions

class QuestionAnswers(BaseModel):
    id: int
    text: str


class QuestionSchema(BaseModel):
    id: int
    text: str
    theme: str
    answers: tuple[QuestionAnswers]
    show_answers: bool


# Quizzes

class QuizViewSchema(BaseModel):
    id: int
    name: str
    picture: bytes
    description: str | None
    theme: str
    questions_count: int


class QuizProcessSchema(BaseModel):
    id: int
    name: str
    completed_questions: list[QuestionSchema]
    right_answers: int

