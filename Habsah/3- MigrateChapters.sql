DECLARE @id INT, @name NVARCHAR(50)

DECLARE db_cursor CURSOR FOR 
SELECT sora, sora_name FROM quran_sora

OPEN db_cursor  
FETCH NEXT FROM db_cursor INTO @id, @name

WHILE @@FETCH_STATUS = 0
BEGIN
	INSERT INTO Chapters (Id, [Name]) VALUES (@id, @name)
	
    FETCH NEXT FROM db_cursor INTO @id, @name
END 

CLOSE db_cursor  
DEALLOCATE db_cursor 