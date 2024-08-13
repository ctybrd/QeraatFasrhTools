UPDATE MadinaWordsXY set realsora =
(select soramap.realsora from soramap where soramap.sora=MadinaWordsXY.surahNo);

UPDATE MadinaWordsXY SET realAya =
 (SELECT ayamap.mappedNumber    FROM ayamap
    WHERE ayamap.ayahNo = MadinaWordsXY.ayahNo )WHERE EXISTS (SELECT 1   FROM ayamap    WHERE ayamap.ayahNo = MadinaWordsXY.ayahNo);

UPDATE  MadinaWordsXY set realaya=ayahNo where realaya is null;

UPDATE MadinaWordsXY SET realPageNo = 
mosshf_madina.page_number FROM mosshf_madina
WHERE mosshf_madina.aya_number = MadinaWordsXY.realAya
  AND mosshf_madina.sora_number = MadinaWordsXY.realsora;

UPDATE MadinaWordsXY set realPageNo=(SELECT pagemap.realPageNo from pagemap
where pagemap.pageNo=MadinaWordsXY.pageNo)
where MadinaWordsXY.realpageno is NULL;

WITH countwords AS (
  SELECT surah,ayah, count(*) AS countword
  FROM words1
  GROUP BY surah,ayah
)
UPDATE MadinaWordsXY
SET realwordcountA = (
  SELECT ma.countword
  FROM countwords ma
  WHERE ma.surah = MadinaWordsXY.realsora and ma.ayah = MadinaWordsXY.realAya
);

WITH countwords AS (
  SELECT surahNo,ayahNo, count(*) AS countword
  FROM MadinaWordsXY where wordNo>0
  GROUP BY surahNo,ayahNo
)
UPDATE MadinaWordsXY
SET wordcountA = (
  SELECT ma.countword
  FROM countwords ma
  WHERE ma.surahNo = MadinaWordsXY.surahNo and  ma.ayahNo = MadinaWordsXY.ayahNo
);

WITH countwords AS (
  SELECT surah, count(*) AS countword
  FROM words1
  GROUP BY surah
)
UPDATE MadinaWordsXY
SET realwordcount = (
  SELECT ma.countword
  FROM countwords ma
  WHERE ma.surah = MadinaWordsXY.realsora
);

WITH countwords AS (
  SELECT surahNo, count(*) AS countword
  FROM MadinaWordsXY where wordNo>0
  GROUP BY surahNo
)
UPDATE MadinaWordsXY
SET wordcount = (
  SELECT ma.countword
  FROM countwords ma
  WHERE ma.surahNo = MadinaWordsXY.surahNo 
);

CREATE TABLE pagemap AS
SELECT DISTINCT pageno, realPageNo
FROM MadinaWordsXY
WHERE realPageNo IS NOT NULL
ORDER BY realPageNo;


update MadinaWordsXY set width=(abs(x1-x2))/100;
update MadinaWordsXY set x=(abs(x2)/100) ;
update MadinaWordsXY set y=((y2-.1*(reallineno))/166)+.001*(15-reallineno);

-- Create indexes if they do not already exist
CREATE INDEX idx_words1 ON words1(ayah, surah, wordsno);
CREATE INDEX idx_madina_wordsxy ON MadinaWordsXY(Aya, sora, wordsno);

-- Update the MadinaWordsXY table using a JOIN
UPDATE MadinaWordsXY
SET word = (
    SELECT words1.word
    FROM words1
    WHERE words1.ayah = MadinaWordsXY.Aya
      AND words1.surah = MadinaWordsXY.sora
      AND words1.wordsno = MadinaWordsXY.wordsno
)
WHERE EXISTS (
    SELECT 1
    FROM words1
    WHERE words1.ayah = MadinaWordsXY.Aya
      AND words1.surah = MadinaWordsXY.sora
      AND words1.wordsno = MadinaWordsXY.wordsno
);

