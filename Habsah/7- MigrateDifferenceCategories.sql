DECLARE @id INT, @name NVARCHAR(50), @desc NVARCHAR(200)

DECLARE db_cursor CURSOR FOR SELECT id, tag, [description] FROM tagsmaster

OPEN db_cursor
FETCH NEXT FROM db_cursor INTO @id, @name, @desc

WHILE @@FETCH_STATUS = 0
BEGIN
	INSERT INTO DifferenceCategories(Id, [Name], [Description]) VALUES (@id, @name, @desc)
	
    FETCH NEXT FROM db_cursor INTO @id, @name, @desc
END 

CLOSE db_cursor  
DEALLOCATE db_cursor 