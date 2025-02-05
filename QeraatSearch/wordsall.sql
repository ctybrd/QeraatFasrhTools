-- إدراج علامات رؤوس الآيات
delete from wordsall where wordsno =999;
insert into wordsall(surah,ayah,aya_index,page_number2,wordindex,lineno2,x,y,width,rasaya,wordsno)
SELECT w1.surah, 
       w1.ayah, 
       w1.aya_index, 
       w1.page_number2, 
       w1.wordindex, 
       w1.lineno2, 
       ms.x_ratio, 
       ms.y_ratio+0.036,0.05,2,999
FROM words1 w1
JOIN (
    SELECT surah, ayah, aya_index, MAX(wordindex) AS max_wordindex
    FROM words1
    GROUP BY surah, ayah, aya_index
) AS w2
ON  w1.aya_index = w2.aya_index 
   AND w1.wordindex = w2.max_wordindex
JOIN mosshf_shmrly ms
ON w1.aya_index = ms.aya_index
ORDER BY w1.aya_index;


-- إدراج علامات الأرباع
delete from wordsall where wordsno =1001;
insert into wordsall(surah,ayah,aya_index,page_number2,wordindex,lineno2,x,y,width,rasaya,wordsno)
SELECT w1.surah, 
       w1.ayah, 
       w1.aya_index, 
       w1.page_number2, 
       w1.wordindex, 
       w1.lineno2, 
       NULL,NULL,0.03,3,1001
FROM words1 w1
JOIN (
    SELECT surah, ayah, aya_index, MAX(wordindex) AS max_wordindex
    FROM words1
    GROUP BY surah, ayah, aya_index
) AS w2
ON  w1.aya_index = w2.aya_index 
   AND w1.wordindex = w2.max_wordindex
JOIN quran_quarter qq
ON w1.aya_index =(select aya_index from mosshf_shmrly where mosshf_shmrly.sora_number=qq.sora_number
AND
mosshf_shmrly.aya_number=qq.aya_number)-1

ORDER BY w1.aya_index;


-- إدراج مواضع السجدات
delete from wordsall where wordsno =1000;
insert into wordsall(surah,ayah,aya_index,page_number2,wordindex,lineno2,rasaya,wordsno)
SELECT w1.surah, 
       w1.ayah, 
       w1.aya_index, 
       w1.page_number2, 
       w1.wordindex, 
       w1.lineno2,4,1000
FROM words1 w1
JOIN (
    SELECT surah, ayah, aya_index, MAX(wordindex) AS max_wordindex
    FROM words1 where aya_index in(1160,1722,1951,2138,2308,2613,2672,2915,3185,3518,4256,3994,4846,5905,6125)
    GROUP BY surah, ayah, aya_index
) AS w2
ON  w1.aya_index = w2.aya_index 
   AND w1.wordindex = w2.max_wordindex
ORDER BY w1.aya_index;


مواضع السجدات

[الأعراف: 206]
[الرعد: 15]
[النحل: 49-50]
[الإسراء: 107 – 109]
[مريم: 58]
[الحج: 18]
[الفرقان: 60] 
[النمل: 25-26] 
[السجدة: 15]
[فصلت: 37، 38]

[الحج: 77]
[ص: 24]
[النجم: 62] 
[الانشقاق: 20-21]
[العلق: 19]

1160,1722,1951,2138,2308,2613,2672,2915,3185,3518,4256,3994,4846,5905,6125


-- استدعاء ما أتمه كريم من إحداثيات

-- Step 1: Prepare a CTE for matching rows with both wordindex and wordsno
WITH MatchUpdates AS (
    SELECT 
        wordsall.wordindex,
        wordsall.wordsno,
        shmrly_words.x AS new_x,
        shmrly_words.width AS new_width
    FROM 
        wordsall
    JOIN 
        shmrly_words 
    ON 
        wordsall.wordindex = shmrly_words.wordindex
    WHERE 
        wordsall.wordsno < 999

    UNION ALL

    SELECT 
        wordsall.wordindex,
        wordsall.wordsno,
        shmrly_words.x AS new_x,
        shmrly_words.width AS new_width
    FROM 
        wordsall
    JOIN 
        shmrly_words 
    ON 
        case 
            when wordsall.wordsno = 999 then '#0000ff' 
            else '#ff0000' 
        end = shmrly_words.color
        AND wordsall.surah = shmrly_words.surahno
        AND wordsall.ayah = shmrly_words.ayahno
    WHERE 
        wordsall.wordsno = 999
)

