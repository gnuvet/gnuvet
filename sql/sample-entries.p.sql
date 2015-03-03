/*
 * Copyright (c) 2012 Enno Deimel <enno dot vet at gmx dot net>
 *
 * This file is part of gnuvet, published under the GNU General Public License
 * (GPL in short).  See the file GPL for more Information.
 */

--insert into boxroles (boxr_name) values
-- ('master server'),('local server'),('workstation');

--insert into boxes (box_name,box_ipv4,box_branch,box_role) values
-- ('master.dunton.org','192.168.1.1',1,1),
-- ('mash.dunton.org',  '192.168.1.2',1,3),
-- ('box3.dunton.org',  '192.168.1.3',1,3);

insert into staff (stf_func,stf_title,stf_surname,stf_mname,stf_forename,stf_short,stf_logname,stf_sex)values
 (2,2,'Deimel','T.E.','Enno','ED','enno','m'),
 (4,3,'Umek','','Susie','SU','susie','f'),
 (3,4,'Xam-Ple','','E','EX','xmpl','f');

insert into addresses (housen,street,village,city,region,postcode)values
('112','Opensource Street','Upston','Gnuville','','GN7 U12'),
('Dunton Hall','Kingsbury Road','Curdworth','Sutton Coldfield','West Midlands','B76 0BA'),
('38','Dempsey Close','Mildew','Worthton','East Midlands','E28 2BT'),
('Dew Farm','Dew Road','Dalmarth','','Staffordshire','ST4 8QR'),
('24','Debbing Road','Wellings','Hightree','','HT7 8TF'),
('64','Abbey Street','Parish','Churchton','West Midlands',''),
('77','Boxcart Street','Ringwell','Sporsing','East Midlands','E34 7MN'),
('57','Toad Road','Laxing','Wellington','West Midlands','WM4 8UR'),
('Wye Farm House','Wye Road','Pisting','','West Midlands','WM7 9BD'),
('29','Twyecross Street','Lisloose','Pilkershill','West Midlands','WM3 4TB'),
('64','Twyecross Street','Lisloose','','West Midlands','WM3 4TB'),
('Gorse Manor Farm','Gorse Manor Road','Pixing','','East Midlands','EM3 7TD'),
('25','Lipton Street','','','West Midlands','WM3 0TS'),
('35','Cowslip Close','Dipton','Derbymore','West Midlands','WM3 0TS'),
('White House','Long Lane','Capitol','Washington','USA','10034-5'),
('47','Wiley Street','Worthington','Polland','West Midlands','WM3 4BS'),
('26','Dromley Drive','Locking','Sutton Upmoor','West Midlands','WM43 5QT'),
('34','Depster Lane','','Bromsgrove','','ST3 0GH'),
('','Tosh Manor Road','Pasting','','West Midlands','WM7 5SR');

insert into branches(branch_name,branch_address,branch_tel)values
('GnuVet Veterinary Clinic',2,'01234-678789');

insert into clients (c_title,c_sname,c_mname,c_fname,c_address,c_reg,c_last)values
(2,'Deimel','T.E.','Enno',3,'2006-02-02','2009-06-01 12:34:00'),
(2,'Foster','T.','Charles',4,'2007-05-30','2008-06-01 12:34:00'),
(3,'Langley','','Mildred',5,'2008-08-01','2009-05-01 12:34:00'),
(4,'Kiddington','B.','Lisa',6,'2007-06-30','2009-05-01 18:34:00'),
(2,'Wallace','','Gromit',7,'2008-01-07','2009-04-01 18:34:00'),
(2,'Tyson','B.S.','Mike',8,'2008-07-31','2008-12-01 14:34:00'),
(3,'Postington','J.','Janet',9,'2007-09-01','2008-11-01 14:34:00'),
(2,'Farmland','C.','James',10,'2007-03-04','2009-05-16 10:11:00'),
(4,'Carlington','M.','Anny',11,'2007-04-17','2009-03-16 15:11:39'),
(2,'Dexter','H.','Homer',12,'2007-02-28','2009-03-17 16:23:49'),
(3,'Dexter','','Julie',13,'2007-05-31','2008-12-23 18:08:12'),
(2,'Postington','M.','Barnard',14,'2007-12-18','2007-04-21 09:35:18'),
(3,'Gower','J.','Julie',15,'2007-11-29','2008-06-26 17:12:28'),
(2,'Powell','D.H.','Colin',16,'2006-07-06','2006-7-6 15:48:23'),
(4,'Clinton','C.','Clara',17,'2007-03-21','2008-10-11 15:32:46'),
(2,'Grimes','','Will',18,'2006-08-12','2009-04-12 16:35:24'),
(3,'Jones','M.','Jeanne',3,'2006-02-02','2009-02-12 12:36:15'),
(2,'Dutton','','Frank',19,'2008-6-7','2008-6-7 10:32:54');

