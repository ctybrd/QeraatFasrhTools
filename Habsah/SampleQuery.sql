SELECT d.Id, p.ChapterId, p.Word, p.Verse, d.Description
FROM DifferenceRecitators AS dr
JOIN PositionDifferences AS pd ON pd.Id = dr.PositionDifferenceId
JOIN Differences AS d ON d.Id = pd.DifferenceId
JOIN Positions AS p ON p.Id = pd.PositionId
WHERE dr.RecitatorId = 1 AND p.ChapterId = 2 AND p.MadinaPage < 22
ORDER BY p.Verse

