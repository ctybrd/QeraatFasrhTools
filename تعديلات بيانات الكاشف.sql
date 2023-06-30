--select 'insert into all_quran_data(name,frsh,reads,reader,recsrc,location)select '''+name+''','''+frsh+''','''+reads+''','''+reader+''',''shalaby'',* from fnsplit('''+location+''',''+'')' from all_quran_data where location like '%+%'

--update [dbo].[all_quran_data] set sora_number=(select top 1 sora_number from quran_sora where [all_quran_data].location like '%'+convert(nvarchar,sora_name)+'%')

--update all_quran_data set sora_number=0 where (location like '%ÌãíÚ%')  and location like '%ÇáŞÑÂä%'
--update all_quran_data set sora_number=0 where (location like '%ÌãíÛ%')  and location like '%ÇáŞÑÂä%'

--update all_quran_data set recsrc=isnull(recsrc,'KASHEF')
--update all_quran_data set aya_number=SUBSTRING(location,PATINDEX('%ÂíÉ%',location),100)
--delete from all_quran_data where location like '%+%'
--update all_quran_data set aya_number=REPLACE(aya_number,'ÂíÉ: ','')

--update all_quran_data set inc=reader
--update all_quran_data set inc= SUBSTRING(reader,1,patindex('%ãÇ ÚÏÇ:%',reader)-1) where reader like '%ãÇ ÚÏÇ:%'
--update all_quran_data set exc= SUBSTRING(reader,patindex('%ãÇ ÚÏÇ:%',reader),1000) where reader like '%ãÇ ÚÏÇ:%'
--sELECT COLUMN_NAME INTO READER_DIC FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='ALL_QURAN_DATA' AND LEN(COLUMN_NAME)<5 AND (COLUMN_NAME LIKE 'R%' OR COLUMN_NAME LIKE 'Q%') ORDER BY ORDINAL_POSITION
--update all_quran_data set reader=replace(reader, 'ÇáŞÑøÖÇÁ
--update all_quran_data set reader=replace(reader, 'ÇáŞÑÇ ','ÇáŞÑÇÁ')
-- update all_quran_data set reader=replace(reader, 'ÇáŞÑøÇÁ ','ÇáŞÑÇÁ')
--update all_quran_data set reader=replace(reader, 'ÇáŞÑøÇÁ ','ÇáŞÑÇÁ')
--update all_quran_data set reader=replace(reader, 'ÇáŞÑøóÇÁ','ÇáŞÑÇÁ')
--select distinct reader from all_quran_data where reader like  '%ÚÔ%'
--update all_quran_data set reader=replace(reader, ' ãÇ ÚÏ:',' ãÇ ÚÏÇ:')

--update all_quran_data set inc=REPLACE(inc,':','|')
--update all_quran_data set Q1=1,R11=1,R12=1,Q2=1,R21=1,R22=1,Q3=1,R31=1,R32=1,Q4=1,R41=1,R42=1,Q5=1,R51=1,R52=1,Q6=1,R61=1,R62=1,Q7=1,R71=1,R72=1,Q8=1,R81=1,R82=1,Q9=1,R91=1,R92=1,Q10=1,R101=1,R102=1 where inc like '%ÇáŞÑÇÁ ÇáÚÔÑÉ%'
--update all_quran_data set inc = REPLACE(inc,'ÈÎáİ','ÈÎáÇİ')
--update all_quran_data set inc = REPLACE(inc,'Îáİ ÇáÚÇÔÑ','ÇáÚÇÔÑ')

--select 'update all_quran_data set '+column_name+'=1 where inc like ''%'+arabic_name+'%''' from reader_dic

