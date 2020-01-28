# Project Title

Scripts that load data from local csv files to AWS DynamoDB.

## Getting Started

* Login to Google Sheets and download a separate CSV for each sheet in the document. Save these with the correct name in the correct order, for example:

``` files = ['./data/media.csv', './data/profile.csv', './data/project.csv'] ```

* Run `aws configure` and input the correct credentials

* Run *create_tables.py* to create the tables

* Run *load.py* to load the CSV data into DynamoDB

### Prerequisites

Requires Python 3, Boto3 and the AWS CLI client.

## Authors

* **Gregory Lindsey** - *Initial work* - [gclindsey](https://github.com/gclindsey)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details