-- Step 2: Update rows in wordsall based on the CTE
UPDATE wordsall
SET 
    x = (SELECT new_x FROM MatchUpdates 
         WHERE MatchUpdates.wordindex = wordsall.wordindex 
           AND MatchUpdates.wordsno = wordsall.wordsno),
    width = (SELECT new_width FROM MatchUpdates 
             WHERE MatchUpdates.wordindex = wordsall.wordindex 
               AND MatchUpdates.wordsno = wordsall.wordsno)
WHERE 
    (wordindex, wordsno) IN (
        SELECT wordindex, wordsno FROM MatchUpdates
    );

-- ضبط wordindex
CREATE INDEX idx_quran_data_sub_subject ON quran_data (sub_subject);
CREATE INDEX idx_quran_data_ayah_sura ON quran_data (aya, sora);
CREATE INDEX idx_wordsall_nxtword ON wordsall (nextword);
CREATE INDEX idx_wordsall_ayah_surah ON wordsall (ayah, surah);
CREATE INDEX idx_wordsall_wordindex ON wordsall (wordindex);
CREATE INDEX idx_quran_data_wordindex ON quran_data (wordindex);


update quran_data set wordindex=Null;
UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			quran_data.sub_subject =xy.nextword	
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;

 UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			quran_data.sub_subject=xy.rawword			
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;

 UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			xy.rawword LIKE '%' || quran_data.sub_subject ||'%'
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;
UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			xy.rawword LIKE '%' || quran_data.sub_subject ||'%'
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;
UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			REPLACE(xy.rawword,' ','') = quran_data.sub_subject
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;
UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			REPLACE(xy.rawword,' ','') = replace(quran_data.sub_subject,' ','')
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;
UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			REPLACE(xy.rawword,' ','') LIKE '%' || REPLACE(quran_data.sub_subject,' ','') ||'%'
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;

UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			REPLACE(quran_data.sub_subject,' ','') LIKE '%' || REPLACE(xy.rawword,' ','') ||'%'
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;

UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			REPLACE(quran_data.sub_subject,
			'يا ويلتى'
			,
			'ياويلتا') 
			=xy.rawword
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;

UPDATE quran_data
SET wordindex = (
    SELECT MIN(xy.wordindex)
    FROM wordsall xy
    WHERE 
			REPLACE(quran_data.sub_subject,
			'يا أسفى'
			,
	'ياأسفا'
			)
			=xy.rawword
    AND xy.ayah = quran_data.aya 
    AND xy.surah = quran_data.sora
)
where wordindex is null
;

UPDATE quran_data
SET page_shmrly = (
    SELECT page_number2
    FROM wordsall xy
    WHERE 
    xy.wordindex = quran_data.wordindex 
)
;
update quran_data set page_number2 = page_shmrly;
-- الإحداثيات
UPDATE quran_data
SET x2 = (
    SELECT max(x)
    FROM wordsall xy
    WHERE xy.wordindex=quran_data.wordindex
);

UPDATE quran_data
SET y2 = (
    SELECT min(y)
    FROM wordsall xy
    WHERE xy.wordindex=quran_data.wordindex
);
UPDATE quran_data
SET width2 = (
    SELECT max(width)
    FROM wordsall xy
    WHERE xy.wordindex=quran_data.wordindex
);

UPDATE quran_data
SET page_shmrly = (
    SELECT min(page_number2)
    FROM wordsall xy
    WHERE 
    xy.wordindex = quran_data.wordindex 
)
;
update quran_data set page_number2 = page_shmrly;

UPDATE quran_data
SET rasaya = (
    SELECT max(rasaya)
    FROM wordsall xy
    WHERE 
    xy.wordindex = quran_data.wordindex  and
    xy.wordsno<999
)
;
UPDATE quran_data
SET wordsno = (
    SELECT min(wordsno)
    FROM wordsall xy
    WHERE 
    xy.wordindex = quran_data.wordindex  AND
	xy.wordsno<999
)
;
-- استخراج خطوط فرش

delete from shmrly_temp ;
insert into shmrly_temp(qaree,page_number,color,x,y,width,style,circle)
select 'M',page_number2,'#8080FF'
 ,x2-0.02,y2-0.04,0.05, 'S', '4'
from quran_data where 
  ((R6_1 IS NOT NULL ) and (R6_2 IS NULL )) AND
             (IFNULL(r5_2, 0) = 0) and
(TAGS like '%,idghamn,%' 
)
AND page_number2>=42
order by aya_index,id;