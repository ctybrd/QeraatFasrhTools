CREATE TABLE "quran_sora" (
	"sora"	INTEGER,
	"sora_name"	TEXT,
	"sora_name_tshkeel"	TEXT,
	"sora_type"	TEXT,
	"ayat_number"	INTEGER
)

CREATE TABLE "book_quran" (
	"aya_index"	INTEGER,
	"text"	TEXT,
	"text_full"	TEXT,
	"sora"	INTEGER,
	"aya"	INTEGER
)

CREATE TABLE qareemaster (
    id INTEGER PRIMARY KEY,
    qkey TEXT,
    name TEXT,
    groups TEXT
)
CREATE TABLE "tagsmaster" (
	"id"	INTEGER,
	"tag"	TEXT UNIQUE,
	"description"	TEXT,
	"qarees"	TEXT,
	"category"	TEXT,
	PRIMARY KEY("id")
)
CREATE TABLE "quran_data" (
	"aya_index"	INTEGER,
	"id"	INTEGER,
	"sora"	INTEGER,
	"aya"	INTEGER,
	"sub_subject"	TEXT,
	"qarees"	TEXT,
	"reading"	TEXT,
	"tags"	TEXT,
	"page_number1"	INTEGER,
	"page_number2"	INTEGER,
	"Q1"	TEXT,
	"R1_1"	TEXT,
	"R1_2"	TEXT,
	"Q2"	TEXT,
	"R2_1"	TEXT,
	"R2_2"	TEXT,
	"Q3"	TEXT,
	"R3_1"	TEXT,
	"R3_2"	TEXT,
	"Q4"	TEXT,
	"R4_1"	TEXT,
	"R4_2"	TEXT,
	"Q5"	TEXT,
	"R5_1"	TEXT,
	"R5_2"	TEXT,
	"Q6"	TEXT,
	"R6_1"	TEXT,
	"R6_2"	TEXT,
	"Q7"	TEXT,
	"R7_1"	TEXT,
	"R7_2"	TEXT,
	"Q8"	TEXT,
	"R8_1"	TEXT,
	"R8_2"	TEXT,
	"Q9"	TEXT,
	"R9_1"	TEXT,
	"R9_2"	TEXT,
	"Q10"	TEXT,
	"R10_1"	TEXT,
	"R10_2"	TEXT,
	"readingresult"	TEXT,
	"qareesrest"	TEXT,
	"count_words"	INTEGER,
	"sub_sno"	INTEGER,
	UNIQUE("sora","aya","id")
)
