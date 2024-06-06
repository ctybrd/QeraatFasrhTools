SELECT  text_full,aya_index,id,sub_subject,reading,qareesrest,resultnew from all_qeraat where 
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
and r5_2 is null
and (resultnew is null
or resultnew='')
order by aya_index,id