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