DROP VIEW "main"."shmrly_all";
DROP VIEW "main"."madina_all";
DROP VIEW "main"."tjwid_all";
DROP VIEW "main"."libya_all";
CREATE VIEW shmrly_all as select *, 
(select text from book_quran where aya_index = mosshf_shmrly.aya_index) aya_text,
(select text_full from book_quran where aya_index = mosshf_shmrly.aya_index) aya_text_full, 
(select text from book_qortoby where aya_index = mosshf_shmrly.aya_index) qortoby,
(select text from book_e3rab where aya_index = mosshf_shmrly.aya_index) e3rab,
(select text from book_katheer where aya_index = mosshf_shmrly.aya_index) katheer,
(select text from book_moyassar where aya_index = mosshf_shmrly.aya_index) moyassar, 
(select text from book_sa3dy where aya_index = mosshf_shmrly.aya_index) sa3dy, 
(select text from book_tabary where aya_index = mosshf_shmrly.aya_index) tabary,
(select text from book_baghawy where aya_index = mosshf_shmrly.aya_index) baghawy, 
(select text from book_m3any where aya_index = mosshf_shmrly.aya_index) m3any, 
(select text from book_tanweer where aya_index = mosshf_shmrly.aya_index) tanweer,
(select text from book_english where aya_index = mosshf_shmrly.aya_index) english , 
(select text from book_nozol where aya_index = mosshf_shmrly.aya_index) nozol ,
(select text from book_waseet where aya_index = mosshf_shmrly.aya_index) waseet , 
(select text from book_mokhtsr where aya_index = mosshf_shmrly.aya_index) mokhtsr, 
(select text from book_jlalin where aya_index = mosshf_shmrly.aya_index) jlalin,
(select text from book_tayseer10 where aya_index = mosshf_shmrly.aya_index) tayseer10,
(SELECT text FROM book_qqalon WHERE aya_index = mosshf_shmrly.aya_index) AS qqalon,
(SELECT text FROM book_qwarsh WHERE aya_index = mosshf_shmrly.aya_index) AS qwarsh,
(SELECT text FROM book_qibnkather WHERE aya_index = mosshf_shmrly.aya_index) AS qibnkather,
(SELECT text FROM book_aboamro WHERE aya_index = mosshf_shmrly.aya_index) AS aboamro,
(SELECT text FROM book_ibnamer WHERE aya_index = mosshf_shmrly.aya_index) AS ibnamer,
(SELECT text FROM book_sho3ba WHERE aya_index = mosshf_shmrly.aya_index) AS sho3ba,
(SELECT text FROM book_qhamza WHERE aya_index = mosshf_shmrly.aya_index) AS qhamza,
(SELECT text FROM book_kisai WHERE aya_index = mosshf_shmrly.aya_index) AS kisai,
(SELECT text FROM book_abujafar WHERE aya_index = mosshf_shmrly.aya_index) AS abujafar,
(SELECT text FROM book_yaqob WHERE aya_index = mosshf_shmrly.aya_index) AS yaqob,
(SELECT text FROM book_khalaf WHERE aya_index = mosshf_shmrly.aya_index) AS khalaf,
(SELECT text FROM book_all10 WHERE aya_index = mosshf_shmrly.aya_index) AS all10,
(SELECT text FROM book_motshabeh7 WHERE aya_index = mosshf_shmrly.aya_index) AS motshabeh7,
(SELECT text FROM book_asbhni WHERE aya_index = mosshf_shmrly.aya_index) AS asbhni,

(SELECT text FROM book_azerbaijani WHERE aya_index = mosshf_shmrly.aya_index) AS azerbaijani,
(SELECT text FROM book_dutch WHERE aya_index = mosshf_shmrly.aya_index) AS dutch,
(SELECT text FROM book_farsi WHERE aya_index = mosshf_shmrly.aya_index) AS farsi,
(SELECT text FROM book_french WHERE aya_index = mosshf_shmrly.aya_index) AS french,
(SELECT text FROM book_indonesian WHERE aya_index = mosshf_shmrly.aya_index) AS indonesian,
(SELECT text FROM book_malay WHERE aya_index = mosshf_shmrly.aya_index) AS malay,
(SELECT text FROM book_norwegian WHERE aya_index = mosshf_shmrly.aya_index) AS norwegian,
(SELECT text FROM book_phonetic WHERE aya_index = mosshf_shmrly.aya_index) AS phonetic,
(SELECT text FROM book_pickthall WHERE aya_index = mosshf_shmrly.aya_index) AS pickthall,
(SELECT text FROM book_russian WHERE aya_index = mosshf_shmrly.aya_index) AS russian,
(SELECT text FROM book_swedish WHERE aya_index = mosshf_shmrly.aya_index) AS swedish,
(SELECT text FROM book_turkish WHERE aya_index = mosshf_shmrly.aya_index) AS turkish,
(SELECT text FROM book_urdu WHERE aya_index = mosshf_shmrly.aya_index) AS urdu,
(SELECT text FROM book_juzay WHERE aya_index = mosshf_shmrly.aya_index) AS juzay,

