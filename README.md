# php-code-checker

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE.md)
[![Latest Stable Version](https://poser.pugx.org/mi-schi/php-code-checker/v/stable)](https://packagist.org/packages/mi-schi/php-code-checker)
[![Total Downloads](https://poser.pugx.org/mi-schi/php-code-checker/downloads)](https://packagist.org/packages/mi-schi/php-code-checker)

## Features

Check your php project code with
* [phpunit](https://github.com/sebastianbergmann/phpunit)
* lint
* [phpcpd](https://github.com/sebastianbergmann/phpcpd)
* [phpcs](https://github.com/squizlabs/PHP_CodeSniffer)
* [phpmd](https://github.com/phpmd/phpmd)
* [security-checker](https://github.com/sensiolabs/security-checker)

and create metrics with
* [phploc](https://github.com/sebastianbergmann/phploc)
* [phpmetrics](https://github.com/Halleck45/PhpMetrics)
* [pdepend](https://github.com/pdepend/pdepend)

It is a better alternative to ant scripts on your jenkins. The python scripts are more flexible and they can also be used on your local dev machine.
You can simply define all settings in the ```composer.json``` in your project but you don't have to.
The scripts also support multiple exclusion folders.

## Installation

Via git:

    git clone git@github.com:mi-schi/php-code-checker.git

Via composer:

    composer require mi-schi/php-code-checker

## Usage

Use python to execute the scripts:

    python all.py path/to/your/project/
    python check.py path/to/your/project/
    python metric.py path/to/your/project/

The ```all.py``` script execute the ```check.py``` and ```metric.py``` script.

If your want to execute the tests with coverage apart to speed up your deployment, then use the ```python coverage.py path/to/your/project/``` script.
You can update all internal dependencies with ```python update.py path/to/php```.

## Configuration

The configuration is quite simple. Look in the [default_configuration.json](data/default_configuration.json) for inspiration.
Add an extra node to the ```composer.json``` in your project and overwrite the default configuration if you want.
