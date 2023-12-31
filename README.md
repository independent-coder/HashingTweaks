# HashingTweaks

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/independent-coder/HashingTweaks/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)

HashingTweaks is a powerful Python command-line application with several features for hashing, finding common passwords using hashes, and utilizing wordlists. This tool is designed to make working with hashes and passwords more efficient and convenient.

## Features

1. Find a common password with a hash (HASH2PASS)
2. Create a password hash (PASS2HASH)
3. Detect a hash algorithm
4. Translate a hash to another algorithm
5. View known hash algorithms
6. File Hashing
7. Compare two Hashes

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Conclusion](#conclusion)

## Installation

1. Clone this repository:
```sh
git clone https://github.com/independent-coder/HashingTweaks.git
```
2. Install python:
Go to [Python.org/downloads](https://www.python.org/downloads/)
Then download it and makes sure to add it to system path.
3. CD to the folder and launch the app
```sh
cd path/to/the/repo/folder
```
4. Then launch python file
```sh
python HT.py
```
## Usage

Find an Existing Password
Choose this option (1) to find an existing password corresponding to a given hash value.

Create a Password Hash
Choose this option (2) to create a hash of a new password using a selected hash algorithm.

Detect Hash Algorithm
Choose this option (3) to detect the hash algorithm used for a given hash value.

Translate Hash to Another Algorithm
Choose this option (4) to translate a hash value from one algorithm to another.

View Known Hash Algorithms
Choose this option (5) to view a list of known hash algorithms along with their descriptions.

File Hashing
Choose this option (6) to calculate the hash value of a file using a selected hash algorithm.

Compare Two Hashes
Choose this option (7) to compare two hash values and determine if they are equal.


## Example

For example, if you want to find the password and you already have your (md5, sha256, sha3_256) password hash, you simply type 1 and select your password hashing algorithm. If you don't know it, go to the third option to find your hashing algorithm. Then enter your hash and find the correct password.

## Conclusion

The common-pass.txt is a big list of 21K lines of common passwords in English and French. Developing this project took a lot of time, so please consider starring my project for more content like this.

See you soon Pal ! :)
