create table hardskill_table (
    id serial,
    title VARCHAR(64) not null,
    author VARCHAR not null default 'akhromlyuk',
    created INTEGER not null,
    updated INTEGER,
    finished BOOLEAN default FALSE,
    DESCRIPTION VARCHAR default '',
    link_approve_first VARCHAR(255) default '',
    link_approve_second VARCHAR(255) default ''
);