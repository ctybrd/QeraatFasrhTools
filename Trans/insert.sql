insert into ayas_phonetic ("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"phonetic" as lang,
	surahContentPhonetic as text
FROM qSurahContent order by _id;

insert into ayas_malay ("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"malay" as lang,
	surahContentMalay as text
FROM qSurahContent order by _id;


insert into ayas_indonesian ("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"indonesian" as lang,
	surahContentIndonesian as text
FROM qSurahContent order by _id;

insert into ayas_french("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"french" as lang,
	surahContentFrench as text
FROM qSurahContent order by _id;

insert into ayas_dutch("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"dutch" as lang,
	surahContentDutch as text
FROM qSurahContent order by _id;


insert into ayas_norwegian("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"norwegian" as lang,
	surahContentNorwegian as text
FROM qSurahContent order by _id;

insert into ayas_swedish("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"swedish" as lang,
	surahContentSwedish as text
FROM qSurahContent order by _id;

insert into ayas_farsi("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"farsi" as lang,
	surahContentFarsi as text
FROM qSurahContent order by _id;

insert into ayas_urdu("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"urdu" as lang,
	surahContentUrdu as text
FROM qSurahContent order by _id;

insert into ayas_pickthall("aya_index",
  "sora",
  "aya",
  "lang",
  "text" )
SELECT
	_id	as aya_index,
	surahID	as sora,
	ayahID	as aya,
	"pickthall" as lang,
	surahContentPickthall as text
FROM qSurahContent order by _id;