--update all_quran_data set Q1=1 where inc like '%äÇİÚ%'
--update all_quran_data set R11=1 where inc like '%ŞÇáæä%'
--update all_quran_data set R12=1 where inc like '%æÑÔ%'
--update all_quran_data set Q2=1 where inc like '%ÇÈä ßËíÑ%'
--update all_quran_data set R21=1 where inc like '%ÇáÈÒí%'
--update all_quran_data set R22=1 where inc like '%ŞäÈá%'
--update all_quran_data set Q3=1 where inc like '%ÃÈæ ÚãÑæ%'
--update all_quran_data set R31=1 where inc like '%ÇáÏæÑí%'
--update all_quran_data set R32=1 where inc like '%ÇáÓæÓí%'
--update all_quran_data set Q4=1 where inc like '%ÇÈä ÚÇãÑ%'
--update all_quran_data set R41=1 where inc like '%åÔÇã%'
--update all_quran_data set R42=1 where inc like '%ÇÈä ĞßæÇä%'
--update all_quran_data set Q5=1 where inc like '%ÚÇÕã%'
--update all_quran_data set R51=1 where inc like '%ÔÚÈÉ%'
--update all_quran_data set R52=1 where inc like '%ÍİÕ%'
--update all_quran_data set Q6=1 where inc like '%ÍãÒÉ%'
--update all_quran_data set R61=1 where inc like '%Îáİ%'
--update all_quran_data set R62=1 where inc like '%ÎáÇÏ%'
--update all_quran_data set Q7=1 where inc like '%ÇáßÓÇÆí%'
--update all_quran_data set R71=1 where inc like '%ÃÈæ ÇáÍÇÑË%'
--update all_quran_data set R72=1 where inc like '%ÍİÕ ÇáÏæÑí%'
--update all_quran_data set Q8=1 where inc like '%ÃÈæ ÌÚİÑ%'
--update all_quran_data set R81=1 where inc like '%ÇÈä æÑÏÇä%'
--update all_quran_data set R82=1 where inc like '%ÇÈä ÌãÇÒ%'
--update all_quran_data set Q9=1 where inc like '%íÚŞæÈ%'
--update all_quran_data set R91=1 where inc like '%ÑæíÓ%'
--update all_quran_data set R92=1 where inc like '%ÑæÍ%'
--update all_quran_data set Q10=1 where inc like '%ÇáÚÇÔÑ%'
--update all_quran_data set R101=1 where inc like '%ÅÓÍÇŞ%'
--update all_quran_data set R102=1 where inc like '%ÅÏÑíÓ%'

