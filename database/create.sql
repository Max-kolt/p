drop table if exists quiz_questions;
drop table if exists user_answers;
drop table if exists user_quizzes_results;
drop table if exists quizzes_users_likes;
drop table if exists answers;
drop table if exists questions;
drop table if exists quizzes;
drop table if exists user_sessions;
drop table if exists themes;
drop table if exists users;


create table users(
	username varchar(50) primary key,
	email varchar(255) not null,
	avatar bytea,
	password varchar(100) not null,
	created_at timestamp not null default (now())
);

create table themes(
	name varchar(50) primary key,
	description varchar(255)
);

create table user_sessions(
	id int GENERATED ALWAYS AS IDENTITY,
	user_pk varchar(50) references users(username),
	time_entry timestamp not null,
	time_exit time not null,
	primary key(id, user_pk)
);

create table quizzes(
	id smallint primary key GENERATED ALWAYS AS IDENTITY,
	name varchar(50) not null,
	picture bytea,
	description varchar(255),
	theme varchar(50) references themes(name)
);

create table questions(
	id int primary key GENERATED ALWAYS AS IDENTITY,
	text varchar(255) not null,
	theme varchar(50) references themes(name),
	show_variants boolean not null,
	time_to_answer smallint default (15)
);

create table answers(
	id bigint primary key GENERATED ALWAYS AS IDENTITY,
	question int not null references questions(id) ON DELETE CASCADE,
	text varchar(255) not null,
	is_right boolean not null
);

create table quizzes_users_likes(
	quiz smallint not null references quizzes(id),
	user_pk varchar(50) not null references users(username),
	date_time timestamp default (now())
);

create table user_quizzes_results(
	quiz smallint not null references quizzes(id),
	user_pk varchar(50) not null references users(username),
	time_passes timestamp not null default(now()),
	result smallint not null check (result between 0 and 100)
);

create table user_answers(
	user_pk varchar(50) not null references users(username),
	questions int not null references questions(id),
	is_successful boolean not null default (false),
	answer_date date not null default (now())
);

create table quiz_questions(
	current_count smallint not null default (0),
	question int not null references questions(id),
	quiz smallint not null references quizzes(id),
	primary key(current_count, quiz)
);