(SELECT text FROM book_aljadwal WHERE aya_index = mosshf_shmrly.aya_index) AS aljadwal,
(SELECT text FROM book_aldur WHERE aya_index = mosshf_shmrly.aya_index) AS aldur,
(SELECT text FROM book_mgharieb WHERE aya_index = mosshf_shmrly.aya_index) AS mgharieb,
(SELECT text FROM book_alnashir WHERE aya_index = mosshf_shmrly.aya_index) AS alnashir,
(SELECT text FROM book_zadmaseer WHERE aya_index = mosshf_shmrly.aya_index) AS zadmaseer,
(SELECT text FROM book_ibnatiyah WHERE aya_index = mosshf_shmrly.aya_index) AS ibnatiyah,
(SELECT text FROM book_sahihint WHERE aya_index = mosshf_shmrly.aya_index) AS sahihint
 from mosshf_shmrly;



CREATE VIEW madina_all as select *, 
(select text from book_quran where aya_index = mosshf_madina.aya_index) aya_text,
(select text_full from book_quran where aya_index = mosshf_madina.aya_index) aya_text_full, 
(select text from book_qortoby where aya_index = mosshf_madina.aya_index) qortoby,
(select text from book_e3rab where aya_index = mosshf_madina.aya_index) e3rab,
(select text from book_katheer where aya_index = mosshf_madina.aya_index) katheer,
(select text from book_moyassar where aya_index = mosshf_madina.aya_index) moyassar, 
(select text from book_sa3dy where aya_index = mosshf_madina.aya_index) sa3dy, 
(select text from book_tabary where aya_index = mosshf_madina.aya_index) tabary,
(select text from book_baghawy where aya_index = mosshf_madina.aya_index) baghawy, 
(select text from book_m3any where aya_index = mosshf_madina.aya_index) m3any, 
(select text from book_tanweer where aya_index = mosshf_madina.aya_index) tanweer,
(select text from book_english where aya_index = mosshf_madina.aya_index) english , 
(select text from book_nozol where aya_index = mosshf_madina.aya_index) nozol ,
(select text from book_waseet where aya_index = mosshf_madina.aya_index) waseet , 
(select text from book_mokhtsr where aya_index = mosshf_madina.aya_index) mokhtsr, 
(select text from book_jlalin where aya_index = mosshf_madina.aya_index) jlalin,
(select text from book_tayseer10 where aya_index = mosshf_madina.aya_index) tayseer10,
(SELECT text FROM book_qqalon WHERE aya_index = mosshf_madina.aya_index) AS qqalon,
(SELECT text FROM book_qwarsh WHERE aya_index = mosshf_madina.aya_index) AS qwarsh,
(SELECT text FROM book_qibnkather WHERE aya_index = mosshf_madina.aya_index) AS qibnkather,
(SELECT text FROM book_aboamro WHERE aya_index = mosshf_madina.aya_index) AS aboamro,
(SELECT text FROM book_ibnamer WHERE aya_index = mosshf_madina.aya_index) AS ibnamer,
(SELECT text FROM book_sho3ba WHERE aya_index = mosshf_madina.aya_index) AS sho3ba,
(SELECT text FROM book_qhamza WHERE aya_index = mosshf_madina.aya_index) AS qhamza,
(SELECT text FROM book_kisai WHERE aya_index = mosshf_madina.aya_index) AS kisai,
(SELECT text FROM book_abujafar WHERE aya_index = mosshf_madina.aya_index) AS abujafar,
(SELECT text FROM book_yaqob WHERE aya_index = mosshf_madina.aya_index) AS yaqob,
(SELECT text FROM book_khalaf WHERE aya_index = mosshf_madina.aya_index) AS khalaf,
(SELECT text FROM book_all10 WHERE aya_index = mosshf_madina.aya_index) AS all10,
(SELECT text FROM book_motshabeh7 WHERE aya_index = mosshf_madina.aya_index) AS motshabeh7,
(SELECT text FROM book_asbhni WHERE aya_index = mosshf_madina.aya_index) AS asbhni,

