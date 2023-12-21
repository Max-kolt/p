from .auth import auth_router
from .question import question_router
from .user import user_router
from .quiz import quiz_router

all_routers = [auth_router, question_router, user_router, quiz_router]

__all__ = ['all_routers', 'auth_router', 'question_router', 'user_router', 'quiz_router']
