BEGIN TRY
	BEGIN TRANSACTION
		DECLARE @diff_desc NVARCHAR(1000), @tags VARCHAR(100)

		DECLARE db_cursor CURSOR FOR 
		SELECT reading, tags FROM quran_data
		
		OPEN db_cursor
		FETCH NEXT FROM db_cursor INTO @diff_desc, @tags
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			DECLARE @is_new_difference BIT = IIF(EXISTS(SELECT 1 FROM dbo.Differences WHERE Description = @diff_desc), 0, 1)

			DECLARE @difference_id INT = (SELECT IIF(
				@is_new_difference = 1,  
				(SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.Differences),  
				(SELECT TOP(1) Id FROM dbo.Differences WHERE [Description] = @diff_desc ORDER BY Id)))
		
			IF @is_new_difference = 1
				INSERT INTO Differences (Id, [Description]) VALUES (@difference_id, @diff_desc)
			
			IF @tags IS NOT NULL
				BEGIN
					DECLARE @tag VARCHAR(50)
					DECLARE categories_db_cursor CURSOR FOR 
					SELECT value FROM STRING_SPLIT(substring(@tags,2,(LEN(@tags)-2)), ',')
					OPEN categories_db_cursor  
					FETCH NEXT FROM categories_db_cursor INTO @tag
					WHILE @@FETCH_STATUS = 0
					BEGIN
						DECLARE @difference_category_id INT = (SELECT Id FROM DifferenceCategories WHERE [Name] = @tag)
						DECLARE @difference_tag_id INT = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceTags)
						INSERT INTO DifferenceTags(Id, DifferenceId, DifferenceCategoryId) VALUES (@difference_tag_id, @difference_id, @difference_category_id)
						FETCH NEXT FROM categories_db_cursor INTO @tag
					END
					CLOSE categories_db_cursor  
					DEALLOCATE categories_db_cursor
				END

			    FETCH NEXT FROM db_cursor INTO @diff_desc, @tags
			END 
		
		CLOSE db_cursor  
		DEALLOCATE db_cursor

		COMMIT TRAN
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRAN --RollBack in case of Error

    DECLARE @ErrorMessage NVARCHAR(4000);  
    DECLARE @ErrorSeverity INT;  
    DECLARE @ErrorState INT;

    SELECT   
       @ErrorMessage = CONCAT(ERROR_MESSAGE(), @tag),
       @ErrorSeverity = ERROR_SEVERITY(),  
       @ErrorState = ERROR_STATE();  

    RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);

	CLOSE db_cursor  
	DEALLOCATE db_cursor
END CATCH



