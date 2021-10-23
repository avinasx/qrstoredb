# qrstoredb
## instructions for image addition:
### Requisites:
1. **open the SQL server management and run following quearies one by one:**
 a) ```
 ALTER TABLE dbo.mpi_file 
 ADD image_url varchar(max);
 ```

b) ```
UPDATE dbo.mpi_file SET image_url = concat('/static/parts/img/',REPLACE(TRIM(part_no), '/', '-'),'.jpg');
```



2. **Image Folder:**
   All images should be saved in this forlder only - ```\qrstoredb\static\parts\img```, where QRSTOREDB is the project folder.


3. **Things need to be taken care of while saving the images of the "Parts":**

a) Name of every image file should be identical to the corresponding 'part_no.'  
b) image extension should be ".jpg" only. if not then please correct it manually. 
c) if there is any space in the beginning or at the end of 'part_no.', then it should be removed in the image name.  
d) if there is any space within the 'part_no.', it should be left as it is in image name also. Please don't change it.  
e) if 'part_no.' contains any "/", then it should be replaced with "-" in the image name.  
f) all the chanages should be done in to the image name saved in the folder only - No need to change anything in the databases.  