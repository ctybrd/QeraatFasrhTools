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