SELECT wordindex,
       (select word from words n where n.wordindex=m.wordindex+1) as nword,
       word,
       surah,
       ayah,
       pageno
  FROM words m where 
  (word like '%ْ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'أ%'
and m.word not like '%هُمْ'
and m.word not like '%هِمْ'
and m.word not like '%كُمْ'
and m.word not like '%تُمْ')
OR
  (word like '%ْ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'إ%'
and m.word not like '%هُمْ'
and m.word not like '%هِمْ'
and m.word not like '%كُمْ'
and m.word not like '%تُمْ')
OR
(word like '%ْ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'ء%'
and m.word not like '%هُمْ'
and m.word not like '%هِمْ'
and m.word not like '%كُمْ'
and m.word not like '%تُمْ')
or  (word like '%ْ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'آ%'
and m.word not like '%هُمْ'
and m.word not like '%هِمْ'
and m.word not like '%كُمْ'
and m.word not like '%تُمْ')

OR
(m.word like '%الْأ%')
or
(m.word like '%الْإ%')
or 
(m.word like '%الْآ%')
or
  (word like '%ْا'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'أ%'
)
or
  (word like '%ْا'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'إ%'
)
or
(word like '%ٌ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'أ%'
)
or
 (word like '%ٌ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'إ%'
)
or
 (word like '%ٌ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'ء%'
)

or
 (word like '%ٌ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'آ%'
)
or
(word like '%ٍ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'أ%'
)
or
 (word like '%ٍ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'إ%'
)
or
 (word like '%ٍ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'ء%'
)
OR

 (word like '%ٍ'
  and (select word from words n where n.wordindex=m.wordindex+1)
like 'آ%'
)

order by wordindex
;
