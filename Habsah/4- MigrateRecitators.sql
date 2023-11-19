DECLARE @id INT, @name NVARCHAR(200)

DECLARE db_cursor CURSOR FOR SELECT id, [name] FROM qareemaster

OPEN db_cursor
FETCH NEXT FROM db_cursor INTO @id, @name

WHILE @@FETCH_STATUS = 0
BEGIN
	INSERT INTO Recitators(Id, [Name]) VALUES (@id, @name)
	
    FETCH NEXT FROM db_cursor INTO @id, @name
END 

CLOSE db_cursor  
DEALLOCATE db_cursor 