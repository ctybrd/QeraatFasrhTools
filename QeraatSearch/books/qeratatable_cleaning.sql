-- إزالة كلمة قرأ قرؤوا
UPDATE qeraat_brief
SET reading = 
  case WHEN reading LIKE 'قرؤوا %' THEN SUBSTR(reading, 7)
   WHEN reading like 'قرأ %'  THEN SUBSTR(reading, 5)
    ELSE reading END;
-- حذف العكس لإدغام خلف عن حمزة بدون غنة
delete from qeraat_brief where 
qareesrest='نافع,ابن كثير, الدوري عن أبي عمرو, ابن عامر, عاصم, حمزة, الكسائي, أبو جعفر, يعقوب, خلف العاشر,'
 and reading ='بالإظهار.'

-- حذف عكس صلة ميم الجمع

delete from qeraat_brief where 
qareesrest='باقي الرواة' 
and reading ='بترك صلة ميم الجمع.'

-- حذف عكس إمالة هاء التأنيث
delete from qeraat_brief where 
qareesrest='نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,'
and reading ='بفتح هاء التأنيث.'



نافع,ابن كثير, أبو عمرو, ابن عامر, عاصم, حمزة, أبو جعفر, يعقوب, خلف العاشر,
أظهر اللام عند النون.

