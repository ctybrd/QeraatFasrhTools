
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
qareesrest='باقي الرواة' 
and reading ='بترك صلة ميم الجمع.'

-- حذف عكس إمالة هاء التأنيث
delete from quran_data where 
qareesrest='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,'
and reading ='بفتح هاء التأنيث.'



-- نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,
-- أظهر اللام عند النون.



-- اختصار وقف حمزة وهشام
-- UPDATE quran_data
-- SET reading = replace(reading,' وصلاً، ووقف','وقف')
-- where qarees like '%حمزة%' or qarees like '%هشام%'

UPDATE quran_data
SET reading = replace(reading,'بتحقيق الهمزتين وصلاً، ','')
where qarees like '%حمزة%' or qarees like '%هشام%';
-- حذف عكس وقف حمزة
delete from quran_data where reading ='بتحقيق الهمزة وصلاً ووقفا.'
and (qareesrest ='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
or 
qarees ='باقي الرواة');
-- حذف عكس الهمزتين
delete from quran_data where reading ='بتحقيق الهمزتين وصلاً ووقفا.'
and qareesrest ='ابن عامر, عاصم, حمزة, الكسائي, روح عن يعقوب, خلف العاشر,';

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
delete from quran_data where reading ='بترك السكت، وإسكان ميم الجمع وصلاً ووقفا.'
delete from quran_data where reading ='بقصر مد البدل، وبترك السكت مع تحقيق الهمزة وصلاً ووقفا.'
delete from quran_data where reading ='بقصر مد البدل، وترك السكت مع تحقيق الهمزة وصلاً ووقفا.'
delete from quran_data where reading ='بتحقيق الهمزة، وترك السكت، مع قصر مد اللين.'

delete from quran_data where reading ='بترك السكت، مع تفخيم الراء، وقصر مد البدل، وفتح هاء التأنيث.'

delete from quran_data where reading ='بتحقيق الهمزة، مع ترك السكت وصلاً ووقفا.'
delete from quran_data where reading ='بترك السكت، وإسكان ميم الجمع، مع قصر مد البدل.'




--- to delete duplicates case when count_words is null then '' when count_words =2 the معا else 'جميعا' end 
-- 
WITH DuplicateRows AS (
    SELECT 
        aya_index,
        sub_subject,
        reading,
        qarees,
        ROW_NUMBER() OVER (PARTITION BY aya_index, sub_subject, reading, qarees ORDER BY aya_index,aya_index, sub_subject, reading, qarees) AS RowNum,
        COUNT(*) as  DupCount
    FROM 
        quran_data
    GROUP BY 
        aya_index, sub_subject, reading, qarees
    HAVING 
        COUNT(*) > 1
)
UPDATE quran_data
SET 
    count_words = DupCount
FROM DuplicateRows
WHERE 
    quran_data.aya_index = DuplicateRows.aya_index
    AND quran_data.sub_subject = DuplicateRows.sub_subject
    AND quran_data.reading = DuplicateRows.reading
    AND quran_data.qarees = DuplicateRows.qarees
    AND DuplicateRows.RowNum = 1;

-- delete duplicates 
WITH DuplicateRows AS (
    SELECT 
        aya_index,
        sub_subject,
        reading,
        qarees,
        ROW_NUMBER() OVER (PARTITION BY aya_index, sub_subject, reading, qarees ORDER BY aya_index,aya_index, sub_subject, reading, qarees) AS RowNum,
        COUNT(*) as  DupCount
    FROM 
        quran_data
    GROUP BY 
        aya_index, sub_subject, reading, qarees
    HAVING 
        COUNT(*) > 1
)
DELETE FROM quran_data
WHERE 
    (aya_index, sub_subject, reading, qarees) IN (
        SELECT 
            aya_index,
            sub_subject,
            reading,
            qarees
        FROM 
            DuplicateRows
        WHERE 
            RowNum > 1
    );
