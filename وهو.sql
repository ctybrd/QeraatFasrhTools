SELECT pageno,word || ' '||        (SELECT word
        FROM words w
        WHERE w.wordindex = words.wordindex + 1),surah,ayah,pageno
FROM words
WHERE word LIKE '%وَهُو%'
   OR word LIKE '%فَهُو%'
   OR word LIKE '%لَهُو%'
   OR word LIKE '%وَهِي%'
   OR word LIKE '%فَهِي%'
   OR word LIKE '%لَهِي%'
   OR (word like '%ثُم%' AND
       (SELECT word
        FROM words w
        WHERE w.wordindex = words.wordindex + 1) like  '%هُو%')
or (word='يُمِلَّ')

		order by wordindex
		
-- brief
select pageno,count(wordindex) from (SELECT wordindex,pageno,word || ' '||        (SELECT word
        FROM words w
        WHERE w.wordindex = words.wordindex + 1),surah,ayah,pageno
FROM words
WHERE word LIKE '%وَهُو%'
   OR word LIKE '%فَهُو%'
   OR word LIKE '%لَهُو%'
   OR word LIKE '%وَهِي%'
   OR word LIKE '%فَهِي%'
   OR word LIKE '%لَهِي%'
   OR (word like '%ثُم%' AND
       (SELECT word
        FROM words w
        WHERE w.wordindex = words.wordindex + 1) like  '%هُو%')
or (word='يُمِلَّ')

) T 
group by 
pageno order by pageno


