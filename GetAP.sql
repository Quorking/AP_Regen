-- Input:  AR Invoice # w/ related AP Invoice #'s intending to be resent
-- Output: Returns all necessary details for resend with appropriate spacing, specifically : AR Invoice #, Vendor #, and AP Document #


select invno, vendno, docno from invline where invno = '57706929-01' and docno <> '' 

-- Note A:  Add in additional "or invno..." lines for each unique invoice, this will return all AP Document #'s associated with an invoice
-- allowing user to pick and choose correct records

--or invno = '57706939-01' and docno <> ''

-- Note B: Add in additional "or invno..." & specific "docno = '' if docno is known

--or invno = '57706939-01' and docno = ''

order by invno

--Sample Output

--25701814-06	00503619	14316824-EST
--53708529-03	00503912	53708529-02-EST
--53708529-03	00504674	17A900932B
--53708529-03	00505377	UT12407A-EST
--53708529-03	00500538	CSHI445444A
--53708529-03	00504032	1029186369A-EST
--67704066-01	00503909	67704066-01
--67704066-01	00503727	TFI-841697
--67704066-01	00503727	TFI-841887
--67704066-01	00504667	OI_IV144758
--67704066-01	00503727	TFI-841695
--67704066-01	00503727	TFI-841699
--67704066-01	00503727	TFI-841694
--67704066-01	00503727	TFI-841698
--67704066-01	00503727	TFI-844422
--67704066-01	00503727	TFI-841696
--67704066-01	00503727	TFI-841886