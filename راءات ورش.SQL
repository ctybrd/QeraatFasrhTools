select pageno,ayah,word,surah from(select * from words where word like  '%ِر%'  and  word not like  '%رِ%'   and word not like '%رْ%'
and word not like '%رٍ%'
union 
select * from words where (word like '%يْر%'  OR
 word like '%ير%' )and word not like  '%رِ%' 
 and word not like '%رٍ%'
union 
select * from words where (word like  '%ِ_ْر%' ) and  (word not like  '%رِ%')
and (word not like  '%صْر%')
and (word not like  '%قْر%')
and (word not like  '%طْر%')
and (word not like '%رٍ%')
)
where word not like '%إِسْرَائِيل%'
and word not like '%عِمْرَان%'
and word not like '%إِبْرَاهِيم%'
and word not like '%إِرَمَ%'
and word not like '%رَاط%'
order by wordindex
