# Brain Games

[![Actions Status](https://github.com/anastasiia-avdeeva/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/anastasiia-avdeeva/python-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=anastasiia-avdeeva_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=anastasiia-avdeeva_python-project-49)

___
## About the project

A set of five console games for brain training. Each game asks you questions. To win give three correct answers in a row. A wrong answer ends the game and suggests trying again
Games:

* Calculator: Arithmetic expressions that need to be calculated
* Progression: Finding missing numbers in a sequence of numbers
* Is number even: Determining whether a number is even
* GCD: Determining the greatest common divisor
* Is number prime: Determining whether a number is prime

___

### Links

This project was built using these tools:

| Tool                                                                   | Description                                             |
|------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust" |

___

### Requirements

* Python ≥ 3.10
* uv package manager

### Installation and Setup

1. Clone repository

    ```bash
    git clone git@github.com:anastasiia-avdeeva/python-project-49.git
    ```

2. Install dependencies

    ```bash
    make install
    ```

3. Build the package

    ```bash
    make build
    ```

4. Install the package locally

    ```bash
    make package-install
    ```

    to update the package:

    ```bash
    make package-reinstall
    ```

5. Run the games

    ```bash
    brain-games
    brain-even
    brain-calc
    brain-gcd
    brain-progression
    brain-prime
    ```

### Example of gameplay

#### Is number even game

[![asciicast](https://asciinema.org/a/bFb83CBpJlXAkEIpLAu2bO5oj.svg)](https://asciinema.org/a/bFb83CBpJlXAkEIpLAu2bO5oj)

#### Calculator game

[![asciicast](https://asciinema.org/a/qt42FUfComO39stz13OJmPmYX.svg)](https://asciinema.org/a/qt42FUfComO39stz13OJmPmYX)

#### Greatest common devisor game

[![asciicast](https://asciinema.org/a/FdY2NVouSswa7ENWTV5sI76Vi.svg)](https://asciinema.org/a/FdY2NVouSswa7ENWTV5sI76Vi)

#### Progression game

[![asciicast](https://asciinema.org/a/XAkpb3XEzG4KR3DbO2B19iXnu.svg)](https://asciinema.org/a/XAkpb3XEzG4KR3DbO2B19iXnu)

#### Is number prime game

[![asciicast](https://asciinema.org/a/2P8TTYFdkZayf1L99gaeiUPfG.svg)](https://asciinema.org/a/2P8TTYFdkZayf1L99gaeiUPfG)
___
