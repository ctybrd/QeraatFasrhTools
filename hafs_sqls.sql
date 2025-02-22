-- الكلمات الخلافية بين شعبة وحفص
select sub_subject1,aya,resultnew,reading from quran_data where r5_1=1 and r5_2 is null
and sora=30 order by aya_index,id;

--ملحق 2 -  مواضع الإظهار الحلقي
-- 1. إظهار النون الساكنة من كلمة عند الهمزة
-- كلمة ينأون فقط في القرآن
-- 2. إظهار النون الساكنة من كلمة عند الهاء
select wordindex,ayah,word,mshfword,nextword2 from wordsall where mshfword like '%نۡه%'
and surah=30 order by wordindex;
--3. إظهار النون الساكنة من كلمة عند العين

select wordindex,ayah,word,mshfword,nextword2 from wordsall where mshfword like '%نۡع%'
and surah=30 order by wordindex;

--4. إظهار النون الساكنة من كلمة عند الحاء
select wordindex,ayah,word,mshfword,nextword2 from wordsall where mshfword like '%نۡح%'
and surah=30 order by wordindex;
--5. إظهار النون الساكنة من كلمة عند الغين
-- كلمة فسينغضون فقط في القرآن
select wordindex,ayah,word,mshfword,nextword2 from wordsall where mshfword like '%نۡغ%'
 order by wordindex;

 --6. إظهار النون الساكنة من كلمة عند الخاء
 select wordindex,ayah,word,mshfword,nextword2 from wordsall where mshfword like '%نۡخ%'
 and surah=30 
 order by wordindex;
 -- 7. إظهار النون الساكنة من كلمتين
-- إظهار النون الساكنة من كلمتين عند الهمزة 
 select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%نْ أ%'
 or
 nextword2 like '%نْ آ%'
 )
 and surah=30 
 order by wordindex;

 -- 1.	إظهار النون الساكنة من كلمتين عند الهاء
  select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%نْ ه%'
 
 )
 and surah=30 
 order by wordindex;

 --2.	إظهار النون الساكنة من كلمتين عند العين
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%نْ ع%'
 
 )
 and surah=30 
 order by wordindex;

 -- 3.	إظهار النون الساكنة من كلمتين عند الحاء
 select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%نْ ح%'
 
 )
 and surah=30 
 order by wordindex;

 -- 4.	إظهار النون الساكنة من كلمتين عند الغين 
 select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%نْ غ%'
 
 )
 and surah=30 
 order by wordindex;
-- 5.	إظهار النون الساكنة من كلمتين عند الخاء 
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%نْ خ%'
 
 )
 and surah=30 
 order by wordindex;

 -- 8. إظهار التنوين
-- 1.	إظهار التنوين عند الهمزة 

 select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%ً أ%'
 or
 nextword2 like '%ً آ%'
 or
 nextword2 like '%ً إ%'
 or
 nextword2 like '%ًا أ%'
 or 
 nextword2 like '%ًا إ%'
 )
 and surah=30 
 order by wordindex;

 2.	إظهار التنوين عند الهاء
  select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%ً ه%'
 or
 nextword2 like '%ًا ه%'
  or
  nextword2 like '%ٌ ه%'
 or
  nextword2 like '%ٍ ه%'
 )
 and surah=30
 order by wordindex;

--3.	إظهار التنوين عند العين

select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%ً ع%'
 or
 nextword2 like '%ًا ع%'
  or
  nextword2 like '%ٌ ع%'
 or
  nextword2 like '%ٍ ع%'
 )
 and surah=30
 order by wordindex;
--4.	إظهار التنوين عند الحاء
 select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%ً ح%'
 or
 nextword2 like '%ًا ح%'
  or
  nextword2 like '%ٌ ح%'
 or
  nextword2 like '%ٍ ح%'
 )
 and surah=30
 order by wordindex;
--5.	إظهار التنوين عند الغين
 select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%ً غ%'
 or
 nextword2 like '%ًا غ%'
  or
  nextword2 like '%ٌ غ%'
 or
  nextword2 like '%ٍ غ%'
 )
 and surah=30
 order by wordindex;

 --6.	إظهار التنوين عند الخاء 
 select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%ً خ%'
 or
 nextword2 like '%ًا خ%'
  or
  nextword2 like '%ٌ خ%'
 or
  nextword2 like '%ٍ خ%'
 )
 and surah=30
 order by wordindex;

 --3) ملحق (3): جمع مواضع الإدغام بغنة
--1. إدغام النون الساكنة بغنة عند الياء 
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%نْ ي%'
 )
 and surah=30
 order by wordindex;