-- could say 'default' instead of '2':
insert into locations (l_id,l_name,l_address,l_tel,l_mobile,l_anno)values
(2,'Tosh Manor Farm',20,'','','');

insert into patients (p_name,p_cid,breed,xbreed,dob,dobest,colour,sex,neutd,loc,vicious,p_last,p_reg)values
('Emiliano Zapata von Krawums',2,34,FALSE,'1999-07-07',FALSE,7,'m',FALSE,1,FALSE,'2009-06-01 12:34:00','2005-05-05'),
('Bobby',	     3,20,FALSE,'1999-8-01',FALSE,1,'m',TRUE,1,FALSE,'2008-06-01 12:34:00','2005-05-05'),
('Darcy',	     4,29,FALSE,'2001-5-6', FALSE,86,'f',FALSE,1,FALSE,'2008-07-01 12:34:00','2005-05-05'),
('Percy',	     5,13,FALSE,'1999-7-6', FALSE,30,'m',TRUE,2,FALSE,'2009-05-01 12:34:00','2005-05-05'),
('Mally',	     5,41,FALSE,'2003-4-3', FALSE,1,'f',TRUE,1,FALSE,'2009-05-01 18:34:00','2005-05-05'),
('Hank',	     6,39,FALSE,'2001-5-4', FALSE,60,'m',FALSE,1,FALSE,'2009-04-01 18:34:00','2005-05-05'),
('Billy',	     7,37,FALSE,'2003-6-7', FALSE,4,'m',TRUE,1,FALSE,'2008-12-01 14:34:00','2005-05-05'),
('Billy',	     8,49,FALSE,'2001-8-7', FALSE,94,'f',TRUE,1,FALSE,'2008-11-01 14:34:00','2005-05-05'),
('Milly',	     9,29,TRUE, '2002-6-12', TRUE,86,'f',null,1,FALSE,'2009-05-16 10:11:00','2005-05-05'),
('David',	    10,22,FALSE,'1998-7-16',FALSE,1,'m',FALSE,1,FALSE,'2009-03-16 15:11:39','2005-05-05'),
('Shalhoul',	    11,14,FALSE,'1993-4-18',FALSE,3,'m',FALSE,1,FALSE,'2009-03-17 16:23:49','2005-05-05'),
('Magouti',	    12,18,FALSE,'2004-7-3', FALSE,1,'f',TRUE,1,FALSE,'2008-12-23 18:08:12','2005-05-05'),
('Raswan I',	    13,14,FALSE,'1987-3-4', FALSE,21,'m',TRUE,1,FALSE,'2007-04-21 09:35:18','2005-05-05'),
('Sherpa Tensing', 14,24,FALSE,'2003-7-6', FALSE,1,'m',FALSE,1,FALSE,'2008-06-26 17:12:28','2005-05-05'),
('McLane',	    17,94,TRUE,'2001-10-11',FALSE,1,'m',TRUE,1,FALSE,'2009-01-31 11:17:36','2005-05-05'),
('Elsa',	    18,84,FALSE,'1999-02-25',TRUE,1,'f',FALSE,1,FALSE,'2009-02-12 12:36:15','2005-05-05'),
('Bull',	    17,12,FALSE,'2005-04-02',FALSE,4,'m',FALSE,1,FALSE,'2009-02-27 10:49:26','2005-05-05'),
('Alina',	    16,193,FALSE,'2004-03-22',FALSE,75,'f',FALSE,1,TRUE,'2008-10-11 15:32:46','2005-05-05'),
('Rex',		    17,97,FALSE,'2002-05-15',FALSE,1,'m',FALSE,1,TRUE,'2009-04-12 16:35:24','2005-05-05'),
('Dönci',           2,34,FALSE,'2005-05-17',FALSE,7,'m',TRUE,1,FALSE,'2012-04-22 0:0:0','2011-12-14');

