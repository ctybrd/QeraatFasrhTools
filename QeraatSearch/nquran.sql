-- Create the qareemaster table
CREATE TABLE qareemaster (
    id INTEGER PRIMARY KEY,
    qkey TEXT,
    name TEXT,
    groups TEXT
);

-- Insert data into the qareemaster table
INSERT INTO qareemaster (qkey, name) VALUES
    ('Q1', 'نافع'),
    ('R1_1', 'قالون عن نافع'),
    ('R1_2', 'ورش عن نافع'),
    ('Q2', 'ابن كثير'),
    ('R2_1', 'البزي عن ابن كثير'),
    ('R2_2', 'قنبل عن ابن كثير'),
    ('Q3', 'أبو عمرو'),
    ('R3_1', 'الدوري عن أبي عمرو'),
    ('R3_2', 'السوسي عن أبي عمرو'),
    ('Q4', 'ابن عامر'),
    ('R4_1', 'هشام عن ابن عامر'),
    ('R4_2', 'ابن ذكوان عن ابن عامر'),
    ('Q5', 'عاصم'),
    ('R5_1', 'شعبة عن عاصم'),
    ('R5_2', 'حفص عن عاصم'),
    ('Q6', 'حمزة'),
    ('R6_1', 'خلف عن حمزة'),
    ('R6_2', 'خلاد عن حمزة'),
    ('Q7', 'الكسائي'),
    ('R7_1', 'أبو الحارث عن الكسائي'),
    ('R7_2', 'الدوري عن الكسائي'),
    ('Q8', 'أبو جعفر'),
    ('R8_1', 'ابن وردان عن أبي جعفر'),
    ('R8_2', 'ابن جماز عن أبي جعفر'),
    ('Q9', 'يعقوب'),
    ('R9_1', 'رويس عن يعقوب'),
    ('R9_2', 'روح عن يعقوب'),
    ('Q10', 'خلف العاشر'),
    ('R10_1', 'إسحق عن خلف'),
    ('R10_2', 'إدريس عن خلف');


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

-- مثال
select * from quran_data where R1_1=1 and R5_2 is null
and reading not like '%صلة%ميم%جمع%'
and reading not like '%ميم%جمع%وصل%'
and (q8=1 or r8_1=1 or r8_2=1)
 order by aya_index,id
-- مثال
select * from quran_data where (q2=1 or r2_1=1 or r2_2=1) and page_number2=26 and ifnull(tags,'') not like '%,meemsela,%' 
and R5_2 is null

order by aya_index,id

select reading,count(*) from quran_data
where tags is null and ifnull(r5_2,0)=0
group by reading
order by count(*) desc


insert into tagsmaster(tag,description,qarees,category)
VALUES('basmala','الفصل بين السورتين',null,null);


