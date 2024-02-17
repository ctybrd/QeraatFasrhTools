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
SET reading = replace(reading,'إبدالها حرفا مديا','الإبدال');

UPDATE quran_data
SET reading = replace(reading,'حرفا مديا من جنس حركة ما قبله','');

UPDATE quran_data
SET reading = replace(reading,'بين بين','');

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

delete from quran_data where reading ='بتحقيق الهمزة المتطرفة وصلا ووقفا.'
and
qareesrest ='نافع,ابن كثير, أبو عمرو, ابن ذكوان عن ابن عامر, عاصم, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
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
(reading like '%بضم%'
) or
(reading like '%مفتوحة%'
) or
(reading like '%مكسورة%'
) or
(reading like '%مشددة%'
) or
(reading like '%تشديد%'
) or
(reading like '%ساكنة%'
) or
(reading like '%مضمومة%'
) or
(reading like '%فراد%'
) or
(reading like '%تشديد%'
) or
(reading like '%تخفيف%'
) or
(reading like '%مخففة%'
) or
(reading like '%ممدودة%'
) or
(reading like '%زيادة%'
) or
(reading like '%إسكان%'
) or
(reading like '%بالرفع%'
) or
(reading like '%بالخفض%'
) or
(reading like '%مبنيا%'
) or
(reading like '%فاعله%'
) or
(reading like '%نون %'
) or
(reading like '%نونين %'
) or
(reading like '%الجمع%'
) or
(reading like '%توحيد%'
) or
(reading like '%تقديم%'
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
or
(reading like '%فعل%'
)
)
and (reading<>'بصلة ميم الجمع وصلا.') and 
(reading <>'بصلة ميم الجمع وصلا بخلف.')
and (reading <>'بصلة ميم الجمع وصلا مع الإشباع.')
and r5_2 is null
and readingresult is null

-- استخراج فرش حمزة لسورة
SELECT distinct sub_subject,reading from quran_data where 
((reading like '%كسر%' 
) or
(reading like '% ضم%'
) or
(reading like '%بضم%'
) or
(reading like '%مفتوحة%'
) or
(reading like '%مكسورة%'
) or
(reading like '%مشددة%'
) or
(reading like '%تشديد%'
) or
(reading like '%ساكنة%'
) or
(reading like '%مضمومة%'
) or
(reading like '%فراد%'
) or
(reading like '%تشديد%'
) or
(reading like '%تخفيف%'
) or
(reading like '%مخففة%'
) or
(reading like '%ممدودة%'
) or
(reading like '%زيادة%'
) or
(reading like '%إسكان%'
) or
(reading like '%بالرفع%'
) or
(reading like '%بالخفض%'
) or
(reading like '%مبنيا%'
) or
(reading like '%فاعله%'
) or
(reading like '%نون %'
) or
(reading like '%نونين %'
) or
(reading like '%الجمع%'
) or
(reading like '%توحيد%'
) or
(reading like '%تقديم%'
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
or
(reading like '%فعل%'
)
or
(reading like '%إشمام%'
)
)
and (reading<>'بصلة ميم الجمع وصلا.') and 
(reading <>'بصلة ميم الجمع وصلا بخلف.')
and (reading <>'بصلة ميم الجمع وصلا مع الإشباع.')
and r5_2 is null
and sora=6
and R6_1=1 and r5_2 is null




SELECT * from quran_data_tayba WHERE
((qareesrest like '%الأصبهاني%'
)
or
(qareesrest like '%ورش%'
and qareesrest not like '%أزرق%'
)
or
(qareesrest like '%نافع%'

and qareesrest not like '%قالون%'
and qareesrest not like '%أزرق%'
))

and reading <>'بالنقل، مع ترك الوقف بهاء السكت.'
and reading <>'بالنقل، مع تحقيق الهمزة المتطرفة.'
and reading <>'بالنقل، مع تفخيم الراء.'
and reading <>'بنقل حركة الهمزة، مع قصر البدل.'
and reading<>'بالنقل، مع قصر اللين.'
and reading<>'بترك هاء السكت وقفا.'
and reading<>'بترك السكت، مع تحقيق الهمزة وصلاً ووقفا.'
and reading<>'بفتح هاء التأنيث وقفا.'
and reading<>'بالفتح في الحالين.'
and reading<>'بإسكان ميم الجمع، وترك الصلة.'
and reading<>'بتحقيق الهمزة وصلاً ووقفا.'
and reading<>'ببقاء غنة النون المدَغمة بخلف.'
and reading<>'بالإظهار.'
and reading<>'بإدغام النون مع الغنة.'
and reading<>'بكسر هاء الضمير وصلاً ووقفا.'
and reading<>'بترك السكت على حروف الهجاء في فواتح السور.'
and reading<>'بالفتح وقفا.'
and reading<>'بترك السكت، مع تحقيق الهمزة.'
and reading<>'بقصر الصلة، مع ترك الإدغام.'
and reading <>'بترقيق اللام.'
and reading<>'بقصر المد في ( لا) النافية للجنس؛ لأن السبب فيها معنوي.'
and reading <>'بتحقيق الهمزة مع ترك السكت على المد وصلاً ووقفا.'
and reading <>'بتحقيق الهمزة، مع ترك السكت وصلاً ووقفا, .'
and reading <>'بتفخيم الراء.'
and reading <>'بالفتح وصلاً ووقفا.'
and reading <>'بقصر مد البدل.'
and reading <> 'بالكسرة الخالصة.'
and (sub_subject not like '%صراط%'
)
and reading <>'بتحقيق الهمزة، مع ترك السكت وصلاً ووقفا.'
and reading <>'بتحقيق الهمزة في الحالين.'
and reading <>'بتحقيق الهمزة، مع ترك السكت على المد وصلاً ووقفا.'
and reading <>'بتفخيم الراء، وترك هاء السكت.'
and reading<>'قرؤوابالفتح مع تحقيق الهمزة مع ترك السكت على المد وصلاً ووقفا.'
and reading <>'بالفتح، مع ترك هاء السكت.'
and sub_subject not in('وهو','فهو','لهو','وهو','فهي','لهي','فهي','وهي','ثم هو')
and reading <>'بتحقيق الهمزة، مع قصر مد البدل، وبلا هاء السكت.'
and reading <>'بترك الإمالة، مع قصر مد البدل.'
and readinG<>'بالفتح، مع ترك هاء السكت وقفا.'
and readinG<>'بترك الصلة مع قصر الهاء.'
and reading<>'بالفتح، مع ترك السكت على المد.'
and reading<>'بالفتح، مع تحقيق الهمزة.'
and readinG<>'بتحقيق الهمزة، مع ترك السكت، وقصر اللين.'
and readinG<>'بضم الهاء وصلاً ووقفا.'
and reading <>'بالفتح وقفاً، مع ترقيق اللام.'
order by aya_index,id