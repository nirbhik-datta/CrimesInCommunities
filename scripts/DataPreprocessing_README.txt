http://archive.ics.uci.edu/ml/machine-learning-databases/00211/

Pre-processing using Python (Pandas)

Read 'CommViolPredUnnormalizedData.txt' as a CSV file replacing the '?' strings as NaN values. 
Rename the 'communityname' attribute from each record by removing the following suffices:

'city'
'town'
'township'
'district'
'division'
'borough'
'village'

Further pre-processing (Excel)

Removed following attributes:

'fold': column that was an optional field in the case of cross-validation
'countyCode': Geofield that was commonly missing and redundant
'communityCode': Geofield that was commonly missing and redundant

Replaced a wrongly inputted community name using its actual name
Twentynine Palms-Morongo Valle, CA -> "Morongo Valley, CA

Imported CommViolPredUnnormalizedData.txt as CSV in Google Sheets

Added row for header containing attibutes