UPDATE MadinaWordsXY
SET rawword = (
    SELECT words1.rawword
    FROM words1
    WHERE words1.ayah = MadinaWordsXY.Aya
      AND words1.surah = MadinaWordsXY.sora
      AND words1.wordsno = MadinaWordsXY.wordsno
)
WHERE EXISTS (
    SELECT 1
    FROM words1
    WHERE words1.ayah = MadinaWordsXY.Aya
      AND words1.surah = MadinaWordsXY.sora
      AND words1.wordsno = MadinaWordsXY.wordsno
);

WITH NextWordCTE AS (
  SELECT
    Sora,
    Aya,
    wordSNo,
    rawword,
    LEAD(rawword) OVER (ORDER BY Sora, Aya, wordSNo) AS nxtword
  FROM MadinaWordsXY
  WHERE wordSNo <> 0
)
UPDATE MadinaWordsXY
SET nxtword = rawword || ' '|| (SELECT nxtword FROM NextWordCTE WHERE MadinaWordsXY.Sora = NextWordCTE.Sora AND MadinaWordsXY.Aya = NextWordCTE.Aya AND MadinaWordsXY.wordSNo = NextWordCTE.wordSNo)
WHERE wordSNo <> 0;

select * FROM MadinaWordsXY where wordsno<>0 order by sora,aya,wordsno;

-- farsh
delete from madina where qaree='B';
insert into madina(qaree,page_number,color,x,y,width,style,circle)
select 'B',realPageNo,case when wordno  % 2 = 1 then 'red' else 'blue' end,x,y,width,'S','' 
from WordCoordinate where realaya=48;
UPDATE WordCoordinate 
SET realPageNo = mosshf_madina.page_number
FROM mosshf_madina
WHERE mosshf_madina.aya_number = WordCoordinate.realAya
  AND mosshf_madina.sora_number = WordCoordinate.realsora
  and WordCoordinate.realaya in(47,48);


UPDATE quran_data
SET wordsno = (
    SELECT MIN(xy.wordsno)
    FROM MadinaWordsXY xy
    WHERE quran_data.sub_subject = CASE 
                                   WHEN instr(quran_data.sub_subject, ' ') = 0 THEN xy.rawword 
                                   ELSE xy.nxtword 
                                   END
    AND xy.aya = quran_data.aya 
    AND xy.sora = quran_data.sora
);
-- revised version
UPDATE quran_data
SET wordsno = (
    SELECT ranked_xy.wordsno
    FROM (
        SELECT xy.wordsno,
               ROW_NUMBER() OVER (ORDER BY xy.wordsno) as rn
        FROM MadinaWordsXY xy
        WHERE quran_data.sub_subject = CASE 
                                       WHEN instr(quran_data.sub_subject, ' ') = 0 THEN xy.rawword 
                                       ELSE xy.nxtword 
                                       END
        AND xy.aya = quran_data.aya 
        AND xy.sora = quran_data.sora
    ) ranked_xy
    WHERE ranked_xy.rn = quran_data.sub_sno
);

UPDATE quran_data
SET wordsno = (
    SELECT ranked_xy.wordsno
    FROM (
        SELECT xy.wordsno,
               ROW_NUMBER() OVER (ORDER BY xy.wordsno) as rn
        FROM MadinaWordsXY xy
        WHERE 
            (replace(quran_data.sub_subject, ' ', '') = replace(xy.rawword, ' ', ''))
            OR
            (replace(quran_data.sub_subject, ' ', '') = replace(xy.nxtword, ' ', ''))
        AND xy.aya = quran_data.aya 
        AND xy.sora = quran_data.sora
    ) ranked_xy
    WHERE ranked_xy.rn = quran_data.sub_sno
)
WHERE wordsno is null;

UPDATE quran_data
SET wordsno = (
    SELECT MIN(xy.wordsno)
    FROM MadinaWordsXY xy
    WHERE 
			(replace(quran_data.sub_subject,' ','')=replace(xy.rawword,' ',''))
			or
			(replace(quran_data.sub_subject,' ','')=replace(xy.nxtword,' ',''))
			
    AND xy.aya = quran_data.aya 
    AND xy.sora = quran_data.sora
)
where wordsno is null
;

UPDATE quran_data
SET x = (
    SELECT x
    FROM MadinaWordsXY xy
    WHERE xy.wordsno=quran_data.wordsno
    AND xy.aya = quran_data.aya 
    AND xy.sora = quran_data.sora
);

