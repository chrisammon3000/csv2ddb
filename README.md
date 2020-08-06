[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# csv2ddb

Command line tool for easy loading of CSV files directly into AWS DynamoDB.

#### -- Project Status: [Active]

## Getting Started

1. Be sure to configure your AWS client:
   ```
   aws configure
   ```
2. Clone the repo:
   ```
   cd <projects folder>
   git clone https://github.com/abk7777/csv2ddb
   ```

3. Install `csv2ddb`:
   ```
   pip install csv2ddb
   csv2ddb --help
   ```

### Prerequisites

Requires Python 3, Boto3 and the AWS CLI client.

## Usage
List tables:
   ```
   csv2ddb list
   ```

Create a new DynamoDB table:
   ```
   csv2ddb create --table-name my-cool-table --partition-key userId --partition-key-type N
   ```

Load a table:
   ```
   csv2ddb load --table-name my-cool-table my_cool_table.csv
   ```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/abk7777/csv2ddb/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Gregory Lindsey** - [abk7777](https://github.com/abk7777)

## License

This project is licensed under the MIT License.

[contributors-shield]: https://img.shields.io/github/contributors/abk7777/csv2ddb.svg?style=flat-square
[contributors-url]: https://github.com/abk7777/csv2ddb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/abk7777/csv2ddb.svg?style=flat-square
[forks-url]: https://github.com/abk7777/csv2ddb/network/members
[stars-shield]: https://img.shields.io/github/stars/abk7777/csv2ddb.svg?style=flat-square
[stars-url]: https://github.com/abk7777/csv2ddb/stargazers
[issues-shield]: https://img.shields.io/github/issues/abk7777/csv2ddb.svg?style=flat-square
[issues-url]: https://github.com/abk7777/csv2ddb/issues
[license-shield]: https://img.shields.io/github/license/abk7777/csv2ddb.svg?style=flat-square
[license-url]: https://github.com/abk7777/csv2ddb/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gregory-lindsey/