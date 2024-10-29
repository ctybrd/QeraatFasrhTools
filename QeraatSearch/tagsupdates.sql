UPDATE quran_data set tags=IFNULL(tags,',') ||'idghak,'
where reading like '%دغام%كبير%%'
and 
ifnull(tags,',') not like '%idghak,%';

update quran_data set done=1 where reading like '%دغام%كبير%%'
and reading <>'بالتاء مع الإدغام الكبير.';


UPDATE quran_data set tags=IFNULL(tags,',') ||'meemsela,'
where reading 
IN (
    'بصلة ميم الجمع وصلا بخلف.',
    'بصلة ميم الجمع وصلا.',
    'بصلة ميم الجمع وصلا مع الإشباع.',
    'بضم ميم الجمع، ووصلها بواو لفظية بخلف.',
    'بضم ميم الجمع، ووصلها بواو لفظية.'
)

and 
ifnull(tags,',') not like '%meemsela,%';

update quran_data set done=1 where reading 
IN (
    'بصلة ميم الجمع وصلا بخلف.',
    'بصلة ميم الجمع وصلا.',
    'بصلة ميم الجمع وصلا مع الإشباع.',
    'بضم ميم الجمع، ووصلها بواو لفظية بخلف.',
    'بضم ميم الجمع، ووصلها بواو لفظية.'
);


UPDATE quran_data set tags=IFNULL(tags,',') ||'meemsela,badal,'
where reading 
IN (
    'بضم ميم الجمع، ووصلها بواو لفظية مع الإشباع، مع ثلاثة البدل.'
)

and 
ifnull(tags,',') not like '%meemsela,%';

update quran_data set done=1 where reading 
 
IN (
    'بضم ميم الجمع، ووصلها بواو لفظية مع الإشباع، مع ثلاثة البدل.'
);


UPDATE quran_data set tags=IFNULL(tags,',') ||'idghamn,'
where reading = 'بإدغام بلا غنة'
and 
ifnull(tags,',') not like '%idghamn,%';

update quran_data set done=1 where reading = 'بإدغام بلا غنة'

UPDATE quran_data set tags=IFNULL(tags,',') ||'nakl,'
where reading = 'بالنقل.'
and 
ifnull(tags,',') not like '%nakl,%';

update quran_data set done=1 where reading = 'بالنقل.'


UPDATE quran_data set tags=IFNULL(tags,',') ||'waqfh1,'
where reading 
IN (
    'وقف بتسهيل وتحقيق الهمزة.',
    'بترك السكت وصلا، ووقف بالنقل والتحقيق.',
    'بالسكت وعدمه وصلا، ووقف بالسكت، والنقل، وتركهما.',
    'بالسكت وعدمه وصلا، ووقف بالسكت والنقل.',
   'بالسكت وصلا، ووقف بالسكت والنقل.'
);

and 
ifnull(tags,',') not like '%waqfh1,%';

update quran_data set done=1 where reading 
IN (
    'وقف بتسهيل وتحقيق الهمزة.',
    'بترك السكت وصلا، ووقف بالنقل والتحقيق.',
    'بالسكت وعدمه وصلا، ووقف بالسكت، والنقل، وتركهما.',
    'بالسكت وعدمه وصلا، ووقف بالسكت والنقل.',
    'بالسكت وصلا، ووقف بالسكت والنقل.'
    );


UPDATE quran_data SET
tags=(SELECT tags from tagsmap where tagsmap.reading=quran_data.reading),done=1
where reading in(SELECT reading from tagsmap)


UPDATE quran_data set tags='wafh1,',done=1 WHERE
reading='وقف بتسهيل وتحقيق الهمزة.' 

UPDATE  quran_data set tags= ',' || tags ||','
where tags is not null;

UPDATE  quran_data set tags= replace(tags,',,',',')
where tags is not null;


UPDATE quran_data set tags=IFNULL(tags,',') ||'waqfh1,'
where reading = 'بترك السكت وصلا، ووقف بالنقل والتحقيق.'
and 
ifnull(tags,',') not like '%waqfh1,%';

update quran_data set done=1 where reading = 'بترك السكت وصلا، ووقف بالنقل والتحقيق.';


