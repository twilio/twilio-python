# Bumping versions

Checklist:

* Run the unit tests
* Run the Twilio stage integration tests
* Add a short change description to CHANGES
* Update the version number in `twilio/__init__.py`
* Update the version number in `docs/conf.py`
* Commit the version bumps.
* Tag a new release in Github with both the version and the `latest` tag.

        git tag 3.3.9
        git tag -d latest
        git tag latest
        git push upstream --tags

* Upload to PyPI. You need a `~/.pypirc` file with this in it:

        [pypirc]
        servers =
            pypi

        [server-login]
        username:<username>
        password:<password>

    You can get the username and password from someone who has them.

    Then run:

        python setup.py sdist

    If you are satisfied with the output, upload to PyPI:

        python setup.py sdist upload
