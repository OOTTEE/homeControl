drop table if exists habitacion;
drop table if exists componente;
drop table if exists usuario;
drop table if exists accion;

create table habitacion (
  h_id						INTEGER PRIMARY KEY AUTOINCREMENT,
  name 						TEXT NOT NULL
);
create table componente (
  c_id 						INTEGER PRIMARY KEY AUTOINCREMENT,
  name 						TEXT NOT NULL,
  address 					TEXT NOT NULL,
  tipo						TEXT NOT NULL,
  fk_h_id					INTEGER,
  FOREIGN KEY(fk_h_id)		REFERENCES habitacion(h_id)
);
create table usuario (
  u_id 						INTEGER PRIMARY KEY AUTOINCREMENT,
  name 						TEXT NOT NULL,
  pass						TEXT NOT NULL,
  administrador				BOOLEAN NOT NULL
);
create table accion (
	a_id					INTEGER PRIMARY KEY AUTOINCREMENT,
	hora					INTEGER NOT NULL,
	accion					TEXT NOT NULL,
	fk_u_id					INTEGER NOT NULL,
	fk_c_id					INTEGER NOT NULL,
	FOREIGN KEY(fk_u_id)	REFERENCES usuario(u_id),
	FOREIGN KEY(fk_c_id)	REFERENCES componente(c_id)
);
/*
insert into habitacion (name) values ('Salon');
insert into habitacion (name) values ('Cocina');
insert into habitacion (name) values ('Baño');
insert into habitacion (name) values ('Viky');
insert into habitacion (name) values ('Oliva y Suso');
insert into habitacion (name) values ('Invitados');

// md5(1234) = 81dc9bdb52d04dc20036dbd8313ed055
insert into usuario (name,pass,admin) values ('admin','81dc9bdb52d04dc20036dbd8313ed055',1);
insert into usuario (name,pass,user) values ('usuario','81dc9bdb52d04dc20036dbd8313ed055',0);
*/