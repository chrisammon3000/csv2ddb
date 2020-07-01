[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# csv2ddb

Command line tool for easy loading of CSV files directly into AWS DynamoDB.

## Getting Started

1. Be sure to configure your AWS client:
   ```
   aws configure
   ```
2. Clone the repo:
   ```
   cd <projects folder>
   git clone https://github.com/gclindsey/csv2ddb
   ```

3. Install `csv2ddb`:
   ```
   pip install csv2ddb
   csv2ddb --help
   ```

### Prerequisites

Requires Python 3, Boto3 and the AWS CLI client.

## Usage
To create a new DyanamDB table:
   ```
   csv2ddb create --table-name my-cool-table --partition-key userId --partition-key-type S
   ```

To load the table:
   ```
   csv2ddb load --table-name my-cool-table ./data/my_cool_table.csv
   ```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/gclindsey/csv2ddb/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Gregory Lindsey** - [gclindsey](https://github.com/gclindsey)

## License

This project is licensed under the MIT License.

[contributors-shield]: https://img.shields.io/github/contributors/gclindsey/csv2ddb.svg?style=flat-square
[contributors-url]: https://github.com/gclindsey/csv2ddb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gclindsey/csv2ddb.svg?style=flat-square
[forks-url]: https://github.com/gclindsey/csv2ddb/network/members
[stars-shield]: https://img.shields.io/github/stars/gclindsey/csv2ddb.svg?style=flat-square
[stars-url]: https://github.com/gclindsey/csv2ddb/stargazers
[issues-shield]: https://img.shields.io/github/issues/gclindsey/csv2ddb.svg?style=flat-square
[issues-url]: https://github.com/gclindsey/csv2ddb/issues
[license-shield]: https://img.shields.io/github/license/gclindsey/csv2ddb.svg?style=flat-square
[license-url]: https://github.com/gclindsey/csv2ddb/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/gregory-lindsey/
[product-screenshot]: images/screenshot.png