-- Create a temporary table to store the grouped results
CREATE TEMP TABLE grouped_lines AS
WITH global_groups AS (
    SELECT
        page_number,
        x,
        y,
        -- You can adjust the tolerance values below as needed
        CAST((x * 100) AS INTEGER) AS x_group, -- Adjust the multiplier for tolerance
        CAST((y * 100) AS INTEGER) AS y_group,
        ROW_NUMBER() OVER (PARTITION BY page_number ORDER BY x, y) AS page_group_id
    FROM shmrly
)
SELECT
    gl.page_number,
    gl.x,
    gl.y,
    sl.page_number AS original_page_number,
    sl.x AS original_x,
    sl.y AS original_y,
    gl.page_group_id AS group_id
FROM shmrly AS sl
JOIN global_groups AS gl ON sl.page_number = gl.page_number
    AND CAST((sl.x * 100) AS INTEGER) = gl.x_group
    AND CAST((sl.y * 100) AS INTEGER) = gl.y_group;

-- Update the original table with the group IDs
UPDATE shmrly
SET group_id = gl.group_id
FROM grouped_lines AS gl
WHERE shmrly.page_number = gl.original_page_number
    AND CAST((shmrly.x * 100) AS INTEGER) = gl.original_x
    AND CAST((shmrly.y * 100) AS INTEGER) = gl.original_y;

-- Remove the temporary table
DROP TABLE grouped_lines;
