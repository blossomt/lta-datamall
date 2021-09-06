# lta-datamall

Using Github actions to regularly download bus stop, bus route, and bus service data from [LTA DataMall API](https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf).

## Usage
Get an API key from LTA and add it as a repository secret named `ACCOUNTKEY`.

Frequency of data extraction is set in [run.yml](.github/workflows/run.yml). This workflow runs once daily at 00:00 UTC (08:00 SGT).