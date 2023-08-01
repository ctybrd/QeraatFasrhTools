SELECT * FROM words
where 
((rawword like '%يه')
or 
(rawword like '%اه')
or
(rawword like '%وه')
or
(word like '%ْهِ')
Or
(word like '%ْهُ') 
)
and 
(
(word not like '٪هً' )
and 
(word not like '٪هٌ' )
and 
(word not like '٪هٍ' )
)