(SELECT text FROM book_azerbaijani WHERE aya_index = mosshf_madina.aya_index) AS azerbaijani,
(SELECT text FROM book_dutch WHERE aya_index = mosshf_madina.aya_index) AS dutch,
(SELECT text FROM book_farsi WHERE aya_index = mosshf_madina.aya_index) AS farsi,
(SELECT text FROM book_french WHERE aya_index = mosshf_madina.aya_index) AS french,
(SELECT text FROM book_indonesian WHERE aya_index = mosshf_madina.aya_index) AS indonesian,
(SELECT text FROM book_malay WHERE aya_index = mosshf_madina.aya_index) AS malay,
(SELECT text FROM book_norwegian WHERE aya_index = mosshf_madina.aya_index) AS norwegian,
(SELECT text FROM book_phonetic WHERE aya_index = mosshf_madina.aya_index) AS phonetic,
(SELECT text FROM book_pickthall WHERE aya_index = mosshf_madina.aya_index) AS pickthall,
(SELECT text FROM book_russian WHERE aya_index = mosshf_madina.aya_index) AS russian,
(SELECT text FROM book_swedish WHERE aya_index = mosshf_madina.aya_index) AS swedish,
(SELECT text FROM book_turkish WHERE aya_index = mosshf_madina.aya_index) AS turkish,
(SELECT text FROM book_urdu WHERE aya_index = mosshf_madina.aya_index) AS urdu,
(SELECT text FROM book_juzay WHERE aya_index = mosshf_madina.aya_index) AS juzay,

(SELECT text FROM book_aljadwal WHERE aya_index = mosshf_madina.aya_index) AS aljadwal,
(SELECT text FROM book_aldur WHERE aya_index = mosshf_madina.aya_index) AS aldur,
(SELECT text FROM book_mgharieb WHERE aya_index = mosshf_madina.aya_index) AS mgharieb,
(SELECT text FROM book_alnashir WHERE aya_index = mosshf_madina.aya_index) AS alnashir,
(SELECT text FROM book_zadmaseer WHERE aya_index = mosshf_madina.aya_index) AS zadmaseer,
(SELECT text FROM book_ibnatiyah WHERE aya_index = mosshf_madina.aya_index) AS ibnatiyah,
(SELECT text FROM book_sahihint WHERE aya_index = mosshf_madina.aya_index) AS sahihint
 from mosshf_madina;


CREATE VIEW tjwid_all as select *, 
(select text from book_quran where aya_index = mosshf_tjwid.aya_index) aya_text,
(select text_full from book_quran where aya_index = mosshf_tjwid.aya_index) aya_text_full, 
(select text from book_qortoby where aya_index = mosshf_tjwid.aya_index) qortoby,
(select text from book_e3rab where aya_index = mosshf_tjwid.aya_index) e3rab,
(select text from book_katheer where aya_index = mosshf_tjwid.aya_index) katheer,
(select text from book_moyassar where aya_index = mosshf_tjwid.aya_index) moyassar, 
(select text from book_sa3dy where aya_index = mosshf_tjwid.aya_index) sa3dy, 
(select text from book_tabary where aya_index = mosshf_tjwid.aya_index) tabary,
(select text from book_baghawy where aya_index = mosshf_tjwid.aya_index) baghawy, 
(select text from book_m3any where aya_index = mosshf_tjwid.aya_index) m3any, 
(select text from book_tanweer where aya_index = mosshf_tjwid.aya_index) tanweer,
(select text from book_english where aya_index = mosshf_tjwid.aya_index) english , 
(select text from book_nozol where aya_index = mosshf_tjwid.aya_index) nozol ,
(select text from book_waseet where aya_index = mosshf_tjwid.aya_index) waseet , 
(select text from book_mokhtsr where aya_index = mosshf_tjwid.aya_index) mokhtsr, 
(select text from book_jlalin where aya_index = mosshf_tjwid.aya_index) jlalin,
(select text from book_tayseer10 where aya_index = mosshf_tjwid.aya_index) tayseer10,
(SELECT text FROM book_qqalon WHERE aya_index = mosshf_tjwid.aya_index) AS qqalon,
(SELECT text FROM book_qwarsh WHERE aya_index = mosshf_tjwid.aya_index) AS qwarsh,
(SELECT text FROM book_qibnkather WHERE aya_index = mosshf_tjwid.aya_index) AS qibnkather,
(SELECT text FROM book_aboamro WHERE aya_index = mosshf_tjwid.aya_index) AS aboamro,
(SELECT text FROM book_ibnamer WHERE aya_index = mosshf_tjwid.aya_index) AS ibnamer,
(SELECT text FROM book_sho3ba WHERE aya_index = mosshf_tjwid.aya_index) AS sho3ba,
(SELECT text FROM book_qhamza WHERE aya_index = mosshf_tjwid.aya_index) AS qhamza,
(SELECT text FROM book_kisai WHERE aya_index = mosshf_tjwid.aya_index) AS kisai,
(SELECT text FROM book_abujafar WHERE aya_index = mosshf_tjwid.aya_index) AS abujafar,
(SELECT text FROM book_yaqob WHERE aya_index = mosshf_tjwid.aya_index) AS yaqob,
(SELECT text FROM book_khalaf WHERE aya_index = mosshf_tjwid.aya_index) AS khalaf,
(SELECT text FROM book_all10 WHERE aya_index = mosshf_tjwid.aya_index) AS all10,
(SELECT text FROM book_motshabeh7 WHERE aya_index = mosshf_tjwid.aya_index) AS motshabeh7,
(SELECT text FROM book_asbhni WHERE aya_index = mosshf_tjwid.aya_index) AS asbhni,

