USE "dims-II";  
GO

CREATE INDEX first_index
ON dbo.mpi_file (part_no);

CREATE INDEX second_index
ON dbo.stokfile (part_no);

CREATE INDEX third_index
ON dbo.duesin_hist (part_no);

CREATE INDEX fourth_index
ON dbo.duesout (part_no);