insert into neuts values (2,'2000-3-4'),(4,'2001-3-5'),(8,'2002-2-20'),
 (12,'2005-1-20'),(13,'1992-7-8'),(15,'2002-4-30'),(20,NULL);

insert into seen values (1,'2005-05-05'),(1,'2009-06-01'),(2,'2005-05-05'),(2,'2008-06-01'),(3,'2005-05-05'),(3,'2008-07-01'),(4,'2005-05-05'),(4,'2009_05-01'),(5,'2005-05-05'),(5,'2009-05-01'),(6,'2005-05-05'),(6,'2009-04-01'),(7,'2005-05-05'),(7,'2008-12-01'),(8,'2005-05-05'),(8,'2008-11-01'),(9,'2005-05-05'),(9,'2009-05-16'),(10,'2005-05-05'),(10,'2009-03-16'),(11,'2005-05-05'),(11,'2009-03-17'),(12,'2005-05-05'),(12,'2008-12-23'),(13,'2005-05-05'),(13,'2007-04-21'),(14,'2005-05-05'),(14,'2008-06-26'),(15,'2005-05-05'),(15,'2009-01-31'),(16,'2005-05-05'),(16,'2009-02-12'),(17,'2005-05-05'),(17,'2009-02-27'),(18,'2005-05-05'),(18,'2008-10-11'),(19,'2005-05-05'),(19,'2009-04-12'),(20,'2012-04-22');

update patients set rip='1' where p_name='Elsa';

insert into rips values (16,'2009-03-22');

update patients set chr=288 where p_name='Elsa';

update patients set identno='040000000123456' where p_name like 'Emiliano%';
update patients set identno='040096100106864',petpass='040-0101555' where p_id=20;

-- update clients set c_telhome='01675 478 322',c_mobile1='07726 898 122',c_email='enno.vet@gmx.net' where c_sname='Deimel';
update clients set c_email='enno.vet@gmx.net' where c_sname='Deimel';
insert into phones values(2,2,'01675 478 322',''),(2,2,'07726 898 122',''),(2,1,'+43(0)664 657 60 55','');

update clients set baddebt='1' where c_id=17;

drop table if exists e1 cascade;
create table e1(id serial primary key);
insert into e1 values (1),(2),(3),(4),(5),(6);
drop table if exists ch1 cascade;
create table ch1(id serial primary key,consid integer not null references e1,dt timestamp not null default current_timestamp,text varchar(1024) not null default '',symp integer not null references symptoms default 1,staff integer references staff not null default 1);
insert into ch1(consid,dt,text,symp)values
 (1,'2005-04-11 08:54:19','o.B.',1),
 (2,'2005-05-10 10:44:32','o.B.',1),
 (3,'2006-05-12 11:12:15','o.B.',1),
 (4,'2007-05-10 10:38:32','o.B.',1),
 (5,'2008-05-08 11:24:12','o.B.',1),
 (6,'2009-05-10 10:12:34','o.B.',1);