--select 'update all_quran_data set '+column_name+'=0 where exc like ''%'+arabic_name+'%'' and exc <>''''' from reader_dic
--update all_quran_data set Q1=0 where exc like '%äÇİÚ%' and exc <>''
--update all_quran_data set R11=0 where exc like '%ŞÇáæä%' and exc <>''
--update all_quran_data set R12=0 where exc like '%æÑÔ%' and exc <>''
--update all_quran_data set Q2=0 where exc like '%ÇÈä ßËíÑ%' and exc <>''
--update all_quran_data set R21=0 where exc like '%ÇáÈÒí%' and exc <>''
--update all_quran_data set R22=0 where exc like '%ŞäÈá%' and exc <>''
--update all_quran_data set Q3=0 where exc like '%ÃÈæ ÚãÑæ%' and exc <>''
--update all_quran_data set R31=0 where exc like '%ÇáÏæÑí%' and exc <>''
--update all_quran_data set R32=0 where exc like '%ÇáÓæÓí%' and exc <>''
--update all_quran_data set Q4=0 where exc like '%ÇÈä ÚÇãÑ%' and exc <>''
--update all_quran_data set R41=0 where exc like '%åÔÇã%' and exc <>''
--update all_quran_data set R42=0 where exc like '%ÇÈä ĞßæÇä%' and exc <>''
--update all_quran_data set Q5=0 where exc like '%ÚÇÕã%' and exc <>''
--update all_quran_data set R51=0 where exc like '%ÔÚÈÉ%' and exc <>''
--update all_quran_data set R52=0 where exc like '%ÍİÕ%' and exc <>''
--update all_quran_data set Q6=0 where exc like '%ÍãÒÉ%' and exc <>''
--update all_quran_data set R61=0 where exc like '%Îáİ%' and exc <>''
--update all_quran_data set R62=0 where exc like '%ÎáÇÏ%' and exc <>''
--update all_quran_data set Q7=0 where exc like '%ÇáßÓÇÆí%' and exc <>''
--update all_quran_data set R71=0 where exc like '%ÃÈæ ÇáÍÇÑË%' and exc <>''
--update all_quran_data set R72=0 where exc like '%ÍİÕ ÇáÏæÑí%' and exc <>''
--update all_quran_data set Q8=0 where exc like '%ÃÈæ ÌÚİÑ%' and exc <>''
--update all_quran_data set R81=0 where exc like '%ÇÈä æÑÏÇä%' and exc <>''
--update all_quran_data set R82=0 where exc like '%ÇÈä ÌãÇÒ%' and exc <>''
--update all_quran_data set Q9=0 where exc like '%íÚŞæÈ%' and exc <>''
--update all_quran_data set R91=0 where exc like '%ÑæíÓ%' and exc <>''
--update all_quran_data set R92=0 where exc like '%ÑæÍ%' and exc <>''
--update all_quran_data set Q10=0 where exc like '%ÇáÚÇÔÑ%' and exc <>''
--update all_quran_data set R101=0 where exc like '%ÅÓÍÇŞ%' and exc <>''
--update all_quran_data set R102=0 where exc like '%ÅÏÑíÓ%' and exc <>''


--update all_quran_data set R11=0,R12=0 where Q1=0 and  R11=1 and R12=1
--update all_quran_data set R21=0,R22=0 where Q2=0 and  R21=1 and R22=1
--update all_quran_data set R31=0,R32=0 where Q3=0 and  R31=1 and R32=1
--update all_quran_data set R41=0,R42=0 where Q4=0 and  R41=1 and R42=1
--update all_quran_data set R51=0,R52=0 where Q5=0 and  R51=1 and R52=1
--update all_quran_data set R61=0,R62=0 where Q6=0 and  R61=1 and R62=1
--update all_quran_data set R71=0,R72=0 where Q7=0 and  R71=1 and R72=1
--update all_quran_data set R81=0,R82=0 where Q8=0 and  R81=1 and R82=1
--update all_quran_data set R91=0,R92=0 where Q9=0 and  R91=1 and R92=1
--update all_quran_data set R101=0,R102=0 where Q10=0 and  R101=1 and R102=1


--update all_quran_data set R11=1,R12=1 where Q1=1 and  isnull(R11,0)=0 and isnull(R12,0)=0
--update all_quran_data set R21=1,R22=1 where Q2=1 and  isnull(R21,0)=0 and isnull(R22,0)=0
--update all_quran_data set R31=1,R32=1 where Q3=1 and  isnull(R31,0)=0 and isnull(R32,0)=0
--update all_quran_data set R41=1,R42=1 where Q4=1 and  isnull(R41,0)=0 and isnull(R42,0)=0
--update all_quran_data set R51=1,R52=1 where Q5=1 and  isnull(R51,0)=0 and isnull(R52,0)=0
--update all_quran_data set R61=1,R62=1 where Q6=1 and  isnull(R61,0)=0 and isnull(R62,0)=0
--update all_quran_data set R71=1,R72=1 where Q7=1 and  isnull(R71,0)=0 and isnull(R72,0)=0
--update all_quran_data set R81=1,R82=1 where Q8=1 and  isnull(R81,0)=0 and isnull(R82,0)=0
--update all_quran_data set R91=1,R92=1 where Q9=1 and  isnull(R91,0)=0 and isnull(R92,0)=0
--update all_quran_data set R101=1,R102=1 where Q10=1 and  isnull(R101,0)=0 and isnull(R102,0)=0

-- ãËáÇ İÑÔ ŞÇáæä Úä ÍİÕ
--select * from all_quran_data where r11=1 and isnull(R52,0)=0