--2. إدغام النون الساكنة بغنة عند الميم
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%نْ م%'
 )
 and surah=30
 order by wordindex;
 --3. إدغام النون الساكنة بغنة عند الواو 
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
  (nextword2 like '%نْ و%'
 )
 and surah=30
 order by wordindex;
-- 4) ملحق (4): جمع مواضع الإدغام بغنة
--1. إدغام التنوين بغنة عند الياء  
  select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%ً ي%'
 or
 nextword2 like '%ًا ي%'
  or
  nextword2 like '%ٌ ي%'
 or
  nextword2 like '%ٍ ي%'
 )
 and surah=30
 order by wordindex;

--1. إدغام التنوين بغنة عند النون
  select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%ً ن%'
 or
 nextword2 like '%ًا ن%'
  or
  nextword2 like '%ٌ ن%'
 or
  nextword2 like '%ٍ ن%'
 )
 and surah=30
 order by wordindex;
--2. إدغام التنوين بغنة عند الميم
  select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%ً م%'
 or
 nextword2 like '%ًا م%'
  or
  nextword2 like '%ٌ م%'
 or
  nextword2 like '%ٍ م%'
 )
 and surah=30
 order by wordindex;

 --3. إدغام التنوين بغنة عند الواو 

  select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%ً و%'
 or
 nextword2 like '%ًا و%'
 or
 nextword2 like '%ًى و%'
  or
  nextword2 like '%ٌ و%'
 or
  nextword2 like '%ٍ و%'
 )
 and surah=30
 order by wordindex;

 -- 5) ملحق (5): جمع مواضع القلب
-- 1. قلب النون الساكنة من كلمة
  select wordindex,ayah,word,mshfword,nextword2 from wordsall where
  word like '%نْب%'
 and surah=30
 order by wordindex;

 -- 2. قلب النون الساكنة من كلمتين
select wordindex,ayah,word,mshfword,nextword2 from wordsall where
  nextword2 like '%نْ ب%'
 and surah=30
 order by wordindex;
--3. قلب التنوين
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
 (nextword2 like '%ً ب%'
 or
 nextword2 like '%ًا ب%'
 or
 nextword2 like '%ًى ب%'
  or
  nextword2 like '%ٌ ب%'
 or
  nextword2 like '%ٍ ب%'
 )
 and surah=30
 order by wordindex;

-- 6) ملحق (6): جمع مواضع الإخفاء الحقيقي
--في كلمة وفي كلمتين
--1. إخفاء النون الساكنة عند التاء
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْت%'
or 
nextword2 like '%نْ ت%'
)
   and surah=30
 order by wordindex;

 --2. إخفاء النون الساكنة عند الثاء
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْث%'
or 
nextword2 like '%نْ ث%'
)
   and surah=30
 order by wordindex;
--3. إخفاء النون الساكنة عند الجيم
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْج%'
or 
nextword2 like '%نْ ج%'
)
   and surah=30
 order by wordindex;
--4. إخفاء النون الساكنة عند الدال
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْد%'
or 
nextword2 like '%نْ د%'
)
   and surah=30
 order by wordindex;
--5. إخفاء النون الساكنة عند الذال
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْذ%'
or 
nextword2 like '%نْ ذ%'
)
   and surah=30
 order by wordindex;
--6. إخفاء النون الساكنة عند الزاي 
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْذ%'
or 
nextword2 like '%نْ ذ%'
)
   and surah=30
 order by wordindex;

--7. إخفاء النون الساكنة عند السين

select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْس%'
or 
nextword2 like '%نْ س%'
)
   and surah=30
 order by wordindex;
--8. إخفاء النون الساكنة عند الشين
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْش%'
or 
nextword2 like '%نْ ش%'
)
   and surah=30
 order by wordindex;

--9. إخفاء النون الساكنة عند الصاد
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْص%'
or 
nextword2 like '%نْ ص%'
)
   and surah=30
 order by wordindex;
--10. إخفاء النون الساكنة عند الضاد
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْض%'
or 
nextword2 like '%نْ ض%'
)
   and surah=30
 order by wordindex;
--11. إخفاء النون الساكنة عند الطاء
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْط%'
or 
nextword2 like '%نْ ط%'
)
   and surah=30
 order by wordindex;

-- 12. إخفاء النون الساكنة عند الظاء
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْظ%'
or 
nextword2 like '%نْ ظ%'
)
   and surah=30
 order by wordindex;
--13. إخفاء النون الساكنة عند الفاء
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْف%'
or 
nextword2 like '%نْ ف%'
)
   and surah=30
 order by wordindex;

