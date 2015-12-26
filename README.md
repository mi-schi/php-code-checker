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

To use this scripts is a better alternative to ant configurations on your jenkins. The python scripts are more flexible and they can also be used on your local dev machine.
You can simply define all settings in the ```composer.json``` in your project but you don't have to.
The scripts also support multiple folders for exclusion.

## Installation

Via git:

    git clone git@github.com:mi-schi/php-code-checker.git

Via composer:

    composer require mi-schi/php-code-checker

## Usage

Use python to execute the scripts in the project folder:

    python all.py
    python check.py
    python metric.py

The ```all.py``` script execute the ```check.py``` and ```metric.py``` script. You can set the first argument as project path:

    python all.py /path/to/your/project/

If your want to execute the tests with coverage apart to speed up your deployment, then use the ```python coverage.py``` script.
You can update all internal dependencies with ```python update.py path/to/php```.

## Configuration

The configuration is quite simple. Look in the [default_configuration.json](data/default_configuration.json) for inspiration.
Add an extra node to the ```composer.json``` in your project and overwrite the default configuration if you want.

## Jenkins integration

There is a huge configuration to process all these reports on jenkins. First you have to install the following plugins:

* [Checkstyle](https://wiki.jenkins-ci.org/display/JENKINS/Checkstyle+Plugin)
* [Clover PHP](https://wiki.jenkins-ci.org/display/JENKINS/Clover+PHP+Plugin)
* [Crap4J](https://wiki.jenkins-ci.org/display/JENKINS/Crap4J+Plugin)
* [Plot](https://wiki.jenkins-ci.org/display/JENKINS/Plot+Plugin)
* [PMD](https://wiki.jenkins-ci.org/display/JENKINS/PMD+Plugin)
* [Sidebar-Link](https://wiki.jenkins-ci.org/display/JENKINS/Sidebar-Link+Plugin)
* [Violations](https://wiki.jenkins-ci.org/display/JENKINS/Violations)
* [xUnit](https://wiki.jenkins-ci.org/display/JENKINS/xUnit+Plugin)

Also useful:
* [Task Scanner](https://wiki.jenkins-ci.org/display/JENKINS/Task+Scanner+Plugin)

Then, create a new empty job called ```default-job```. Copy the [default-jenkins-config.xml](data/default-jenkins-config.xml) to ```/var/lib/jenkins/jobs/default-job/config.xml``` on your jenkins.
That was it. Append the configuration and copy from this moment forth the ```default-job```.
