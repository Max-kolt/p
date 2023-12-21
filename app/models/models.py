# from sqlalchemy import Table
# import asyncio
#
#
# User = Table
# UserSession = Table
# UserAnswer = Table
# UserQuizzesResult = Table
# QuizzesUsersLike = Table
# Quizz = Table
# Theme = Table
# QuizQuestion = Table
# Question = Table
# Answer = Table
#
#
#
#
# async def load_models(conn, metadata):
#     global User
#     global UserSession
#     global UserAnswer
#     global UserQuizzesResult
#     global QuizzesUsersLike
#     global Quizz
#     global Theme
#     global QuizQuestion
#     global Question
#     global Answer
#
#     User: Table = await conn.run_sync(lambda sync_conn: Table('users', metadata, autoload_with=sync_conn))
#     UserSession = await conn.run_sync(
#         lambda sync_conn: Table('user_sessions', metadata, autoload_with=sync_conn))
#     UserAnswer = await conn.run_sync(
#         lambda sync_conn: Table('user_answers', metadata, autoload_with=sync_conn))
#     UserQuizzesResult = await conn.run_sync(
#         lambda sync_conn: Table('user_quizzes_results', metadata, autoload_with=sync_conn))
#     QuizzesUsersLike = await conn.run_sync(
#         lambda sync_conn: Table('quizzes_users_likes', metadata, autoload_with=sync_conn))
#     Quizz = await conn.run_sync(lambda sync_conn: Table('quizzes', metadata, autoload_with=sync_conn))
#     Theme = await conn.run_sync(lambda sync_conn: Table('themes', metadata, autoload_with=sync_conn))
#     QuizQuestion = await conn.run_sync(
#         lambda sync_conn: Table('quiz_questions', metadata, autoload_with=sync_conn))
#     Question = await conn.run_sync(lambda sync_conn: Table('questions', metadata, autoload_with=sync_conn))
#     Answer = await conn.run_sync(lambda sync_conn: Table('answers', metadata, autoload_with=sync_conn))
#