--14. إخفاء النون الساكنة عند القاف
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْق%'
or 
nextword2 like '%نْ ق%'
)
   and surah=30
 order by wordindex;
--15. إخفاء النون الساكنة عند الكاف 
select wordindex,ayah,word,mshfword,nextword2 from wordsall where 
( word like '%نْك%'
or 
nextword2 like '%نْ ك%'
)
   and surah=30
 order by wordindex;


-- إخفاء التنوين
-- 1. إخفاء التنوين عند التاء
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ت%'
   OR nextword2 LIKE '%ًا ت%'
   OR nextword2 LIKE '%ًى ت%'
   OR nextword2 LIKE '%ٌ ت%'
   OR nextword2 LIKE '%ٍ ت%')
  AND surah=30
ORDER BY wordindex;

-- 2. إخفاء التنوين عند الثاء
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ث%'
   OR nextword2 LIKE '%ًا ث%'
   OR nextword2 LIKE '%ًى ث%'
   OR nextword2 LIKE '%ٌ ث%'
   OR nextword2 LIKE '%ٍ ث%')
  AND surah=30
ORDER BY wordindex;

-- 3. إخفاء التنوين عند الجيم
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ج%'
   OR nextword2 LIKE '%ًا ج%'
   OR nextword2 LIKE '%ًى ج%'
   OR nextword2 LIKE '%ٌ ج%'
   OR nextword2 LIKE '%ٍ ج%')
  AND surah=30
ORDER BY wordindex;

-- 4. إخفاء التنوين عند الدال
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً د%'
   OR nextword2 LIKE '%ًا د%'
   OR nextword2 LIKE '%ًى د%'
   OR nextword2 LIKE '%ٌ د%'
   OR nextword2 LIKE '%ٍ د%')
  AND surah=30
ORDER BY wordindex;

-- 5. إخفاء التنوين عند الذال
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ذ%'
   OR nextword2 LIKE '%ًا ذ%'
   OR nextword2 LIKE '%ًى ذ%'
   OR nextword2 LIKE '%ٌ ذ%'
   OR nextword2 LIKE '%ٍ ذ%')
  AND surah=30
ORDER BY wordindex;

-- 6. إخفاء التنوين عند الزاي
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ز%'
   OR nextword2 LIKE '%ًا ز%'
   OR nextword2 LIKE '%ًى ز%'
   OR nextword2 LIKE '%ٌ ز%'
   OR nextword2 LIKE '%ٍ ز%')
  AND surah=30
ORDER BY wordindex;

-- 7. إخفاء التنوين عند السين
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً س%'
   OR nextword2 LIKE '%ًا س%'
   OR nextword2 LIKE '%ًى س%'
   OR nextword2 LIKE '%ٌ س%'
   OR nextword2 LIKE '%ٍ س%')
  AND surah=30
ORDER BY wordindex;

-- 8. إخفاء التنوين عند الشين
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ش%'
   OR nextword2 LIKE '%ًا ش%'
   OR nextword2 LIKE '%ًى ش%'
   OR nextword2 LIKE '%ٌ ش%'
   OR nextword2 LIKE '%ٍ ش%')
  AND surah=30
ORDER BY wordindex;

-- 9. إخفاء التنوين عند الصاد
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ص%'
   OR nextword2 LIKE '%ًا ص%'
   OR nextword2 LIKE '%ًى ص%'
   OR nextword2 LIKE '%ٌ ص%'
   OR nextword2 LIKE '%ٍ ص%')
  AND surah=30
ORDER BY wordindex;

-- 10. إخفاء التنوين عند الضاد
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ض%'
   OR nextword2 LIKE '%ًا ض%'
   OR nextword2 LIKE '%ًى ض%'
   OR nextword2 LIKE '%ٌ ض%'
   OR nextword2 LIKE '%ٍ ض%')
  AND surah=30
ORDER BY wordindex;

-- 11. إخفاء التنوين عند الطاء
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ط%'
   OR nextword2 LIKE '%ًا ط%'
   OR nextword2 LIKE '%ًى ط%'
   OR nextword2 LIKE '%ٌ ط%'
   OR nextword2 LIKE '%ٍ ط%')
  AND surah=30
ORDER BY wordindex;

-- 12. إخفاء التنوين عند الظاء
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ظ%'
   OR nextword2 LIKE '%ًا ظ%'
   OR nextword2 LIKE '%ًى ظ%'
   OR nextword2 LIKE '%ٌ ظ%'
   OR nextword2 LIKE '%ٍ ظ%')
  AND surah=30
ORDER BY wordindex;

