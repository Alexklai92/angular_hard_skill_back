create table posts_table (
    id serial,
    title VARCHAR(64) not null,
    path_to_body VARCHAR(255) not null,
    author VARCHAR not null,
    created INTEGER not null,
    updated INTEGER,
    commits INTEGER[]
);