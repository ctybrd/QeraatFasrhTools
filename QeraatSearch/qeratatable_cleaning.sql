select reading,count(*)
from quran_data group by reading order by count(*) desc

-- إزالة كلمة قرأ قرؤوا
UPDATE quran_data
SET reading = 
  case WHEN reading LIKE 'قرؤوا %' THEN SUBSTR(reading, 7)
   WHEN reading like 'قرأ %'  THEN SUBSTR(reading, 5)
    ELSE reading END;
-- حذف عكس السوسي الإدغام الكبير
delete from quran_data where 
qareesrest='نافع,ابن كثير, الدوري عن أبي عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
 and reading ='بالإظهار.'
-- حذف عكس إدغام خلف بغير غنة
delete from quran_data where 
qareesrest='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, خلاد عن حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
 and reading ='بالإدغام مع الغنة.'
-- حذف عكس صلة ميم الجمع

delete from quran_data where 
qarees='باقي الرواة' 
and reading ='بترك صلة ميم الجمع.'

-- حذف عكس إمالة هاء التأنيث
delete from quran_data where 
qareesrest='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,'
and reading ='بفتح هاء التأنيث.'



-- نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,
-- أظهر اللام عند النون.

-- اختصارات بسيطة
UPDATE quran_data
SET reading = replace(reading,'حرفا مديا من جنس حركة ما قبلها','');
UPDATE quran_data
SET reading = replace(reading,'بالنقل وصلاً ووقفا','بالنقل');

UPDATE quran_data
SET reading = replace(reading,'بالنقل مع ترك السكت','بالنقل');
where qarees like '% ورش%'

UPDATE quran_data
SET reading = replace(reading,'بلا خلاف عنه', '');
UPDATE quran_data
SET reading = replace(reading,' بخلف عنه', ' بخلف');
UPDATE quran_data
SET qarees = replace(qarees,'_ ', ' ');

UPDATE quran_data
SET qarees = replace(qarees,'_',' ');

UPDATE quran_data
SET reading = replace(reading,'بتثليث مد البدل','ثلاثة البدل');
UPDATE quran_data
SET reading = replace(reading,'بتثليث البدل','ثلاثة البدل');
UPDATE quran_data
SET reading = replace(reading,'تثليث مد البدل','ثلاثة البدل');

UPDATE quran_data
SET reading = replace(reading,'  ',' ');

UPDATE quran_data
SET reading = replace(reading,'بإبدال الهمزة الساكنة .','بالإبدال')
where reading ='بإبدال الهمزة الساكنة .'

UPDATE quran_data
SET reading = replace(reading,'بالإدغام مع ترك الغنة.','بإدغام بلا غنة');


-- اختصار وقف حمزة وهشام
-- UPDATE quran_data
-- SET reading = replace(reading,' وصلاً، ووقف','وقف')
-- where qarees like '%حمزة%' or qarees like '%هشام%'



UPDATE quran_data
SET reading = replace(reading,'بتحقيق الهمزتين وصلاً، ','')
where qarees like '%حمزة%' or qarees like '%هشام%';

UPDATE quran_data
SET reading = replace(reading,'بتحقيق الهمزة وصلاً، ووقف','وقف')
where qarees like '%حمزة%' or qarees like '%هشام%';

UPDATE quran_data
SET reading = replace(reading,'بتحقيق الهمزة المتطرفة وصلاً، ووقف','وقف')
where qarees like '%حمزة%' or qarees like '%هشام%';

UPDATE quran_data
SET reading = replace(reading,'بتحقيق الهمزة وصلاً ، و','')
where qarees like '%حمزة%' or qarees like '%هشام%';


-- حذف عكس وقف حمزة
delete from quran_data where reading ='بتحقيق الهمزة وصلاً ووقفا.'
and (qareesrest ='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
or 
qarees ='باقي الرواة');
-- حذف عكس الهمزتين
delete from quran_data where reading ='بتحقيق الهمزتين وصلاً ووقفا.'
and qareesrest ='ابن عامر, عاصم, حمزة, الكسائي, روح عن يعقوب, خلف العاشر,';

delete from quran_data where reading ='بقصر مد البدل، مع فتح هاء التأنيث.'
AND qarees ='باقي الرواة';

