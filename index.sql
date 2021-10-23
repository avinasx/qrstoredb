USE "dims-II";  
GO

CREATE INDEX first_index
ON dbo.mpi_file (part_no);

CREATE INDEX second_index
ON dbo.stokfile (part_no);


ALTER TABLE dbo.mpi_file
ADD image_url varchar(max);

UPDATE dbo.mpi_file SET image_url = concat('/static/parts/img/',REPLACE(TRIM(part_no), '/', '-'),'.jpg');