UPDATE quran_data
SET y = (
    SELECT y
    FROM MadinaWordsXY xy
    WHERE xy.wordsno=quran_data.wordsno
    AND xy.aya = quran_data.aya 
    AND xy.sora = quran_data.sora
);

UPDATE quran_data
SET width = (
    SELECT width
    FROM MadinaWordsXY xy
    WHERE xy.wordsno=quran_data.wordsno
    AND xy.aya = quran_data.aya 
    AND xy.sora = quran_data.sora
);

SELECT * from quran_data where x is null and sub_subject not like '% بسم%';

-- أول تجربة ابن كثير
delete from madina_temp where qaree='B';

insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'B',page_number1,
case when reading like '%بصلة هاء الضمير%' 
then '#32cd32' else 
case when sub_subject like '%صراط%' then
  '#00FFFF'
else
  case when reading like '%وقف بهاء السكت%' then '#FF6820'
  else
  '#ff0000'
end end
end ,x,y,width,'S',CASE WHEN  R2_1=1 and R2_2 is null then '1' ELSE
case WHEN  R2_2=1 and R2_1 is null then '2' else '' END END
from quran_data where 
            (R2_1 IS NOT NULL or R2_2 IS NOT NULL) AND
             (IFNULL(r5_2, 0) = 0) and
             (reading <> 'بصلة ميم الجمع وصلا.'
			 )
       and 
       (reading <>'بضم ميم الجمع، ووصلها بواو لفظية.');

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
update madina_temp set width= width/2 where qaree='B' and color='#32cd32';
update madina_temp set width= width-.01 where qaree='B' and color<>'#32cd32';

-- in the farsh db
delete from madina where qaree='B';
insert into madina select * from madina_temp;


select sora,aya,sub_subject,reading,r2_1,r2_2,page_number1,count(*)
from quran_data where 
            (R2_1 IS NOT NULL or R2_2 IS NOT NULL) AND
             (IFNULL(r5_2, 0) = 0) and
             (reading <> 'بصلة ميم الجمع وصلا.'
			 )
       and 
       (reading <>'بضم ميم الجمع، ووصلها بواو لفظية.')
	   group by sora,aya,sub_subject,reading,r2_1,r2_2,page_number1
	  having count(*)>1
	  ORDER by sora,aya
	 ;

   -- ورش
   -- اللين المهموز
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#FF00FF'
 ,x+width/4,y,width/2,'S', ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%توسط%إشباع%'
and reading like '%اللين%')
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
-- تغليظ اللام
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#800080'
 ,x+width/4,y,width/2,case when reading like '%بخلف%' or reading like '%ترقيق%' then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%تغليظ%')
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

-- ترقيق الراء
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#FF8C00'
 ,x,y-0.002,width/3,case when reading like '%بخلف%'  then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like  '%ترقيق%الراء%')
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

-- صلة ميم الجمع
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#808000'
 ,x,y-0.002,0.05,case when reading like '%بخلف%'  then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like  '%ميم الجمع%')
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

-- الإبدال
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#32CD32'
 ,x,y,width,case when reading like '%بخلف%'  then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading ='بالإبدال' or reading like '%إبدال الهمزة%' or reading like '%مع إبدال%')
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

-- نقل
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#007FFF'
 ,case when sub_subject like '% %' then x else x+width-0.06 end ,y,0.05,case when reading like '%بخلف%'  then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%نقل%'
and reading not like '%نقلب%'
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

-- البدل
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#FF78FF'
 ,x+(width/2.0)-0.025,y-0.003,0.05,case when reading like '%بخلف%'  then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%ثلاثة%البدل%'
or reading like '%تثليث%'
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

-- التقليل بخلف 
--40E0D0

delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#40E0D0'
 ,x,y,0.05,case when reading like 
 '%بخلف%'  
 then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%تقليل%بخلف%'
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

-- تقليل
--00FFFF
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'A',page_number1,'#00FFFF'
 ,x,y,0.05,case when reading like 
 '%بخلف%'  
 then 'D' else 'S' end, ''
