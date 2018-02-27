# Unmaintained. Deprecated in favor of [DSA Sign In Sheets](https://github.com/PhillyDSA/dsa-sign-in-sheets)

[![CircleCI](https://circleci.com/gh/PhillyDSA/phillydsa-intake-form.svg?style=svg)](https://circleci.com/gh/PhillyDSA/phillydsa-intake-form) [![codecov](https://codecov.io/gh/PhillyDSA/phillydsa-intake-form/branch/develop/graph/badge.svg)](https://codecov.io/gh/PhillyDSA/phillydsa-intake-form)

# Philly DSA Intake Form
Temporary form to be used for updating membership info at general meetings until we can provide this functionality on the main website.

## Installation

Standard Django installation. You'll need to create a `conf.ini` file similar to the one in the repo with your API key for [ActionNetwork](http://www.actionnetwork.org) and your Django `SECRET_KEY`.

## Contributing

####  Code of Conduct
All contributors agree to abide by the Philly DSA Code of Conduct, which can be found at: [TKTK](github.com/TKTK).

#### Environment
Install requirements. If you're using [pyenv](https://github.com/pyenv/pyenv):

* `make dev`

Or by running:

* `pip install -r requirements/dev.txt`

This will install all the required dependencies for the project. We use [pre-commit](http://pre-commit.com/) hooks, so if you didn't install by `make dev`, run `pre-commit install` in the root directory.

Development occurs on the `develop` branch and `master` is reserved for releases. See [A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/) for rationale. [Git Flow AVH](https://github.com/petervanderdoes/gitflow-avh) is one tool to help manage this workflow. YMMV so use whatever you're comfortable with and it'll work out in the end.

#### Testing

Please ensure that all contributions have corresponding test coverage. Running `make test` will run all the tests for the project and output a coverage report.

#### Pull Requests

We use the following naming conventions, which help to keep things organized:

* Branch name for production releases: `master`
* Branch name for "next release" development: `develop`
* Feature branch prefix: `feature/`
* Bugfix branch prefix: `bugfix/`
* Release branch prefix: `release/`
* Hotfix branch prefix: `hotfix/`

To submit a pull request, start new branch, commit your changes, and then submit the PR. We're all volunteers, so review may not be immediate (it doesn't mean you're being ignored!), but if it's been a while, ping a collaborator.

#### Issues

Feel free to submit any issues you come across, whether they're technical or something about installation or usage is unclear - both are important and welcome.

We use issue templates, which may not be appropriate for all issues, so take the template with a grain of salt.

## Usage

_TKTK_
