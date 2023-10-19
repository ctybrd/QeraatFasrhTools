CREATE VIEW all_qeraat
AS
SELECT quran_data.*, quran_sora.sora_name, book_quran.text, book_quran.text_full
FROM quran_data
LEFT JOIN quran_sora ON quran_data.sora = quran_sora.sora
LEFT JOIN book_quran ON (quran_data.sora = book_quran.sora AND quran_data.aya = book_quran.aya);


# remove extra رقم الآية text
# UPDATE quran_data
# SET subject = SUBSTR(subject, 1, INSTR(subject, '- رقم الآية:') - 1)
# WHERE INSTR(subject, '- رقم الآية:') > 0;
#remove curly braces
# UPDATE quran_data
# SET subject = REPLACE(REPLACE(subject, '{', ''), '}', ''),
#    sub_subject = REPLACE(REPLACE(sub_subject, '{', ''), '}', '');

# update quran_data set page_number1=(SELECT mosshf_madina.page_number  from mosshf_madina where aya_number= quran_data.aya and sora_number=quran_data.sora)
# update quran_data set page_number2=(SELECT mosshf_shmrly.page_number  
# from mosshf_shmrly where aya_number= quran_data.aya and sora_number=quran_data.sora)

-- Add columns Q1, R1_1, R1_2
ALTER TABLE quran_data ADD COLUMN Q1 TEXT;
ALTER TABLE quran_data ADD COLUMN R1_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R1_2 TEXT;

-- Add columns Q2, R2_1, R2_2
ALTER TABLE quran_data ADD COLUMN Q2 TEXT;
ALTER TABLE quran_data ADD COLUMN R2_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R2_2 TEXT;

-- Add columns Q3, R3_1, R3_2
ALTER TABLE quran_data ADD COLUMN Q3 TEXT;
ALTER TABLE quran_data ADD COLUMN R3_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R3_2 TEXT;

-- Add columns Q4, R4_1, R4_2
ALTER TABLE quran_data ADD COLUMN Q4 TEXT;
ALTER TABLE quran_data ADD COLUMN R4_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R4_2 TEXT;

-- Add columns Q5, R5_1, R5_2
ALTER TABLE quran_data ADD COLUMN Q5 TEXT;
ALTER TABLE quran_data ADD COLUMN R5_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R5_2 TEXT;

-- Add columns Q6, R6_1, R6_2
ALTER TABLE quran_data ADD COLUMN Q6 TEXT;
ALTER TABLE quran_data ADD COLUMN R6_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R6_2 TEXT;

-- Add columns Q7, R7_1, R7_2
ALTER TABLE quran_data ADD COLUMN Q7 TEXT;
ALTER TABLE quran_data ADD COLUMN R7_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R7_2 TEXT;

-- Add columns Q8, R8_1, R8_2
ALTER TABLE quran_data ADD COLUMN Q8 TEXT;
ALTER TABLE quran_data ADD COLUMN R8_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R8_2 TEXT;

-- Add columns Q9, R9_1, R9_2
ALTER TABLE quran_data ADD COLUMN Q9 TEXT;
ALTER TABLE quran_data ADD COLUMN R9_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R9_2 TEXT;

-- Add columns Q10, R10_1, R10_2
ALTER TABLE quran_data ADD COLUMN Q10 TEXT;
ALTER TABLE quran_data ADD COLUMN R10_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R10_2 TEXT;


update quran_data set Q1=1 where 
(qarees like '%نافع%') and 
NOT ((qarees like '%قالون%')  or (qarees like '%ورش%'))

update quran_data set R1_1=1 where 
(qarees like '%قالون%') or (Q1=1)  
update quran_data set R1_2=1 where 
(qarees like '%ورش%') or (Q1=1) 


--select * from quran_data where R1_1=1 and (reading not like '%صلة ميم الجمع %')

update quran_data set Q2=1 where 
(qarees like '%كثير%') and 
NOT ((qarees like '%البزي%')  or (qarees like '%قنبل%'))

update quran_data set R2_1=1 where (qarees like '%البزي%') or (Q2=1) 
update quran_data set R2_2=1 where (qarees like '%قنبل%') or (Q2=1) 


update quran_data set Q3=1 where 
(qarees like '%عمرو%') and 
NOT ((qarees like '%الدوري_عن_ أبي عمرو%')  or (qarees like '%السوسي_عن_ أبي عمرو%'))

