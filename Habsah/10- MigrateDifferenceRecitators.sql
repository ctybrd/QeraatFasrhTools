BEGIN TRY
	BEGIN TRANSACTION
		DECLARE @word NVARCHAR(300),
				@diff_desc NVARCHAR(1000),
				@chapter_id INT,
				@verse INT,
				@Q1 INT,
				@R1_1 INT, 
				@R1_2 INT,
				@Q2 INT,
				@R2_1 INT, 
				@R2_2 INT,
				@Q3 INT, 
				@R3_1 INT, 
				@R3_2 INT,
				@Q4 INT, 
				@R4_1 INT, 
				@R4_2 INT,
				@Q5 INT, 
				@R5_1 INT, 
				@R5_2 INT,
				@Q6 INT, 
				@R6_1 INT, 
				@R6_2 INT,
				@Q7 INT, 
				@R7_1 INT, 
				@R7_2 INT,
				@Q8 INT, 
				@R8_1 INT, 
				@R8_2 INT,
				@Q9 INT, 
				@R9_1 INT, 
				@R9_2 INT,
				@Q10 INT, 
				@R10_1 INT, 
				@R10_2 INT

		DECLARE db_cursor CURSOR FOR 
		SELECT sora, aya, sub_subject, reading,
			Q1, R1_1, R1_2,
			Q2, R2_1, R2_2,
			Q3, R3_1, R3_2,
			Q4, R4_1, R4_2,
			Q5, R5_1, R5_2,
			Q6, R6_1, R6_2,
			Q7, R7_1, R7_2,
			Q8, R8_1, R8_2,
			Q9, R9_1, R9_2,
			Q10, R10_1, R10_2
		FROM quran_data
		ORDER BY sora, aya
		
		OPEN db_cursor  
		FETCH NEXT FROM db_cursor INTO @chapter_id, @verse, @word, @diff_desc,
			@Q1, @R1_1, @R1_2, @Q2, @R2_1, @R2_2, @Q3, @R3_1, @R3_2, @Q4, @R4_1, @R4_2, @Q5, @R5_1, @R5_2,
			@Q6, @R6_1, @R6_2, @Q7, @R7_1, @R7_2, @Q8, @R8_1, @R8_2, @Q9, @R9_1, @R9_2, @Q10, @R10_1, @R10_2
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			DECLARE @position_id INT = (SELECT TOP(1) Id FROM dbo.Positions WHERE Word = @word AND ChapterId = @chapter_id AND Verse = @verse ORDER BY Id)
			DECLARE @difference_id INT = (SELECT TOP(1) Id FROM dbo.Differences WHERE [Description] = @diff_desc ORDER BY Id)
			
			DECLARE @position_difference_id INT = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.PositionDifferences)
			INSERT INTO PositionDifferences(Id, DifferenceId, PositionId) VALUES(@position_difference_id, @difference_id, @position_id)
		
			DECLARE @position_difference_recitator_id INT
		
			IF @Q1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 1)
			END
			IF @R1_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 2)
			END
			IF @R1_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 3)
			END
			
			IF @Q2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 4)
			END
			IF @R2_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 5)
			END
			IF @R2_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 6)
			END
		
			IF @Q3 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 7)
			END
			IF @R3_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 8)
			END
			IF @R3_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 9)
			END
		
			IF @Q4 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 10)
			END
			IF @R4_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 11)
			END
			IF @R4_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 12)
			END
		
			IF @Q5 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 13)
			END
			IF @R5_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 14)
			END
			IF @R5_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 15)
			END
		
			IF @Q6 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 16)
			END
			IF @R6_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 17)
			END
			IF @R6_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 18)
			END
		
			IF @Q7 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 19)
			END
			IF @R7_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 20)
			END
			IF @R7_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 21)
			END
		
			IF @Q8 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 22)
			END
			IF @R8_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 23)
			END
			IF @R8_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 24)
			END
		
			IF @Q9 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 25)
			END
			IF @R9_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 26)
			END
			IF @R9_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 27)
			END
		
			IF @Q10 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 28)
			END
			IF @R10_1 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 29)
			END
			IF @R10_2 = 1
			BEGIN
				SET @position_difference_recitator_id = (SELECT ISNULL(MAX(Id), 0) + 1 FROM dbo.DifferenceRecitators)
				INSERT INTO DifferenceRecitators(Id, PositionDifferenceId, RecitatorId) VALUES(@position_difference_recitator_id, @position_difference_id, 30)
			END
		
		    FETCH NEXT FROM db_cursor INTO @chapter_id, @verse, @word, @diff_desc,
				@Q1, @R1_1, @R1_2, @Q2, @R2_1, @R2_2, @Q3, @R3_1, @R3_2, @Q4, @R4_1, @R4_2, @Q5, @R5_1, @R5_2,
				@Q6, @R6_1, @R6_2, @Q7, @R7_1, @R7_2, @Q8, @R8_1, @R8_2, @Q9, @R9_1, @R9_2, @Q10, @R10_1, @R10_2
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
       @ErrorMessage = ERROR_MESSAGE(),  
       @ErrorSeverity = ERROR_SEVERITY(),  
       @ErrorState = ERROR_STATE();  

    RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);

	CLOSE db_cursor  
	DEALLOCATE db_cursor
END CATCH