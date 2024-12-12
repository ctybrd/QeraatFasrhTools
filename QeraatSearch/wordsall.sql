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
delete from wordsall where wordsno =1000;
insert into wordsall(surah,ayah,aya_index,page_number2,wordindex,lineno2,x,y,width,rasaya,wordsno)
SELECT w1.surah, 
       w1.ayah, 
       w1.aya_index, 
       w1.page_number2, 
       w1.wordindex, 
       w1.lineno2, 
       NULL,NULL,0.03,3,1000
FROM words1 w1
JOIN (
    SELECT surah, ayah, aya_index, MAX(wordindex) AS max_wordindex
    FROM words1
    GROUP BY surah, ayah, aya_index
) AS w2
ON  w1.aya_index = w2.aya_index 
   AND w1.wordindex = w2.max_wordindex
JOIN quran_quarter qq
ON w1.surah = qq.sora_number
AND
w1.ayah = qq.aya_number
ORDER BY w1.aya_index;