update quran_data set R3_1=1 where (qarees like '%الدوري_عن_ أبي عمرو%') or (Q3=1) 
update quran_data set R3_2=1 where (qarees like '%السوسي_عن_ أبي عمرو%') or (Q3=1) 


update quran_data set Q4=1 where 
(qarees like '%عامر%') and 
NOT ((qarees like '%هشام%')  or (qarees like '%ذكوان%'))

update quran_data set R4_1=1 where (qarees like '%هشام%') or (Q4=1) 
update quran_data set R4_2=1 where (qarees like '%ذكوان%') or (Q4=1)

update quran_data set Q5=1 where 
(qarees like '%عاصم%') and 
NOT ((qarees like '%شعبة%')  or (qarees like '%حفص%'))

update quran_data set R5_1=1 where (qarees like '%شعبة%') or (Q5=1) 
update quran_data set R5_2=1 where (qarees like '%حفص%') or (Q5=1)  

update quran_data set Q6=1 where 
(qarees like '%حمزة%') and 
NOT ((qarees like '%خلف_عن_ حمزة%')  or (qarees like '%خلاد_عن_ حمزة%'))

update quran_data set R6_1=1 where (qarees like '%خلف_عن_ حمزة%') or (Q6=1) 
update quran_data set R6_2=1 where (qarees like '%خلاد_عن_ حمزة%') or (Q6=1)  


update quran_data set Q7=1 where 
(qarees like '%الكسائي%') and 
NOT ((qarees like '%الدوري_عن_ الكسائي%')  or (qarees like '%الحارث%'))

update quran_data set R7_1=1 where (qarees like '%الحارث%') or (Q7=1) 
update quran_data set R7_2=1 where (qarees like '%الدوري_عن_ الكسائي%') or (Q7=1)  

update quran_data set Q8=1 where 
(qarees like '%جعفر%') and 
NOT ((qarees like '%وردان%')  or (qarees like '%جماز%'))

update quran_data set R8_1=1 where (qarees like '%وردان%') or (Q8=1) 
update quran_data set R8_2=1 where (qarees like '%جماز%') or (Q8=1) 

update quran_data set Q9=1 where 
(qarees like '%يعقوب%') and 
NOT ((qarees like '%روح%')  or (qarees like '%رويس%'))

update quran_data set R9_1=1 where (qarees like '%رويس%') or (Q9=1) 
update quran_data set R9_2=1 where (qarees like '%روح%') or (Q9=1) 

update quran_data set Q10=1,R10_1=1,R10_2=1 where 
(qarees like '%العاشر%') 

--update quran_data set R10_1=1 where (qarees like '%دريس%') or (Q10=1) 
--update quran_data set R10_2=1 where (qarees like '%إسحق%') or (Q10=1) 

update quran_data set R5_2=0 where R5_2 is null
update quran_data set Q5=0 where Q5 is null

update quran_data set R5_2=Null where R5_2=0
update quran_data set Q5=Null where Q5=0

update quran_data set 
Q1=1,R1_1=1,R1_2=1,
Q2=1,R2_1=1,R2_2=1,
Q3=1,R3_1=1,R3_2=1,
Q4=1,R4_1=1,R4_2=1,
Q5=1,R5_1=1,R5_2=1,
Q6=1,R6_1=1,R6_2=1,
Q7=1,R7_1=1,R7_2=1,
Q8=1,R8_1=1,R8_2=1,
Q9=1,R9_1=1,R9_2=1,
Q10=1,R10_1=1,R10_2=1 where qarees like '%كل الرواة%'

update quran_data set Q1=null  where R1_1  is null or R1_2 is null
update quran_data set Q2=null  where R2_1  is null or R2_2 is null
update quran_data set Q3=null  where R3_1  is null or R3_2 is null
update quran_data set Q4=null  where R4_1  is null or R4_2 is null
update quran_data set Q5=null  where R5_1  is null or R5_2 is null
update quran_data set Q6=null  where R6_1  is null or R6_2 is null
update quran_data set Q7=null  where R7_1  is null or R7_2 is null
update quran_data set Q8=null  where R8_1  is null or R8_2 is null
update quran_data set Q9=null  where R9_1  is null or R9_2 is null
update quran_data set Q10=null where R10_1 is null or R10_2 is null