drop table if exists prod1 cascade;
create table prod1(id serial primary key,consid integer not null references e1,dt timestamp not null default current_timestamp,prodid integer not null references products,count numeric(8,2) not null default 1,symp integer not null references symptoms default 1,staff integer not null references staff default 1);
insert into prod1(consid,dt,prodid,count,symp)values
 (1,'2005-04-11 08:52:19',130,1,1), -- seq was 3
 (2,'2005-05-10 10:43:32',131,1,1), -- seq was 3
 (2,'2005-05-10 10:44:05',140,1,1), -- seq was 3
 (3,'2006-05-12 11:11:23',133,1,1), -- seq was 3
 (4,'2007-05-10 10:37:08',133,1,1), -- seq was 3
 (4,'2007-05-10 10:37:43',140,1,1), -- seq was 3
 (5,'2008-05-08 11:23:44',133,1,1), -- seq was 3
 (6,'2009-05-10 10:12:00',133,1,1), -- seq was 3
 (6,'2009-05-10 10:12:32',140,1,1); -- seq was 3

drop table if exists e20 cascade;
create table e20(id serial primary key);
insert into e20 values (default);
insert into e20 values (default);

drop table if exists ch20 cascade;
create table ch20(id serial primary key,consid integer not null references e20,dt timestamp not null default current_timestamp,text varchar(1024) not null default '',symp integer not null references symptoms default 1,staff integer references staff not null default 1);
insert into ch20(consid,dt,text,symp)values
 (1,'2012-05-14 17:51:34.473996','Watery diarrhea for 3 days,IBT 39.5°C,had vomited 3 days ago,unknown vaccination status.',12),
 (2,'2012-07-28 13:37:57.584051',E'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np,li { white-space: pre-wrap; }\n</style></head><body style=" font-family:''Sans Serif''; font-size:9pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">And now for <span style=" color:#ff0000;">something </span><span style=" color:#0000ff;">completely </span><span style=" color:#000000;">different...</span></p></body></html>',1);

drop table if exists prod20;
create table prod20(
 id serial primary key,
 consid integer not null references e20,
 dt timestamp not null default current_timestamp,
 prodid integer not null references products,
 count numeric(8,2) not null default 1,
 symp integer not null references symptoms default 1,
 staff integer not null references staff default 1
);
insert into prod20(consid,dt,prodid,count,symp)values
 (1,'2012-05-14 17:51:34.473996',37,1,12), -- seq was 1
 (1,'2012-05-14 17:51:34.473996',5,14,12), -- seq was 3
 (2,'2012-07-28 13:37:57.584051',37,1,1), -- seq was 1
 (2,'2012-07-28 13:37:57.584051',16,1,1); -- seq was 3

