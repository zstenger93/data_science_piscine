-- merge_tables.sql
CREATE TABLE IF NOT EXISTS customers AS
(
    -- Query for table1
    SELECT * FROM data_2022_dec
    UNION ALL
    -- Query for table2
    SELECT * FROM data_2022_nov
    UNION ALL
    -- Query for table3
    SELECT * FROM data_2022_oct
    UNION ALL
    -- Query for table4
    SELECT * FROM data_2023_feb
    UNION ALL
    -- Query for table5
    SELECT * FROM data_2023_jan
);
