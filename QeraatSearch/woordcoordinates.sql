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
select 'B',page_number1,case when reading like '%بصلة هاء الضمير%' 
then '#32cd32' else '#ff0000' end ,x,y,width,'S',CASE WHEN  R2_1=1 and R2_2 is null then '1' ELSE
case WHEN  R2_2=1 and R2_1 is null then '2' else '' END END
from quran_data where 
            (R2_1 IS NOT NULL or R2_2 IS NOT NULL) AND
             (IFNULL(r5_2, 0) = 0) and
             (reading <> 'بصلة ميم الجمع وصلا.'
			 )
       and 
       (reading <>'بضم ميم الجمع، ووصلها بواو لفظية.');


-- in the farsh db
delete from madina where qaree='B';
insert into madina select * from madina_temp;
update madina set circle= '' where circle is null;
update madina set STYLE= 'S' where style  is null;
update madina set width= width/2 where qaree='B' and color='#32cd32';
update madina set width= width-.01 where qaree='B' and color<>'#32cd32';