-- 13. إخفاء التنوين عند الفاء
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ف%'
   OR nextword2 LIKE '%ًا ف%'
   OR nextword2 LIKE '%ًى ف%'
   OR nextword2 LIKE '%ٌ ف%'
   OR nextword2 LIKE '%ٍ ف%')
  AND surah=30
ORDER BY wordindex;

-- 14. إخفاء التنوين عند القاف
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ق%'
   OR nextword2 LIKE '%ًا ق%'
   OR nextword2 LIKE '%ًى ق%'
   OR nextword2 LIKE '%ٌ ق%'
   OR nextword2 LIKE '%ٍ ق%')
  AND surah=30
ORDER BY wordindex;

-- 15. إخفاء التنوين عند الكاف
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (nextword2 LIKE '%ً ك%'
   OR nextword2 LIKE '%ًا ك%'
   OR nextword2 LIKE '%ًى ك%'
   OR nextword2 LIKE '%ٌ ك%'
   OR nextword2 LIKE '%ٍ ك%')
  AND surah=30
ORDER BY wordindex;


--7) ملحق (7): جمع مواضع النون المشددة من كلمة
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  (word like '%نّ%')
  AND surah=30
ORDER BY wordindex;

--8) ملحق (8): جمع مواضع الميم المشددة من كلمة
SELECT wordindex, ayah, mshfword, nextword2 FROM wordsall WHERE 
  word like '%مّ%'
  AND surah=30
ORDER BY wordindex;

-- 9) ملحق (9): جمع مواضع الإخفاء الشفوي 
select wordindex,ayah,word,mshfword,nextword2 from wordsall where
  nextword2 like '%مْ ب%'
 and surah=30
 order by wordindex;

--10) ملحق (10): جمع مواضع الإظهار الشفوي
--1.	الإظهار الشفوي من كلمة

SELECT wordindex, ayah, word, mshfword, nextword2 
FROM wordsall 
WHERE 
  word LIKE '%مْ%' 
  AND word NOT LIKE '%مْ'  -- Exclude words ending with مْ

  AND LENGTH(word) > 2      -- Ensure the word is long enough to have مْ in the middle
  AND surah = 30
ORDER BY wordindex;
--2.	الإظهار الشفوي من كلمتين
SELECT wordindex, ayah, word, mshfword, nextword2 
FROM wordsall 
WHERE 
  (nextword2  LIKE '%مْ %' 
  or
  nextword2  LIKE '%م %'
  )
  and nextword2 NOT LIKE '%مْ ب%'
  and nextword2 NOT LIKE '%مْ م%'
  AND surah = 30
ORDER BY wordindex;

--11) ملحق (11): جمع مواضع الإظهار القمري
SELECT wordindex, ayah, word, mshfword, nextword2 
FROM wordsall 
WHERE 
  (mshfword LIKE '%ٱلۡ%'
  or
  mshfword  LIKE '%لِلۡ%'
  )
  and nextword2 NOT LIKE '%مْ ب%'
  and nextword2 NOT LIKE '%مْ م%'
  AND surah = 30
ORDER BY wordindex;

