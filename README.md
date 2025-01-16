## Token Generation

The purpose of this project is to generate tokens using the user's name, start date, end date, and a specified algorithm.

The start date is converted to epoch time and concatenated with the user's name to generate tokens iteratively until the epoch time of the end date is reached.

The algorithm can be **md5**, **sha1**, **sha256**, or **sha512**.

Date Format: **DD-MM-YYYY HH:MM:SS**

## How to use

To use this project, you need to have Python3 installed on your machine.

```bash

python3 token_gen.py  -u xpto_user -s '01-16-2025 12:30:00' -e '01-16-2025 12:33:00' -a sha256 -g 0

```

The arguments are:

- -u: user name
- -s: start date
- -e: end date
- -a: algorithm (MD5, SHA1, SHA256, SHA512)

The output will be the token generated, one token per line.

## License

[MIT](https://opensource.org/license/mit)

## Disclaimer

This project is intended for educational purposes only. The author is not responsible for any misuse or damages arising from the use of this project.
