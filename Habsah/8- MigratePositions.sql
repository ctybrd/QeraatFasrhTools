DECLARE @id INT,
		@word NVARCHAR(300),
		@diff_desc NVARCHAR(500),
		@chapter_id INT = 1,
		@verse INT,
		@page1 INT,
		@page2 INT

DECLARE db_cursor CURSOR FOR 
SELECT sora, aya, sub_subject, reading, page_number1, page_number2, tags
FROM quran_data

OPEN db_cursor  
FETCH NEXT FROM db_cursor INTO @chapter_id, @verse, @word, @diff_desc

WHILE @@FETCH_STATUS = 0
BEGIN
	DECLARE @is_new_position BIT = IIF(EXISTS(SELECT 1 FROM dbo.Positions WHERE Word = @word AND ChapterId = @chapter_id AND Verse = @verse), 0, 1)
	
	DECLARE @position_id INT = (SELECT IIF(
		@is_new_position = 1,  
		(SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.Positions),  
		(SELECT TOP(1) Id FROM dbo.Positions WHERE Word = @word AND ChapterId = @chapter_id AND Verse = @verse ORDER BY Id)))

	IF @is_new_position = 1
		INSERT INTO Positions (Id, Word, ChapterId, MadinaPage, ShemerlyPage, Verse) VALUES (@position_id, @word, @chapter_id, @page1, @page2, @verse)
	
    FETCH NEXT FROM db_cursor INTO @chapter_id, @verse, @word, @diff_desc, @page1, @page2
END 

CLOSE db_cursor  
DEALLOCATE db_cursor 