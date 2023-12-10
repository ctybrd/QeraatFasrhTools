#example query
sql1="""
create view Motashabehat1 as SELECT
    sm.index1,
    sm.index2,
    s1.sora_name AS sora_name1,
    b1.aya AS aya1,
    replace(b1.text,'بسم الله الرحمن الرحيم','') AS text1,
    s2.sora_name AS sora_name2,
    b2.aya AS aya2,
    replace(b2.text,'بسم الله الرحمن الرحيم','') AS text2,
    (sm.similarity_score * 100) AS percent_rank
FROM
    similarity_matrix sm
JOIN
    book_quran b1 ON sm.index1 = b1.aya_index
JOIN
    book_quran b2 ON sm.index2 = b2.aya_index
JOIN
    quran_sora s1 ON b1.sora = s1.sora
JOIN
    quran_sora s2 ON b2.sora = s2.sora
WHERE
    b1.text not like '%بسم الله الرحمن الرحيم%'
	and b2.text <>'%الرحمن%';
"""
print(sql1)

sql1= """SELECT
    sm.index1,
    sm.index2,
    s1.sora_name AS sora_name1,
    b1.aya AS aya1,
    replace(b1.text,'بسم الله الرحمن الرحيم','') AS text1,
    s2.sora_name AS sora_name2,
    b2.aya AS aya2,
    replace(b2.text,'بسم الله الرحمن الرحيم','') AS text2,
    (sm.similarity_score * 100) AS percent_rank
FROM
    similarity_matrix sm
JOIN
    book_quran b1 ON sm.index1 = b1.aya_index
JOIN
    book_quran b2 ON sm.index2 = b2.aya_index
JOIN
    quran_sora s1 ON b1.sora = s1.sora
JOIN
    quran_sora s2 ON b2.sora = s2.sora
WHERE
    b1.text not like '%بسم الله الرحمن الرحيم%'
	and b2.text <>'%الرحمن%'
Union
SELECT
    sm.index2 as index1,
    sm.index1 as index2,
    s2.sora_name AS sora_name1,
    b2.aya AS aya1,
    replace(b2.text,'بسم الله الرحمن الرحيم','') AS text1,
    s1.sora_name AS sora_name2,
    b1.aya AS aya2,
    replace(b1.text,'بسم الله الرحمن الرحيم','') AS text2,
    (sm.similarity_score * 100) AS percent_rank
FROM
    similarity_matrix sm
JOIN
    book_quran b1 ON sm.index1 = b1.aya_index
JOIN
    book_quran b2 ON sm.index2 = b2.aya_index
JOIN
    quran_sora s1 ON b1.sora = s1.sora
JOIN
    quran_sora s2 ON b2.sora = s2.sora
WHERE
    b1.text not like '%بسم الله الرحمن الرحيم%'
	and b2.text <>'%الرحمن%'
order by index1

"""
print(sql1)
sql1="""select index1 as aya_index,group_concat(
'<b>' || sora_name2 || ' ' || aya2 || '</b>' || text2 ||' ') as text 
 from MotshabehatU
 group by index1
 order by index1"""
print(sql1)
sql1="""select sora_name1 || ' ' || aya1 || ' ' || text1  as aya1,group_concat(
 sora_name2 || ' ' || aya2 || ' '|| text2 ||' ') as text 
 from MotshabehatU
 group by index1
 order by index1"""
