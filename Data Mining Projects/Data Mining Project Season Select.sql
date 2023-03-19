create database DataMining;

select * from DataMining.order_train0;

alter table DataMining.order_train0 modify order_date datetime;

select * from DataMining.order_train0 where order_date between '2016-1-01' and '2016-4-30';
select * from DataMining.order_train0 where order_date between '2016-05-01' and '2016-08-31';
select * from DataMining.order_train0 where order_date between '2016-09-01' and '2016-12-31';

select * from DataMining.order_train0 where order_date between '2017-1-01' and '2017-4-30';
select * from DataMining.order_train0 where order_date between '2017-05-01' and '2017-08-31';
select * from DataMining.order_train0 where order_date between '2017-09-01' and '2017-12-31';

select * from DataMining.order_train0 where order_date between '2018-1-01' and '2018-4-30';
select * from DataMining.order_train0 where order_date between '2018-05-01' and '2018-08-31';
select * from DataMining.order_train0 where order_date between '2018-09-01' and '2018-12-31';