(SELECT text FROM book_azerbaijani WHERE aya_index = mosshf_tjwid.aya_index) AS azerbaijani,
(SELECT text FROM book_dutch WHERE aya_index = mosshf_tjwid.aya_index) AS dutch,
(SELECT text FROM book_farsi WHERE aya_index = mosshf_tjwid.aya_index) AS farsi,
(SELECT text FROM book_french WHERE aya_index = mosshf_tjwid.aya_index) AS french,
(SELECT text FROM book_indonesian WHERE aya_index = mosshf_tjwid.aya_index) AS indonesian,
(SELECT text FROM book_malay WHERE aya_index = mosshf_tjwid.aya_index) AS malay,
(SELECT text FROM book_norwegian WHERE aya_index = mosshf_tjwid.aya_index) AS norwegian,
(SELECT text FROM book_phonetic WHERE aya_index = mosshf_tjwid.aya_index) AS phonetic,
(SELECT text FROM book_pickthall WHERE aya_index = mosshf_tjwid.aya_index) AS pickthall,
(SELECT text FROM book_russian WHERE aya_index = mosshf_tjwid.aya_index) AS russian,
(SELECT text FROM book_swedish WHERE aya_index = mosshf_tjwid.aya_index) AS swedish,
(SELECT text FROM book_turkish WHERE aya_index = mosshf_tjwid.aya_index) AS turkish,
(SELECT text FROM book_urdu WHERE aya_index = mosshf_tjwid.aya_index) AS urdu,
(SELECT text FROM book_juzay WHERE aya_index = mosshf_tjwid.aya_index) AS juzay,

(SELECT text FROM book_aljadwal WHERE aya_index = mosshf_tjwid.aya_index) AS aljadwal,
(SELECT text FROM book_aldur WHERE aya_index = mosshf_tjwid.aya_index) AS aldur,
(SELECT text FROM book_mgharieb WHERE aya_index = mosshf_tjwid.aya_index) AS mgharieb,
(SELECT text FROM book_alnashir WHERE aya_index = mosshf_tjwid.aya_index) AS alnashir,
(SELECT text FROM book_zadmaseer WHERE aya_index = mosshf_tjwid.aya_index) AS zadmaseer,
(SELECT text FROM book_ibnatiyah WHERE aya_index = mosshf_tjwid.aya_index) AS ibnatiyah,
 (SELECT text FROM book_sahihint WHERE aya_index = mosshf_tjwid.aya_index) AS sahihint
from mosshf_tjwid;


