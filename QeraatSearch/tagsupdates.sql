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