drop table if exists weight16 cascade;
create table weight16(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
insert into weight16(w_date,weight,w_staff)values('2009-1-1 11:34',86,4);

drop table if exists weight1 cascade;
drop table if exists weight2 cascade;
drop table if exists weight3 cascade;
drop table if exists weight4 cascade;
drop table if exists weight5 cascade;
drop table if exists weight6 cascade;
drop table if exists weight7 cascade;
drop table if exists weight8 cascade;
drop table if exists weight9 cascade;
drop table if exists weight10 cascade;
drop table if exists weight20 cascade;

create table weight1(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight2(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight3(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight4(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight5(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight6(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight7(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight8(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight9(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight10(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
create table weight20(w_id serial primary key,w_est boolean not null default '0',w_date timestamp not null default current_timestamp,weight numeric(7,3) not null,w_staff integer references staff not null default 1);
insert into weight1(w_date,w_est,weight)values('2000 6 6',False,1.1),('2000 7 7',True,2.2),('2000,8,8',False,1.3),('2000 9 9',False,3.2),('2000 10 11',False,4.1),('2001 3 12',True,2.8),('2001 4 12',False,3.2),('2001 4 18',False,3.7),('2001 5 1',False,4.6),('2001 11 12',False,7.7),('2002 4 12',False,13.4),('2002 8 12',False,16.8),('2003 1 12',False,20.5);
insert into weight2(w_date,weight)values('2000 6 6',5),('2000 7 7',10.3),('2000 8 8',18.4),('2000 9 9',24.2),('2000 10 11',27.8),('2001 3 12',34.9);
insert into weight3(w_date,weight)values('2000 6 6',4),('2000 7 6',6),('2000 8 6',7);
insert into weight4(w_date,weight)values('2000 6 6',60),('2000 7 7',320),('2000 8 8',480),('2000 9 9',560),('2000 10 11',600),('2001 3 12',680);
insert into weight5(w_date,weight)values('2012 1 10',0.005),('2012 1 20',0.008),('2012 1 24',0.012),('2012 1 31',0.015);
insert into weight6(w_date,weight)values('2012 1 12 12:08:16',31.8),('2012 1 12 13:08',32),('2012 1 12 15:16:12',32.8);
insert into weight7(w_date,weight)values('2000 6 6',6.5),('2000 7 7',6),('2000 8 8',5.7),('2000 9 9',5.2),('2000 10 11',5);
insert into weight8(w_date,weight)values('2012 1 1',12),('2012 2 1',13.5);
insert into weight9(w_date,weight)values('2012 1 31',12.5);
insert into weight10(w_date,weight)values('2011 12 12',8.6);
insert into weight20(w_date,weight)values('2011 12 14 16:02:08',32.8),('2011 12 21 16:02:08',31.8),('2011 12 28 16:02:08',30.8),('2012 1 25 16:02:08',32),('2012 2 22 16:02:08',32),('2013 11 20 10:00:45',35.5);

drop table if exists vac1 cascade;
create table vac1(v_type integer not null references vtypes); -- obs?
insert into vac1 values (2),(2),(5),(2),(2),(5),(2),(2),(5);
insert into vdues values(1,2,'2010-05-10'),(1,5,'2012-05-10');

drop table if exists vac16 cascade;-- Elsa
create table vac16(v_type integer not null references vtypes); -- obs?
insert into vac16 values (2);
insert into vdues values(16,2,'2009-3-24');
drop table if exists e16;
create table e16(id serial primary key);
insert into e16 default values;
drop table if exists prod16 cascade;
create table prod16(id serial primary key,consid integer not null references e16,dt timestamp not null default current_timestamp,prodid integer not null references products,count numeric(8,2) not null default 1,symp integer not null references symptoms default 1,staff integer not null references staff default 1);
insert into prod16(consid,dt,prodid)values(1,'2008-3-24 14:44:45',133);
drop table if exists ch16 cascade;
create table ch16(id serial primary key,consid integer not null references e16,dt timestamp not null default current_timestamp,text varchar(1024) not null default '',symp integer not null references symptoms default 1,staff integer references staff not null default 1);
insert into ch16(consid,dt,text)values(1,'2008-3-24 14:45:45','o.B.');

drop table if exists vac19 cascade; -- Rex
create table vac19(v_type integer not null references vtypes); -- obs?
insert into vac19 values (2);
insert into vdues values(19,2,'2009-3-12');
drop table if exists e19;
create table e19(id serial primary key);
insert into e19 default values;
drop table if exists prod19;
create table prod19(id serial primary key,consid integer not null references e19,dt timestamp not null default current_timestamp,prodid integer not null references products,count numeric(8,2) not null default 1,symp integer not null references symptoms default 1,staff integer not null references staff default 1);
insert into prod19(consid,dt,prodid)values(1,'2008-3-12 14:34:12',133);
drop table if exists ch19 cascade;
create table ch19(id serial primary key,consid integer not null references e19,dt timestamp not null default current_timestamp,text varchar(1024) not null default '',symp integer not null references symptoms default 1,staff integer references staff not null default 1);
insert into ch19(consid,dt,text)values(1,'2008-3-12 14:35:45','o.B.');

insert into addresses(housen,street,village,city,region,postcode)values
 ('NVS','Twyman Street','','Brummagem','West Midlands','B72 5SO'),
 ('3','Dordon Road','Wickenham','London','','SE23 42E'),
 ('','Gaadenstraat 15','','Törensen','','DK 8342');

insert into suppliers(s_name,s_address,s_tel,s_fax,s_mobile,s_email,s_rep)values
 ('NVS',21,'0121 378 98 98','0121 378 98 99','07815 044 044',
 'order@nvs.co.uk','Mr Harvey E. Mittens'),
 ('Vetoquinol',22,'020 467 33 22','020 467 33 33','07799 348 23 65',
 'vet@vetoquinol.co.uk','Mr Nevar T.B. Shangarathi'),
 ('Kruuse',23,'+3x989 123 456','+3x989 456 123','','info@kruuse.dk','');

drop table if exists inst20 cascade;
create table inst20(id serial primary key,text varchar(300) not null default '',prodid integer not null references prod20);
insert into inst20(text,prodid)values('Give 1 tablet twice daily for 7 days',2); --,('Give 1 tablet twice daily for 3 days',7),('Give 1 tablet per day for 3 days',8);

insert into invoices(inv_no)values(1205140001),(1207280001);

drop table if exists acc2 cascade;
create table acc2(
 acc_id serial primary key,
 acc_pid integer references patients,
 acc_prid integer not null references prod20,
 acc_npr numeric(9,2) not null,
 acc_vat integer not null references vats default 1,
 acc_invd bool not null default False);
insert into acc2(acc_pid,acc_prid,acc_npr,acc_vat)values
 (20,1,20,1),
 (20,2,6.02,2),
 (20,3,20,1),
 (20,4,1.28,2);

--drop table if exists pay2 cascade;
--create table pay2(pay_id serial primary key,pay_date date not null default current_date,pay_amount numeric(9,2)not null default 0);

insert into appointments(app_dt,app_text,app_cid,app_pid,app_staffid,app_dur)values
 ('2013-5-31 9:30','Cat spay',null,null,1,'1:00'),
 ('2013-5-31 11:30','Dog consultation',2,20,2,'0:30'),
 ('2013-5-31 10:30','Call Ringo',null,null,2,'0:0'),
 ('2013-5-31 11:30','Dog castr.',null,null,1,'0:30'),
 ('2013-6-1 8:30','Mooh',17,17,1,'0:0');

/*
ALTER TABLE tablename ADD CONSTRAINT constr_name FOREIGN KEY (col_name) REFERENCES othertable[(col_name)]
*/

/*
drop table if exists vac1;
create table vac1(v_id serial primary key,vvacid integer not null references vaccinations,vdate timestamp not null,vdue date);
insert into vac1(vvacid,vdate,vdue)values
 (4,'2005-04-11 08:54:19','2005-05-11'),
 (4,'2005-05-10 10:44:32','2006-05-11'),
 (11,'2005-05-10 10:45:30','2007-05-10'),
 (4,'2006-05-12 11:12:15','2007-05-12'),
 (4,'2007-05-10 10:38:32','2008-05-10'),
 (11,'2007-05-10 10:39:22','2009-05-10'),
 (4,'2008-05-08 11:24:12','2009-05-08'),
 (4,'2009-05-10 10:12:34','2010-05-10'),
 (11,'2009-05-10 10:12:35','2011-05-10');

drop table if exists vac16;
create table vac16(v_id serial primary key,vvacid integer not null references vaccinations,vdate timestamp not null,vdue date);
insert into vac16(vvacid,vdate,vdue)values
 (4,'2008-03-24 14:44:45','2009-03-24');
drop table if exists vac19;
create table vac19(v_id serial primary key,vvacid integer not null references vaccinations,vdate timestamp not null,vdue date);
insert into vac19(vvacid,vdate,vdue)values
 (4,'2008-03-12 14:34:12','2009-03-12');
*/