CREATE VIEW libya_all as select *, 
(select text from book_quran where aya_index = mosshf_libya.aya_index) aya_text,
(select text_full from book_quran where aya_index = mosshf_libya.aya_index) aya_text_full, 
(select text from book_qortoby where aya_index = mosshf_libya.aya_index) qortoby,
(select text from book_e3rab where aya_index = mosshf_libya.aya_index) e3rab,
(select text from book_katheer where aya_index = mosshf_libya.aya_index) katheer,
(select text from book_moyassar where aya_index = mosshf_libya.aya_index) moyassar, 
(select text from book_sa3dy where aya_index = mosshf_libya.aya_index) sa3dy, 
(select text from book_tabary where aya_index = mosshf_libya.aya_index) tabary,
(select text from book_baghawy where aya_index = mosshf_libya.aya_index) baghawy, 
(select text from book_m3any where aya_index = mosshf_libya.aya_index) m3any, 
(select text from book_tanweer where aya_index = mosshf_libya.aya_index) tanweer,
(select text from book_english where aya_index = mosshf_libya.aya_index) english , 
(select text from book_nozol where aya_index = mosshf_libya.aya_index) nozol ,
(select text from book_waseet where aya_index = mosshf_libya.aya_index) waseet , 
(select text from book_mokhtsr where aya_index = mosshf_libya.aya_index) mokhtsr, 
(select text from book_jlalin where aya_index = mosshf_libya.aya_index) jlalin,
(select text from book_tayseer10 where aya_index = mosshf_libya.aya_index) tayseer10,
(SELECT text FROM book_qqalon WHERE aya_index = mosshf_libya.aya_index) AS qqalon,
(SELECT text FROM book_qwarsh WHERE aya_index = mosshf_libya.aya_index) AS qwarsh,
(SELECT text FROM book_qibnkather WHERE aya_index = mosshf_libya.aya_index) AS qibnkather,
(SELECT text FROM book_aboamro WHERE aya_index = mosshf_libya.aya_index) AS aboamro,
(SELECT text FROM book_ibnamer WHERE aya_index = mosshf_libya.aya_index) AS ibnamer,
(SELECT text FROM book_sho3ba WHERE aya_index = mosshf_libya.aya_index) AS sho3ba,
(SELECT text FROM book_qhamza WHERE aya_index = mosshf_libya.aya_index) AS qhamza,
(SELECT text FROM book_kisai WHERE aya_index = mosshf_libya.aya_index) AS kisai,
(SELECT text FROM book_abujafar WHERE aya_index = mosshf_libya.aya_index) AS abujafar,
(SELECT text FROM book_yaqob WHERE aya_index = mosshf_libya.aya_index) AS yaqob,
(SELECT text FROM book_khalaf WHERE aya_index = mosshf_libya.aya_index) AS khalaf,
(SELECT text FROM book_all10 WHERE aya_index = mosshf_libya.aya_index) AS all10,
(SELECT text FROM book_motshabeh7 WHERE aya_index = mosshf_libya.aya_index) AS motshabeh7,
(SELECT text FROM book_asbhni WHERE aya_index = mosshf_libya.aya_index) AS asbhni,

(SELECT text FROM book_azerbaijani WHERE aya_index = mosshf_libya.aya_index) AS azerbaijani,
(SELECT text FROM book_dutch WHERE aya_index = mosshf_libya.aya_index) AS dutch,
(SELECT text FROM book_farsi WHERE aya_index = mosshf_libya.aya_index) AS farsi,
(SELECT text FROM book_french WHERE aya_index = mosshf_libya.aya_index) AS french,
(SELECT text FROM book_indonesian WHERE aya_index = mosshf_libya.aya_index) AS indonesian,
(SELECT text FROM book_malay WHERE aya_index = mosshf_libya.aya_index) AS malay,
(SELECT text FROM book_norwegian WHERE aya_index = mosshf_libya.aya_index) AS norwegian,
(SELECT text FROM book_phonetic WHERE aya_index = mosshf_libya.aya_index) AS phonetic,
(SELECT text FROM book_pickthall WHERE aya_index = mosshf_libya.aya_index) AS pickthall,
(SELECT text FROM book_russian WHERE aya_index = mosshf_libya.aya_index) AS russian,
(SELECT text FROM book_swedish WHERE aya_index = mosshf_libya.aya_index) AS swedish,
(SELECT text FROM book_turkish WHERE aya_index = mosshf_libya.aya_index) AS turkish,
(SELECT text FROM book_urdu WHERE aya_index = mosshf_libya.aya_index) AS urdu,
(SELECT text FROM book_juzay WHERE aya_index = mosshf_libya.aya_index) AS juzay,

(SELECT text FROM book_aljadwal WHERE aya_index = mosshf_libya.aya_index) AS aljadwal,
(SELECT text FROM book_aldur WHERE aya_index = mosshf_libya.aya_index) AS aldur,
(SELECT text FROM book_mgharieb WHERE aya_index = mosshf_libya.aya_index) AS mgharieb,
(SELECT text FROM book_alnashir WHERE aya_index = mosshf_libya.aya_index) AS alnashir,
(SELECT text FROM book_zadmaseer WHERE aya_index = mosshf_libya.aya_index) AS zadmaseer,
(SELECT text FROM book_ibnatiyah WHERE aya_index = mosshf_libya.aya_index) AS ibnatiyah,
(SELECT text FROM book_sahihint WHERE aya_index = mosshf_libya.aya_index) AS sahihint

 from mosshf_libya;
