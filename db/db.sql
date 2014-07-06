drop table if exists habitacion;
drop table if exists componente;
drop table if exists usuario;
create table habitacion (
  habitacion_id 		INTEGER PRIMARY KEY AUTOINCREMENT,
  name 					TEXT NOT NULL
);
create table componente (
  componente_id 		INTEGER PRIMARY KEY AUTOINCREMENT,
  name 					TEXT NOT NULL,
  address 				TEXT NOT NULL,
  hab_id_fk				INTEGER,
  FOREIGN KEY(hab_id_fk) REFERENCES habitacion(id)
);
create table usuario (
  usuario_id 			INTEGER PRIMARY KEY AUTOINCREMENT,
  name 					TEXT NOT NULL,
  pass					TEXT NOT NULL,
  admin					BOOLEAN NOT NULL
);

insert into habitacion (name) values ('Salon');
insert into habitacion (name) values ('Cocina');
insert into habitacion (name) values ('Baño');
insert into habitacion (name) values ('Viky');
insert into habitacion (name) values ('Oliva y Suso');
insert into habitacion (name) values ('Invitados');

insert into usuario (name,pass,admin) values ('admin','1234',1);
insert into usuario (name,pass,admin) values ('usuario','1234',1);

select * from usuario;