SELECT reading,count(*),group_concat(distinct sub_subject),group_concat(distinct qarees) from 
  quran_data

where done is null

and
(
    q1 IS NOT NULL OR q2 IS NOT NULL OR q3 IS NOT NULL OR q4 IS NOT NULL OR q5 IS NOT NULL OR 
    q7 IS NOT NULL OR q8 IS NOT NULL OR q9 IS NOT NULL OR
    r1_1 IS NOT NULL OR r1_2 IS NOT NULL OR
    r2_1 IS NOT NULL OR r2_2 IS NOT NULL OR
    r3_1 IS NOT NULL OR r3_2 IS NOT NULL OR
    --r4_1 IS NOT NULL OR 
	r4_2 IS NOT NULL OR
    r5_1 IS NOT NULL OR r5_2 IS NOT NULL OR
    --r6_1 IS NOT NULL OR r6_2 IS NOT NULL OR
    r7_1 IS NOT NULL OR r7_2 IS NOT NULL OR
    r8_1 IS NOT NULL OR r8_2 IS NOT NULL OR
    r9_1 IS NOT NULL OR r9_2 IS NOT NULL OR
    r10_1 IS NOT NULL OR r10_2 IS NOT NULL
)
group by reading
ORDER by count(*) desc


UPDATE quran_data
SET resultnew = (
    SELECT a.resultnew
    FROM quran_data AS a
    WHERE a.sub_subject = quran_data.sub_subject
      AND a.reading = quran_data.reading
      AND a.resultnew IS NOT NULL
      AND a.resultnew != ''
)
WHERE (quran_data.resultnew IS NULL OR quran_data.resultnew = '')
AND EXISTS (
    SELECT 1
    FROM quran_data AS a
    WHERE a.sub_subject = quran_data.sub_subject
      AND a.reading = quran_data.reading
      AND a.resultnew IS NOT NULL
      AND a.resultnew != ''
);



--- split tags

WITH RECURSIVE tags_split(aya_index, id, sub_subject, reading, tag, remaining_tags) AS (
    SELECT aya_index, id, sub_subject, reading,
        CASE WHEN tags LIKE ',%' THEN SUBSTR(tags, 2, INSTR(tags, ',') - 1)
        ELSE SUBSTR(tags, 1, INSTR(tags, ',') - 1) END,
        CASE WHEN tags LIKE ',%' THEN SUBSTR(tags, INSTR(tags, ',') + 1)
        ELSE '' END
    FROM quran_data 
    WHERE tags IS NOT NULL AND tags NOT LIKE '%nochange%' and page_shmrly is not null
    
    UNION ALL
    
    SELECT aya_index, id, sub_subject, reading,
        CASE WHEN remaining_tags LIKE ',%' THEN SUBSTR(remaining_tags, 2, INSTR(remaining_tags, ',') - 1)
        ELSE SUBSTR(remaining_tags, 1, INSTR(remaining_tags, ',') - 1) END,
        CASE WHEN remaining_tags LIKE ',%' THEN SUBSTR(remaining_tags, INSTR(remaining_tags, ',') + 1)
        ELSE '' END
    FROM tags_split
    WHERE remaining_tags != ''
)

SELECT ts.aya_index, 
       ts.id, 
       ts.sub_subject, 
       ts.reading, 
       ts.tag, 
       tm.description,
       qd.page_shmrly  -- Add the page_shmrly column from quran_data
FROM tags_split ts
LEFT JOIN tagsmaster tm ON ts.tag = tm.tag
JOIN quran_data qd ON ts.aya_index = qd.aya_index AND ts.id = qd.id  -- Ensure the join to get page_shmrly
WHERE ts.tag != ''
ORDER BY ts.aya_index, ts.id;

select case when q7=1 then 'الكسائي' 
else case WHEN r7_2 =1 then 'الدوري عن الكسائي' 
else 'أبو الحارث عن الكسائي' 
end end   "القاريء",
aya  "آية",
sora_name  "سورة",
sub_subject,page_number2   "صفحة"
  from all_qeraat where tags like '%,imala,%' and qareesrest like '%كسائ%' 
and qareesrest not like '%خلف العاشر%'
ORDER by aya_index,id;