insert into tagsmaster(tag,description,qarees,category)
VALUES('meemsela','صلة ميم الجمع وصلا','حمزة',null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('heemee','كسر الهاء والميم',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('hoomoo','ضم الهاء والميم وصلا',null,null);

	insert into tagsmaster(tag,description,qarees,category)
	VALUES('yaaend','إثبات الياء الزائدة',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('yaa','فتح ياء الإضافة',null,null);


insert into tagsmaster(tag,description,qarees,category)
VALUES('sakt2', 'السكت على الساكن قبل الهمزة',null,null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('waqfhamer','وقف هشام','حمزة',null);

insert into tagsmaster(tag,description,qarees,category)
VALUES('haasela','صلة هاء الضمير ','ابن كثير',null);


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
VALUES('leenhamz','لين مهموز',null,null);


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

UPDATE quran_data set tags=IFNULL(tags,',') ||'imalah,'
where reading like '%مالة%'
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
where (reading like '%تثليث البدل%' or reading like '%ثلاثة البدل%'  or reading like '%تثليث%بدل%'  )
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

UPDATE quran_data set tags=IFNULL(tags,',') ||'haasela,'
where (reading like '%صلة%هاء%')
and 
qarees like '%كثير%'
and
ifnull(tags,',') not like '%haasela,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'nakl,'
where (reading like '%نقل%')
and 
qarees like '%ورش%'
and
ifnull(tags,',') not like '%nakl,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'leenhamz,'
where (reading like '%شباع%اللين%')
and 
qarees like '%ورش%'
and
ifnull(tags,',') not like '%leenhamz,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'ibdal,'
where (reading like '%إبدال%همز%')
and 
qarees not like '%حمز%' and qarees not like '%هشام%'
and
ifnull(tags,',') not like '%ibdal,%'



UPDATE quran_data set tags=IFNULL(tags,',') ||'sakt2,'
where reading like '%سكت%' 
and 
qarees like '%حمزة%'
and
ifnull(tags,',') not like '%sakt2,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'haasakt,'
where reading like '%هاء%سكت%' 
and 
qarees like '%يعقوب%'
and
ifnull(tags,',') not like '%haasakt,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'haadam,'
where reading like '%ضم%هاء%ضمي%' 
and
ifnull(tags,',') not like '%haadam,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'haasokon,'
where reading like '%قرأ بإسكان الهاء، مع ترك الوقف بهاء السكت.%' 
and
ifnull(tags,',') not like '%haasokon,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'heemee,'
where reading like '%قرأ بكسر الهاء والميم وصلاً، وبكسر الهاء وإسكان الميم وقفا.%' 
and
ifnull(tags,',') not like '%heemee,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'hoomoo,'
where reading like '%قرأ بضم الهاء والميم وصلاً، %' 
and
ifnull(tags,',') not like '%hoomoo,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'`,'
where reading like '%ثبات%الياء الزائدة%' 
and
ifnull(tags,',') not like '%yaaend,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'yaafath,'
where reading like '%قرأ بفتح ياء الإضافة.%' 
and
ifnull(tags,',') not like '%yaafath,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'meemsela,'
where reading like '%قرأ بضم ميم الجمع، ووصلها بواو لفظية.%' 
and
ifnull(tags,',') not like '%meemsela,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'meemsela,'
where reading like '%قرأ بضم ميم الجمع، ووصلها بواو لفظية بخلف عنه.%' 
and
ifnull(tags,',') not like '%meemsela,%'


UPDATE quran_data set tags=IFNULL(tags,',') ||'basmala,'
where reading like '%سورتين%' 
and
ifnull(tags,',') not like '%basmala,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'idgham,'
where reading like '%دغام%' 
and
ifnull(tags,',') not like '%idgham,%'

UPDATE quran_data set tags=IFNULL(tags,',') ||'idgham,'
where reading like '%دغم%' 
and
ifnull(tags,',') not like '%idgham,%





SELECT 
	CASE WHEN Q1 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q1') || ','  else '' end ||
	CASE WHEN R1_1 IS NOT NULL AND Q1 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R1_1') || ', '  else '' end || 
	CASE WHEN R1_2 IS NOT NULL AND Q1 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R1_2') || ', '  else '' end ||
	CASE WHEN Q2 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q2') || ', '  else '' end ||
	CASE WHEN R2_1 IS NOT NULL AND Q2 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R2_1') || ', '  else '' end ||
	CASE WHEN R2_2 IS NOT NULL AND Q2 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R2_2') || ', '  else '' end ||
	CASE WHEN Q3 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q3') || ', '  else '' end ||
	CASE WHEN R3_1 IS NOT NULL AND Q3 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R3_1') || ', '  else '' end ||
	CASE WHEN R3_2 IS NOT NULL AND Q3 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R3_2') || ', '  else '' end ||
	CASE WHEN Q4 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q4') || ', '  else '' end ||
	CASE WHEN R4_1 IS NOT NULL AND Q4 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R4_1') || ', '  else '' end ||
	CASE WHEN R4_2 IS NOT NULL AND Q4 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R4_2') || ', '  else '' end ||
	CASE WHEN Q5 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q5') || ', '  else '' end ||
	CASE WHEN R5_1 IS NOT NULL AND Q5 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R5_1') || ', '  else '' end ||
	CASE WHEN R5_2 IS NOT NULL AND Q5 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R5_2') || ', '  else '' end ||
	CASE WHEN Q6 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q6') || ', '  else '' end ||
	CASE WHEN R6_1 IS NOT NULL AND Q6 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R6_1') || ', '  else '' end ||
	CASE WHEN R6_2 IS NOT NULL AND Q6 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R6_2') || ', '  else '' end ||
	CASE WHEN Q7 IS NOT NULL   THEN (SELECT name FROM qareemaster WHERE qkey = 'Q7') || ', '  else '' end ||
	CASE WHEN R7_1 IS NOT NULL AND Q7 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R7_1') || ', '  else '' end ||
	CASE WHEN R7_2 IS NOT NULL AND Q7 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R7_2') || ', '  else '' end ||
	CASE WHEN Q8 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q8') || ', '  else '' end ||
	CASE WHEN R8_1 IS NOT NULL AND Q8 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R8_1') || ', '  else '' end ||
	CASE WHEN R8_2 IS NOT NULL AND Q8 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R8_2') || ', '  else '' end ||
	CASE WHEN Q9 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q9') || ', '  else '' end ||
	CASE WHEN R9_1 IS NOT NULL AND Q9 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R9_1') || ', '  else '' end ||
	CASE WHEN R9_2 IS NOT NULL AND Q9 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R9_2') || ', '  else '' end ||
	CASE WHEN Q10 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q10') || ', '  else '' end ||
	CASE WHEN R10_1 IS NOT NULL AND Q10 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R10_1') || ', '  else '' end ||
	CASE WHEN R10_2 IS NOT NULL AND Q10 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R10_2') || ', '  else '' end 
as all_qa,qarees,*

FROM quran_data;


update quran_data set qareesrest = 	CASE WHEN Q1 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q1') || ','  else '' end ||
	CASE WHEN R1_1 IS NOT NULL AND Q1 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R1_1') || ', '  else '' end || 
	CASE WHEN R1_2 IS NOT NULL AND Q1 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R1_2') || ', '  else '' end ||
	CASE WHEN Q2 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q2') || ', '  else '' end ||
	CASE WHEN R2_1 IS NOT NULL AND Q2 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R2_1') || ', '  else '' end ||
	CASE WHEN R2_2 IS NOT NULL AND Q2 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R2_2') || ', '  else '' end ||
	CASE WHEN Q3 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q3') || ', '  else '' end ||
	CASE WHEN R3_1 IS NOT NULL AND Q3 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R3_1') || ', '  else '' end ||
	CASE WHEN R3_2 IS NOT NULL AND Q3 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R3_2') || ', '  else '' end ||
	CASE WHEN Q4 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q4') || ', '  else '' end ||
	CASE WHEN R4_1 IS NOT NULL AND Q4 IS NULL  THEN (SELECT name FROM qareemaster WHERE qkey = 'R4_1') || ', '  else '' end ||
	CASE WHEN R4_2 IS NOT NULL AND Q4 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R4_2') || ', '  else '' end ||
	CASE WHEN Q5 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q5') || ', '  else '' end ||
	CASE WHEN R5_1 IS NOT NULL AND Q5 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R5_1') || ', '  else '' end ||
	CASE WHEN R5_2 IS NOT NULL AND Q5 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R5_2') || ', '  else '' end ||
	CASE WHEN Q6 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q6') || ', '  else '' end ||
	CASE WHEN R6_1 IS NOT NULL AND Q6 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R6_1') || ', '  else '' end ||
	CASE WHEN R6_2 IS NOT NULL AND Q6 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R6_2') || ', '  else '' end ||
	CASE WHEN Q7 IS NOT NULL   THEN (SELECT name FROM qareemaster WHERE qkey = 'Q7') || ', '  else '' end ||
	CASE WHEN R7_1 IS NOT NULL AND Q7 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R7_1') || ', '  else '' end ||
	CASE WHEN R7_2 IS NOT NULL AND Q7 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R7_2') || ', '  else '' end ||
	CASE WHEN Q8 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q8') || ', '  else '' end ||
	CASE WHEN R8_1 IS NOT NULL AND Q8 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R8_1') || ', '  else '' end ||
	CASE WHEN R8_2 IS NOT NULL AND Q8 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R8_2') || ', '  else '' end ||
	CASE WHEN Q9 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q9') || ', '  else '' end ||
	CASE WHEN R9_1 IS NOT NULL AND Q9 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R9_1') || ', '  else '' end ||
	CASE WHEN R9_2 IS NOT NULL AND Q9 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R9_2') || ', '  else '' end ||
	CASE WHEN Q10 IS NOT NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'Q10') || ', '  else '' end ||
	CASE WHEN R10_1 IS NOT NULL AND Q10 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R10_1') || ', '  else '' end ||
	CASE WHEN R10_2 IS NOT NULL AND Q10 IS NULL THEN (SELECT name FROM qareemaster WHERE qkey = 'R10_2') || ', '  else '' end


-- إمالة حمزة
select page_number2,sora,aya,sub_subject,reading from quran_data where (q6=1 or R6_1=1 or R6_2=1) and (reading  like '%مالة%' or
reading like '%أمال%'
or
reading like '%تقليل%'
or reading like '%قلل%'
)
and reading not like '%ترك الإمالة%'
order by aya_index,id



-- وقف حمزة
-- Create Waqf_Types table if it doesn't exist
CREATE TABLE IF NOT EXISTS Waqf_Types (
    id INTEGER PRIMARY KEY,
    waqf TEXT
);

-- Insert data into Waqf_Types table from the query
INSERT INTO Waqf_Types (waqf)
SELECT DISTINCT SUBSTR(reading, INSTR(reading, 'وقف ب')) AS group_part
FROM all_qeraat
WHERE QAREES LIKE '%حمزة%' AND reading LIKE '%وقف ب%'
GROUP BY group_part;



SELECT
    qd.page_number2,
    wt.waqf AS waqf,
    GROUP_CONCAT('(' || qd.aya || ',' || qd.sub_subject || ')') AS aya_and_sub_subject
FROM
    quran_data qd
 JOIN
    Waqf_Types wt ON 
	SUBSTR(qd.reading,INSTR(qd.reading, 
	'وقف ب'
	)) = wt.waqf
WHERE qd.qarees like '%حمزة%'
GROUP BY
    qd.page_number2,wt.waqf ;


SELECT
    qd.page_number2,qd.sora,
	qd.aya,qd.qarees,
    wt.waqf AS waqf,
    GROUP_CONCAT('(' || qd.aya || ',' || qd.sub_subject || ')') AS aya_and_sub_subject
FROM
    quran_data qd
 JOIN
    Waqf_Types wt ON 
	SUBSTR(qd.reading,INSTR(qd.reading, 
	'وقف ب'
	)) = wt.waqf
WHERE qd.qarees like '%حمزة%'
GROUP BY
    qd.page_number2,qd.sora,qd.aya,wt.waqf 
order by qd.page_number2,qd.sora,
	qd.aya,qd.qarees desc,
    wt.waqf;

-- فرش حمزة للمراجعة
select page_number2,sora,aya,sub_subject,reading,Q6,r6_1,r6_2 from all_qeraat where qareesrest like '%حمزة%' 
AND
R5_2 is NULL
and reading not like '%ترك%غنة%'
and ifnull(tags,'') not like '%basmala%'
and ifnull(tags,'') not like '%sakt%'
and ifnull(tags,'') not like '%imalah%'
and ifnull(tags,'') not like '%haadam%'
and ifnull(tags,'') not like '%waqf%'
and ifnull(tags,'') not like '%hoomo%'

and sub_subject not like '%صراط%'
order by aya_index,id



-- create book for quran holder

SELECT
  aya_index,
  GROUP_CONCAT('<b>' || sub_subject || '</b> : ' ||
    CASE
      WHEN q6 IS NOT NULL THEN ' '
      ELSE
        CASE
          WHEN r6_1 IS NOT NULL THEN 'خلف '
          ELSE 'خلاد '
        END
    END || REPLACE(REPLACE(REPLACE(REPLACE(reading, 'قرأ ', ''), 'قرؤوا ', ''), 'بلا خلاف عنه', ''), 'حرفا مديا من جنس حركة ما قبلها', '')) AS text
FROM
  ALL_qeraat
WHERE
  qareesrest LIKE '%حمزة%'
  AND IFNULL(r5_2, 0) = 0
    AND IFNULL(tags, '') NOT LIKE '%basmala%'
GROUP BY
  aya_index
ORDER BY
  aya_index;




SELECT
  aya_index,
  GROUP_CONCAT('<b>' || sub_subject || '</b> : ' ||
   REPLACE(REPLACE(REPLACE(REPLACE(reading, 'قرأ ', ''), 'قرؤوا ', ''), 'بلا خلاف عنه', ''), 
   'حرفا مديا من جنس حركة ما قبلها', '')) AS text
FROM
  ALL_qeraat
WHERE
  R1_2 IS NOT NULL
  AND IFNULL(r5_2, 0) = 0
  AND IFNULL(tags, '') NOT LIKE '%basmala%'
GROUP BY
  aya_index
ORDER BY
  aya_index;



CREATE VIEW shmrly_all as select *, (select text from book_quran where aya_index = mosshf_shmrly.aya_index) aya_text, (select text_full from book_quran where aya_index = mosshf_shmrly.aya_index) aya_text_full, (select text from book_qortoby where aya_index = mosshf_shmrly.aya_index) qortoby, (select text from book_e3rab where aya_index = mosshf_shmrly.aya_index) e3rab, (select text from book_katheer where aya_index = mosshf_shmrly.aya_index) katheer, (select text from book_moyassar where aya_index = mosshf_shmrly.aya_index) moyassar, (select text from book_sa3dy where aya_index = mosshf_shmrly.aya_index) sa3dy, (select text from book_tabary where aya_index = mosshf_shmrly.aya_index) tabary, (select text from book_baghawy where aya_index = mosshf_shmrly.aya_index) baghawy, (select text from book_m3any where aya_index = mosshf_shmrly.aya_index) m3any, (select text from book_tanweer where aya_index = mosshf_shmrly.aya_index) tanweer, (select text from book_english where aya_index = mosshf_shmrly.aya_index) english , (select text from book_nozol where aya_index = mosshf_shmrly.aya_index) nozol , (select text from book_waseet where aya_index = mosshf_shmrly.aya_index) waseet , (select text from book_mokhtsr where aya_index = mosshf_shmrly.aya_index) mokhtsr, (select text from book_jlalin where aya_index = mosshf_shmrly.aya_index) jlalin,
(select text from book_tayseer10 where aya_index = mosshf_shmrly.aya_index) tayseer10
,(select text from book_qwarsh where aya_index = mosshf_shmrly.aya_index) qwarsh
,(select text from book_qhamza where aya_index = mosshf_shmrly.aya_index) qhamza
 from mosshf_shmrly


 CREATE VIEW madina_all as select *, (select text from book_quran where aya_index = mosshf_madina.aya_index) aya_text, (select text_full from book_quran where aya_index = mosshf_madina.aya_index) aya_text_full, (select text from book_qortoby where aya_index = mosshf_madina.aya_index) qortoby, (select text from book_e3rab where aya_index = mosshf_madina.aya_index) e3rab, (select text from book_katheer where aya_index = mosshf_madina.aya_index) katheer, (select text from book_moyassar where aya_index = mosshf_madina.aya_index) moyassar, (select text from book_sa3dy where aya_index = mosshf_madina.aya_index) sa3dy, (select text from book_tabary where aya_index = mosshf_madina.aya_index) tabary, (select text from book_baghawy where aya_index = mosshf_madina.aya_index) baghawy, (select text from book_m3any where aya_index = mosshf_madina.aya_index) m3any, (select text from book_tanweer where aya_index = mosshf_madina.aya_index) tanweer, (select text from book_english where aya_index = mosshf_madina.aya_index) english , (select text from book_nozol where aya_index = mosshf_madina.aya_index) nozol,
(select text from book_waseet where aya_index = mosshf_madina.aya_index) waseet, (select text from book_mokhtsr where aya_index = mosshf_madina.aya_index) mokhtsr, (select text from book_jlalin where aya_index = mosshf_madina.aya_index) jlalin ,(select text from book_tayseer10 where aya_index = mosshf_madina.aya_index) tayseer10
,(select text from book_qwarsh where aya_index = mosshf_madina.aya_index) qwarsh
,(select text from book_qhamza where aya_index = mosshf_madina.aya_index) qhamza from mosshf_madina



-- تقطيع الكلمات النتيجة بناء على وجود التشكيل
UPDATE quran_data
SET readingresult = TRIM(
    SUBSTR(
        reading,
        INSTR(reading, '(') + 1,
        INSTR(reading, ')') - INSTR(reading, '(') - 1
    )
)
WHERE reading LIKE '%(%َ%)%' OR
      reading LIKE '%(%ُ%)%' OR
      reading LIKE '%(%ِ%)%' OR
      reading LIKE '%(%ْ%)%' OR
      reading LIKE '%(%ّ%)%';


UPDATE quran_data
SET readingresult = TRIM(
    SUBSTR(
        reading,
        INSTR(reading, '(') + 1,
        INSTR(reading, ')') - INSTR(reading, '(') - 1
    )
)
WHERE (reading LIKE 'قرؤوا (%' 
OR reading LIKE 'قرأ (%');


select reading ,readingresult from quran_data 
where readingresult is not null


-- استخراج وقف حمزة نهايات الآيات
-- استخراج وقف حمزة نهايات الآيات
SELECT rawword,surah as sora,ayah as aya from words 
where wordindex in(select max(wordindex) from words group by surah,ayah)

and( rawword like '%أ%'
or
rawword like '%إ%'
or
rawword like '%ؤ%'
or 
rawword like '%ء%'
or
rawword like '%ئ%'
or
rawword like '%آ%'
)

select sora,aya,page_number2,sub_subject,reading from quran_data
 
where qareesrest like '%حمزة%' 
AND
 exists (select 1 from hamzaend where hamzaend.sora=quran_data.sora and 
hamzaend.aya=quran_data.aya and quran_data.sub_subject like '%' || hamzaend.rawword ||'%' ) 

order by 
aya_index,id

#الإدغام الكبير للسوسي
SELECT sora_name, aya, text_full, sub_subject, qareesrest, reading, sora FROM all_qeraat WHERE qareesrest LIKE '%سوسي%'  
AND reading like '%غام%كبير%'
order by aya_index,id

#الهمز من الهمزات
SELECT sora_name, aya, text_full, sub_subject, qareesrest, reading, sora FROM all_qeraat 
WHERE  ((reading like '%همز%الأولى%') or (reading like '%همز%الثانية') or (reading like '%همزت%')
) and (reading like '% %')

order by aya_index,id