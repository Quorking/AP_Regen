import os
import datetime
import csv

time = str(datetime.datetime.now())
time = '_' + time[:10].replace('-','_')
confirmation = 'Your AP regen file has been created under "C:\python27\"'

##Get AP file #'s
##Input file should be formatted per tab delimited GetAP-SQL.txt output
##47706374-01	00502522	TFI-827774

with open('APfile.txt') as apdat:
    apdata = csv.reader(apdat, dialect = 'excel', delimiter='\t')
    
    invnos = []
    vendnos = []
    docnos = []
    departments = []

    for row in apdata:
        invnos.append(row[0])
        vendnos.append(row[1])
        docnos.append(row[2])

####Get department #'s from invoice #'s
    for f in range(len(invnos)):
        department = invnos[f]
        department = department[:2]
        departments.append('0' + department)

####Create file to generate output  
    with open(str('AP_regen' + time + '.txt'), 'w') as script:

##Optional variables for SQL script - AP Process
        functionstart = str(
"""INSERT INTO [ITSMain2].[dbo].[ITSWEB_SCHEDULE_TASK]
        ([USER_NAME],[DB_NAME],[TASK_TYPE],[PROCESS_TYPE],[DEPTNO],[INVNO],[CUSTNO],[IN_PROCESS])
VALUES  ('bdp-alec','bdp','XML-OUTBOUND','AP_INV','""")
                            
        functionend = str("', 0)")
                    
##Contatenate all values together & write data to file
        for i in range(len(invnos)):
            line = functionstart + departments[i].strip() + "', '" + docnos[i].strip() + "', '" + vendnos[i].strip() + functionend + '\n'
            script.write(line)
##Clean up
        print(confirmation)