--12) ملحق (12): جمع مواضع الإدغام الشمسي
SELECT rawword, MIN(wordindex), MIN(ayah), COUNT(*) 
FROM wordsall 
WHERE (
  rawword LIKE 'الت%' 
  OR rawword LIKE 'الث%' 
  OR rawword LIKE 'الد%' 
  OR rawword LIKE 'الذ%' 
  OR rawword LIKE 'الر%' 
  OR rawword LIKE 'الز%' 
  OR rawword LIKE 'الس%' 
  OR rawword LIKE 'الش%' 
  OR rawword LIKE 'الص%' 
  OR rawword LIKE 'الض%' 
  OR rawword LIKE 'الط%' 
  OR rawword LIKE 'الظ%' 
  OR rawword LIKE 'الل%' 
  OR rawword LIKE 'الن%' 
  OR rawword LIKE 'للت%' 
  OR rawword LIKE 'للث%' 
  OR rawword LIKE 'للد%' 
  OR rawword LIKE 'للذ%' 
  OR rawword LIKE 'للر%' 
  OR rawword LIKE 'للز%' 
  OR rawword LIKE 'للس%' 
  OR rawword LIKE 'للش%' 
  OR rawword LIKE 'للص%' 
  OR rawword LIKE 'للض%' 
  OR rawword LIKE 'للط%' 
  OR rawword LIKE 'للظ%' 
  OR rawword LIKE 'للل%' 
  OR rawword LIKE 'للن%' 
  OR rawword LIKE 'بالت%' 
  OR rawword LIKE 'بالث%' 
  OR rawword LIKE 'بالد%' 
  OR rawword LIKE 'بالذ%' 
  OR rawword LIKE 'بالر%' 
  OR rawword LIKE 'بالز%' 
  OR rawword LIKE 'بالس%' 
  OR rawword LIKE 'بالش%' 
  OR rawword LIKE 'بالص%' 
  OR rawword LIKE 'بالض%' 
  OR rawword LIKE 'بالط%' 
  OR rawword LIKE 'بالظ%' 
  OR rawword LIKE 'بالل%' 
  OR rawword LIKE 'بالن%' 
  OR rawword LIKE 'فالت%' 
  OR rawword LIKE 'فالث%' 
  OR rawword LIKE 'فالد%' 
  OR rawword LIKE 'فالذ%' 
  OR rawword LIKE 'فالر%' 
  OR rawword LIKE 'فالز%' 
  OR rawword LIKE 'فالس%' 
  OR rawword LIKE 'فالش%' 
  OR rawword LIKE 'فالص%' 
  OR rawword LIKE 'فالض%' 
  OR rawword LIKE 'فالط%' 
  OR rawword LIKE 'فالظ%' 
  OR rawword LIKE 'فالل%' 
  OR rawword LIKE 'فالن%' 
  OR rawword LIKE 'والت%' 
  OR rawword LIKE 'والث%' 
  OR rawword LIKE 'والد%' 
  OR rawword LIKE 'والذ%' 
  OR rawword LIKE 'والر%' 
  OR rawword LIKE 'والز%' 
  OR rawword LIKE 'والس%' 
  OR rawword LIKE 'والش%' 
  OR rawword LIKE 'والص%' 
  OR rawword LIKE 'والض%' 
  OR rawword LIKE 'والط%' 
  OR rawword LIKE 'والظ%' 
  OR rawword LIKE 'والل%' 
  OR rawword LIKE 'والن%' 
)  
AND surah = 30  
GROUP BY rawword  
ORDER BY MIN(wordindex);

-- 13) ملحق (13): جمع مواضع
-- إدغام المتماثلين الصغير

SELECT wordindex, ayah, word, mshfword, nextword2 
FROM wordsall 
WHERE (nextword2 LIKE '%اْ ا%' 
   OR nextword2 LIKE '%بْ ب%' 
   OR nextword2 LIKE '%تْ ت%' 
   OR nextword2 LIKE '%ثْ ث%' 
   OR nextword2 LIKE '%جْ ج%' 
   OR nextword2 LIKE '%حْ ح%' 
   OR nextword2 LIKE '%خْ خ%' 
   OR nextword2 LIKE '%دْ د%' 
   OR nextword2 LIKE '%ذْ ذ%' 
   OR nextword2 LIKE '%رْ ر%' 
   OR nextword2 LIKE '%زْ ز%' 
   OR nextword2 LIKE '%سْ س%' 
   OR nextword2 LIKE '%شْ ش%' 
   OR nextword2 LIKE '%صْ ص%' 
   OR nextword2 LIKE '%ضْ ض%' 
   OR nextword2 LIKE '%طْ ط%' 
   OR nextword2 LIKE '%ظْ ظ%' 
   OR nextword2 LIKE '%عْ ع%' 
   OR nextword2 LIKE '%غْ غ%' 
   OR nextword2 LIKE '%فْ ف%' 
   OR nextword2 LIKE '%قْ ق%' 
   OR nextword2 LIKE '%كْ ك%' 
   OR nextword2 LIKE '%لْ ل%' 
   OR nextword2 LIKE '%مْ م%' 
   OR nextword2 LIKE '%نْ ن%' 
   OR nextword2 LIKE '%هْ ه%' 
   OR nextword2 LIKE '%وْ و%' 
   OR nextword2 LIKE '%يْ ي%' 
   )
AND surah = 30  
ORDER BY wordindex;

--14) ملحق (14): جمع مواضع
--إدغام المتجانسين الصغير
SELECT wordindex, ayah, word, mshfword, nextword2 
FROM wordsall 
WHERE (
   -- الأحرف النطعية
   nextword2 LIKE '%تْ ط%' 
   OR nextword2 LIKE '%طْ ت%' 
   OR nextword2 LIKE '%تْ د%' 
   OR nextword2 LIKE '%دْ ت%' 

   -- الأحرف اللثوية
   OR nextword2 LIKE '%ثْ ذ%' 
   OR nextword2 LIKE '%ذْ ظ%' 

   -- الأحرف الشفوية
   OR nextword2 LIKE '%بْ م%' 
)
   AND surah = 30  
ORDER BY wordindex;
