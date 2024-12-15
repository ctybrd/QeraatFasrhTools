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