from quran_data where 
            (R1_2 IS NOT NULL ) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%تقليل%' 
and reading not like '%تقليل بخلف%'
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;

--- فرق الأصبهاني عن الشاطبية
SELECT w.sora,w.aya,w.page_number1,w.sub_subject,w.reading
FROM Asbahani W 
LEFT JOIN quran_data A 
ON A.sub_subject = W.sub_subject 
AND A.aya_index = W.aya_index 
AND A.r5_2 IS NULL 
AND A.r1_2 IS NOT NULL
WHERE A.sub_subject IS NULL
order by w.aya_index

--تذكر التوراة
SELECT a.sora,a.aya,a.page_number1,a.sub_subject,a.reading
FROM quran_data A
WHERE NOT EXISTS (
    SELECT 1 
    FROM asbahanitable W
    WHERE A.sub_subject = W.sub_subject 
      AND A.aya_index = W.aya_index
)
AND A.r5_2 IS NULL 
AND A.r1_2 IS NOT NULL
AND NOT (
    A.reading LIKE '%تقليل%' 
    OR A.reading LIKE '%ثلاثة%البدل%' 
    OR A.reading LIKE '%تثليث%' 
    OR A.reading LIKE '%ترقيق%الراء%' 
    OR A.reading LIKE '%تغليظ%' 
    OR (
        A.reading LIKE '%توسط%إشباع%' 
        AND A.reading LIKE '%اللين%'
    )
	or A.reading like '%السورتين%'
	or a.reading like '%ترقيقها%'
);

--- قراءة حمزة

delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#ff9900'
 ,x,y,0.05,case when reading like 
 '%بخلف%'  
 then 'D' else 'S' end, ''
from quran_data where 
            ((R6_1 IS NOT NULL ) or (R6_2 IS NOT NULL )) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%تقليل%' 
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;



delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#800080'
 ,x,y,0.05, 'S', '4'
from quran_data where 
  ((R6_1 IS NOT NULL ) and (R6_2 IS NULL )) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%غنة%' 
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
-- الإمالة
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#00ffff'
 , CASE WHEN substr(sub_subject, -1) = 'ى' or substr(sub_subject, -1) = 'ا'  THEN x  ELSE x + width/ 2   END AS x_value,y+0.005,0.05,'S', '4'
from quran_data where 
            ((R6_1 IS NOT NULL ) or (R6_2 IS NOT NULL )) AND
             (IFNULL(r5_2, 0) = 0) and
