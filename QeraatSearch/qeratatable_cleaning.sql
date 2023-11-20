
select reading,count(*)
from qeraat_brief group by reading order by count(*) desc

-- إزالة كلمة قرأ قرؤوا
UPDATE qeraat_brief
SET reading = 
  case WHEN reading LIKE 'قرؤوا %' THEN SUBSTR(reading, 7)
   WHEN reading like 'قرأ %'  THEN SUBSTR(reading, 5)
    ELSE reading END;
-- حذف عكس السوسي الإدغام الكبير
delete from qeraat_brief where 
qareesrest='نافع,ابن كثير, الدوري عن أبي عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
 and reading ='بالإظهار.'
-- حذف عكس إدغام خلف بغير غنة
delete from qeraat_brief where 
qareesrest='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, خلاد عن حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
 and reading ='بالإدغام مع الغنة.'
-- حذف عكس صلة ميم الجمع

delete from qeraat_brief where 
qareesrest='باقي الرواة' 
and reading ='بترك صلة ميم الجمع.'

-- حذف عكس إمالة هاء التأنيث
delete from qeraat_brief where 
qareesrest='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,'
and reading ='بفتح هاء التأنيث.'



-- نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,
-- أظهر اللام عند النون.



-- اختصار وقف حمزة وهشام
-- UPDATE qeraat_brief
-- SET reading = replace(reading,' وصلاً، ووقف','وقف')
-- where qarees like '%حمزة%' or qarees like '%هشام%'

UPDATE qeraat_brief
SET reading = replace(reading,'بتحقيق الهمزتين وصلاً، ','')
where qarees like '%حمزة%' or qarees like '%هشام%';
-- حذف عكس وقف حمزة
delete from qeraat_brief where reading ='بتحقيق الهمزة وصلاً ووقفا.'
and (qareesrest ='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
or 
qarees ='باقي الرواة');
-- حذف عكس الهمزتين
delete from qeraat_brief where reading ='بتحقيق الهمزتين وصلاً ووقفا.'
and qareesrest ='ابن عامر, عاصم, حمزة, الكسائي, روح عن يعقوب, خلف العاشر,';

-- حذف عكس ترقيق الراء لورش

delete from qeraat_brief where reading ='بتفخيم الراء.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

delete from qeraat_brief where reading ='بتفخيم الراء في الحالين.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

-- حذف عكس السكت
delete from qeraat_brief where reading ='بترك السكت مع تحقيق الهمزة وصلاً ووقفا.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

-- حذف عكس مد البدل
delete from qeraat_brief where reading ='بقصر مد البدل.' and
qareesrest ='قالون عن نافع, ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,';

-- تنظيف هاء الصلة لابن كثير
UPDATE qeraat_brief
SET reading = replace(reading,'خلافا لجمهور القراء','')
where qarees like '%كثير%' ;