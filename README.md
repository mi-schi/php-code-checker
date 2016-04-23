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


This script is a better alternative to configure ant on your jenkins. The python script is more flexible and can also be used on your local dev machine. You can define all settings in the `composer.json` in your project, but you don't have to. The scripts also supports exclusion of multiple folders.


The scripts are tested with `Python 2.6` and `Python 3.5`.

## Installation

Via git:

    git clone git@github.com:mi-schi/php-code-checker.git

Via composer:

    composer require mi-schi/php-code-checker

## Usage

Use python to execute the script in the project folder:

    checker.py all
    checker.py check
    checker.py metric

The `all` argument executes the `check` and `metric` argument. You can set the second argument as project path:

    checker.py all /path/to/your/project
    checker.py all relative/path

If you want to execute tests with coverage, regardless your configuration, then use the `checker.py coverage` argument.
You can update all internal dependencies with `update.py path/to/php`.

## Configuration

The configuration is simple. Just look in the [default_configuration.json](data/default_configuration.json) for usage. Add an extra property to the `composer.json` in your project and overwrite the default configuration if you want.
The `php-code-checker` comes with its own dependencies for `phpunit`, `phpcs` and so on. If you want to use another `phpunit`, you can define the `bin-dir` property and add `phpunit` in your composer requirements.
If `php-code-checker` find `path/to/your/project/bin/phpunit` then this binary will be used. Otherwise your tests were executed with the `phpunit` version which comes with `php-code-checker`.

## Jenkins integration

There is a huge configuration to process all these reports on Jenkins. First you have to install the following plugins:

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

Then, create a new empty job called ```default-job```. Copy the [default-jenkins-config.xml](data/default-jenkins-config.xml) to ```/var/lib/jenkins/jobs/default-job/config.xml``` on your Jenkins.
That's it! Append the configuration and copy `default-job` from now on.
