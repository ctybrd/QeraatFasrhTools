# remove extra رقم الآية text
# UPDATE quran_data
# SET subject = SUBSTR(subject, 1, INSTR(subject, '- رقم الآية:') - 1)
# WHERE INSTR(subject, '- رقم الآية:') > 0;
#remove curly braces
# UPDATE quran_data
# SET subject = REPLACE(REPLACE(subject, '{', ''), '}', ''),
#    sub_subject = REPLACE(REPLACE(sub_subject, '{', ''), '}', '');

# update quran_data set page_number1=(SELECT mosshf_madina.page_number  from mosshf_madina where aya_number= quran_data.aya and sora_number=quran_data.sora)
# update quran_data set page_number2=(SELECT mosshf_shmrly.page_number  
# from mosshf_shmrly where aya_number= quran_data.aya and sora_number=quran_data.sora)

-- Add columns Q1, R1_1, R1_2
ALTER TABLE quran_data ADD COLUMN Q1 TEXT;
ALTER TABLE quran_data ADD COLUMN R1_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R1_2 TEXT;

-- Add columns Q2, R2_1, R2_2
ALTER TABLE quran_data ADD COLUMN Q2 TEXT;
ALTER TABLE quran_data ADD COLUMN R2_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R2_2 TEXT;

-- Add columns Q3, R3_1, R3_2
ALTER TABLE quran_data ADD COLUMN Q3 TEXT;
ALTER TABLE quran_data ADD COLUMN R3_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R3_2 TEXT;

-- Add columns Q4, R4_1, R4_2
ALTER TABLE quran_data ADD COLUMN Q4 TEXT;
ALTER TABLE quran_data ADD COLUMN R4_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R4_2 TEXT;

-- Add columns Q5, R5_1, R5_2
ALTER TABLE quran_data ADD COLUMN Q5 TEXT;
ALTER TABLE quran_data ADD COLUMN R5_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R5_2 TEXT;

-- Add columns Q6, R6_1, R6_2
ALTER TABLE quran_data ADD COLUMN Q6 TEXT;
ALTER TABLE quran_data ADD COLUMN R6_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R6_2 TEXT;

-- Add columns Q7, R7_1, R7_2
ALTER TABLE quran_data ADD COLUMN Q7 TEXT;
ALTER TABLE quran_data ADD COLUMN R7_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R7_2 TEXT;

-- Add columns Q8, R8_1, R8_2
ALTER TABLE quran_data ADD COLUMN Q8 TEXT;
ALTER TABLE quran_data ADD COLUMN R8_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R8_2 TEXT;

-- Add columns Q9, R9_1, R9_2
ALTER TABLE quran_data ADD COLUMN Q9 TEXT;
ALTER TABLE quran_data ADD COLUMN R9_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R9_2 TEXT;

-- Add columns Q10, R10_1, R10_2
ALTER TABLE quran_data ADD COLUMN Q10 TEXT;
ALTER TABLE quran_data ADD COLUMN R10_1 TEXT;
ALTER TABLE quran_data ADD COLUMN R10_2 TEXT;


