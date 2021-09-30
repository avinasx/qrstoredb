USE "dims-II";  
GO

CREATE INDEX first_index
ON dbo.mpi_file (part_no);

CREATE INDEX second_index
ON dbo.stokfile (part_no);