delete from quran_data where reading ='بقصر مد البدل مع تحقيق الهمزة.'
AND qarees ='باقي الرواة';
delete from quran_data where readinG='بقصر مد البدل، مع تحقيق الهمزة، وفتح هاء التأنيث.'
AND qarees ='باقي الرواة';
delete from quran_data where readinG='بقصر مد البدل مع ترك هاء السكت.'
AND qarees ='باقي الرواة';

delete from quran_data where readinG='بترك الإمالة وصلا ووقفا.'
AND qarees ='باقي الرواة';

UPDATE quran_data
SET reading = replace(reading,'ً','')

-- حذف عكس ترقيق الراء لورش

delete from quran_data where reading ='بتفخيم الراء.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

delete from quran_data where reading ='بتفخيم الراء في الحالين.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

-- حذف عكس السكت
delete from quran_data where reading ='بترك السكت مع تحقيق الهمزة وصلاً ووقفا.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

-- حذف عكس مد البدل
delete from quran_data where reading ='بقصر مد البدل.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

-- تنظيف هاء الصلة لابن كثير
UPDATE quran_data
SET reading = replace(reading,'خلافا لجمهور القراء','')
where qarees like '%كثير%' ;

-- حذف عكس السكت
delete from quran_data where reading ='بترك السكت، وإسكان ميم الجمع وصلاً ووقفا.';
delete from quran_data where reading ='بقصر مد البدل، وبترك السكت مع تحقيق الهمزة وصلاً ووقفا.';
delete from quran_data where reading ='بقصر مد البدل، وترك السكت مع تحقيق الهمزة وصلاً ووقفا.';
delete from quran_data where reading ='بتحقيق الهمزة، وترك السكت، مع قصر مد اللين.';

delete from quran_data where reading ='بترك السكت، مع تفخيم الراء، وقصر مد البدل، وفتح هاء التأنيث.';

delete from quran_data where reading ='بتحقيق الهمزة، مع ترك السكت وصلاً ووقفا.';
delete from quran_data where reading ='بترك السكت، وإسكان ميم الجمع، مع قصر مد البدل.';

--- الغاء كلمة باقي الرواة
update quran_data set qarees='الباقون'
where 
qarees='باقي الرواة' 



--- to delete duplicates case when count_words is null then '' when count_words =2 the معا else 'جميعا' end 
-- count_words  = عدد مرات تكرار الكلمة في نفس الآية
-- sub_sno  = ترتيب الكلمة ضمن مرات تكرارها
-- وبالتالي لإخفاء التكرار يتم عرض السطور التي رقمها 1 فقط

WITH DuplicateRows AS (
    SELECT 
        aya_index,
        sub_subject,
        reading,
        qarees,
		id,
        ROW_NUMBER() OVER (PARTITION BY aya_index, sub_subject, reading, qarees ORDER BY aya_index, sub_subject, reading, qarees) AS RowNum,
		count(*) OVER (PARTITION BY aya_index, sub_subject, reading, qarees ORDER BY aya_index, sub_subject, reading, qarees) AS dupcount
    FROM 
        quran_data
)

UPDATE quran_data
 SET   count_words = dupcount,sub_sno=RowNum
FROM DuplicateRows
WHERE 
    quran_data.aya_index = DuplicateRows.aya_index
 and quran_data.id=DuplicateRows.id
	;


select sub_subject,sub_sno,
case when count_words =1 then '' when count_words =2 THEN 'معا' else 'جميعا' end as extra
  from quran_data where sub_sno=1 order by aya_index,id

SELECT distinct sub_subject,reading from quran_data where 
((reading like '%كسر%' 
) or
(reading like '% ضم%'
) or
(reading like '%فراد%'
) or
(reading like '%خطاب%'
) or
(reading like '%فتحة%'
) or
(reading like '%سكان%'
) or
(reading like '%بالياء%'
) or
(reading like '%بالتاء%'
) or
(reading like '%بتاء%'
) or
(reading like '%بياء%'
)
or
(reading like '%بنون%'
)
or
(reading like '%بالنون%'
)

)

and r5_2 is null
and readingresult is null