select * from quran_data where R1_1=1 and R5_2 is null
and reading not like '%صلة%ميم%جمع%'
and reading not like '%ميم%جمع%وصل%'
and (q8=1 or r8_1=1 or r8_2=1)
 order by aya_index,id
 
select reading,count(*) from quran_data
group by reading
order by count(*) desc

insert into tagsmaster(tag,description,qarees,category)
VALUES('meemsela','صلة ميم الجمع وصلا','حمزة',null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('sakt2', 'السكت على الساكن قبل الهمزة',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('waqfhamer','وقف هشام','حمزة',null);


insert into tagsmaster(tag,description,qarees,category)
VALUES('waqfh1','تغيير الهمزة المتوسطة لحمزة وقفا','حمزة',null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('waqfh2', 'تسهيل الهمزة المتوسطة بزائد لحمزة وقفا (وإذا، ولأتم)','حمزة',null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('ishmam','الإشمام بأنواعه',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('ishmams','إشمام الصاد صوت الزاي في (الصراط وصراط،)','حمزة',null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('haadam', 'ضم هاء ضمير الجمع والمثنى',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('haaakasr', 'كسر هاء ضمير الجمع والمثنى',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('idgham','الإدغام بنوعَيْه',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('idghamn','الإدغام بغير غنة',null,null);


insert into tagsmaster(tag,description,qarees,category)
VALUES('idghak','الإدغام الكبير',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('raatarkek','ترقيق الراء',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('lamtaghlez','تغليظ اللام',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('haasokon','إسكان الهاء',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('taklel','التقليل',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('imala','الإمالة',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('taklelw','التقليل وقفا',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('imalaw','الإمالة وقفا',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('imalah','إمالة هاء التأنيث',null,null);


insert into tagsmaster(tag,description,qarees,category)
VALUES('haasakt','هاء السكت',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('nakl','النقل',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('ibdal','إبدال الهمز',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('badal','ثلاثة مدل البدل',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('ikhfaa','إخفاء عند الخاء والغين',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('yaafath','فتح ياء الإضافة',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('hamzatan','الهمزتين',null,null);

UPDATE quran_data set tags=IFNULL(tags,',') ||'meemsela,'
where reading like '%صلة%ميم%جمع%' 
and 
ifnull(tags,',') not like '%meemsela,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'meemsela,'
where reading like '%ميم%جمع%وصلا%' 
and 
ifnull(tags,',') not like '%meemsela,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'ikhfaa,'
where reading like '%خفاء عند الغين والخاء%'
and 
ifnull(tags,',') not like '%ikhfaa,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'taklelw,'
where reading like '%تقليل%وقفا%'
and 
ifnull(tags,',') not like '%taklelw,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'taklel,'
where reading like '%تقليل%'
and 
ifnull(tags,',') not like '%taklel,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'imalah,'
where reading like '%إمالة هاء التأنيث%'
and 
ifnull(tags,',') not like '%imalah,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'idghak,'
where reading like '%%غام%كبير%%'
and 
ifnull(tags,',') not like '%idghak,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'ishmams,'
where reading like '%شمام%صاد%' and 
sub_subject like '%صراط%'
and 
ifnull(tags,',') not like '%ishmams,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'ishmam,'
where reading like '%شمام%'  
and sub_subject not like '%صراط%'
AND reading not like '%ترك%شمام%'
AND
ifnull(tags,',') not like '%ishmam,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'idghamn,'
where reading like '%دغام%ترك الغنة%'  
and qarees like '%خلف_عن_ حمزة%'
and ifnull(tags,',') not like '%idghamn,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'raatarkek,'
where reading like '%رقيق%الراء%'
and 
ifnull(tags,',') not like '%raatarkek,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'badal,'
where (reading like '%تثليث البدل%' or reading like '%ثلاثة البدل%')
and 
ifnull(tags,',') not like '%badal,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'lamtaghlez,'
where (reading like '%تغليظ اللام%' or reading like '%تفخيم اللام%')
and 
ifnull(tags,',') not like '%lamtaghlez,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'waqfh1,'
where (reading like '%وقف%همز%' or reading like '%همز%وقف%')
and 
qarees like '%حمزة%'
and
ifnull(tags,',') not like '%waqfh1,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'waqfh1,'
where (reading like '%وقف%همز%' or reading like '%همز%وقف%')
and 
qarees like '%هشام%'
and
ifnull(tags,',') not like '%waqfhamer,%'