(reading like '%إمال%' or reading like '%أمال%'
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
-- ضم الهاء وصلا

delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#0000ff',x+0.04,y-0.04,0.05,'H', '4'
from quran_data where 
            ((R6_1 IS NOT NULL ) or (R6_2 IS NOT NULL )) AND
             (IFNULL(r5_2, 0) = 0) and
(reading  ='بضم الهاء والميم وصلا، وبكسر الهاء وإسكان الميم وقفا.'
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;


-- عليهم
delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#0000ff',x+0.04,y-0.04,0.05,'S', '4'
from quran_data where 
            ((R6_1 IS NOT NULL ) or (R6_2 IS NOT NULL )) AND
             (IFNULL(r5_2, 0) = 0) AND 
reading  !='بضم الهاء والميم وصلا، وبكسر الهاء وإسكان الميم وقفا.'
AND
sub_subject not like '% %' AND 
(sub_subject like '%عليهم%'
or sub_subject  like '%إليهم%'
or sub_subject like '%لديهم%'

)

order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;


-- ادغام إدغام
-- وضعت شرطا أن يكون قد وافق قارئاآخر لأستبعد ما يخص وقف حمزة وهشام والاقتصار على الادغام فقط

delete from madina_temp;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#0000ff',case when sub_subject like '% %' then  x-width/2  else x end,y,width,'S',CASE WHEN  R6_1=1 and R6_2 is null then '1' ELSE
case WHEN  R6_2=1 and R6_1 is null then '2' else '' END END as circle
from quran_data where 
            (R6_1 IS NOT NULL or R6_2 IS NOT NULL) AND
             (IFNULL(r5_2, 0) = 0) and
             (reading <> 'بإدغام بلا غنة')
			 and
             ((reading like '%دغام%')
			 or
			 (reading like '%دغم%')
			 )
	AND
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
			 ORDER by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
update madina_temp set x= 0.0 where x<0.0;

-- وقف حمزة
delete from madina_temp;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#808000',x,y+0.005,width,'S','' circle
from quran_data where 
             (IFNULL(r5_2, 0) = 0) and
R6_1 is not null
AND
 exists (select 1 from hamzaend where hamzaend.sora=quran_data.sora and 
hamzaend.aya=quran_data.aya and quran_data.sub_subject =  hamzaend.rawword  );
update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
update madina_temp set x= 0.0 where x<0.0;

-- فرش حمزة
delete from madina_temp;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number1,'#ff0000',x,y,width,'S',
CASE WHEN  R6_1=1 and R6_2 is null then '1' ELSE
case WHEN  R6_2=1 and R6_1 is null then '2' else '' END END as circle
from quran_data where

qareesrest like '%حمزة%'
 and r5_2 is null
 AND
 reading not like 'وقف%'
 and reading not like 'وله حال الوقف%'
 and reading not like 'بضم الهاء والميم وصلا، وبضم الهاء وإسكان الميم وقفا.'
 and reading not like 'بضم الهاء والميم وصلا، وبكسر الهاء وإسكان الميم وقفا.'
 and sub_subject not like '%صراط%'
 and sub_subject<>'عليهم'
 and sub_subject<>'إليهم'
 and sub_subject<>'لديهم'
 AND
   sub_subject not like '%شيء%'
   and
   sub_subject not like '%شيئا%'
   and
((reading like '%كسر%' 
) or
(reading like '% ضم%'
) or
(reading like '%بضم%'
) or
(reading like '%مفتوحة%'
) or
(reading like '%بفتح%'
) or


(reading like '%سكون%'
)
or
(reading like '%مكسورة%'
) or
(reading like '%بكسر%'
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
and (reading <>'قرأ بصلة ميم الجمع وصلا.')
and (reading<>'قرأ بصلة ميم الجمع وصلاً بخلف عنه.')
and (reading <>'قرأ بصلة ميم الجمع وصلاً مع الإشباع.')
and reading<>'قرأ بضم الهاء مع الوقف بهاء السكت باتفاق.'
and reading<>'قرأ بضم هاء الضمير ، مع الوقف بهاء السكت.'
and reading <>'قرأ بترك الإمالة، ووقف على نون النسوة بهاء السكت.'
and reading <>'قرأ بكسر الهاء ووقف بهاء السكت باتفاق.'
and r5_2 is null;
update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
update madina_temp set x= 0.0 where x<0.0;

-- أبو عمرو
-- فهو تم استيراده

-- كسر الهاء وصلا

delete from madina_temp ;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'C',page_number1,'#0000ff',x,y,0.05,'H', '4'
from quran_data where 
            ((R3_1 IS NOT NULL ) or (R3_2 IS NOT NULL )) AND
             (IFNULL(r5_2, 0) = 0) and
(reading = 'بكسر الهاء والميم وصلا، وبكسر الهاء وإسكان الميم وقفا.'
)
order by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
update madina_temp set x= 0.0 where x<0.0;


-- ادغام إدغام كبير

delete from madina_temp;
insert into madina_temp(qaree,page_number,color,x,y,width,style,circle)
select 'C',page_number1,'#007FFF',case when sub_subject like '% %' then  x-width/2  else x end,y,width,'S',CASE WHEN  R6_1=1 and R6_2 is null then '1' ELSE
case WHEN  R3_2=1 and R3_1 is null then '2' else '' END END as circle
from quran_data where 
            (R3_1 IS NOT NULL or R3_2 IS NOT NULL) AND
             (IFNULL(r5_2, 0) = 0) 
			 and
             ((reading like '%دغام%كبير%')

			 )

			 ORDER by aya_index,id;

update madina_temp set circle= '' where circle is null;
update madina_temp set STYLE= 'S' where style  is null;
update madina_temp set x= 0.0 where x<0.0;