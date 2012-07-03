# Bumping versions

Checklist:

* Run the unit tests
* Run the Twilio stage integration tests
* Add a short change description to CHANGES
* Update the version number in `twilio/__init__.py`
* Update the version number in `docs/conf.py`
* Tag a new release in Github with both the version and the `latest` tag.

        git tag 3.3.9
        git tag -d latest
        git tag latest
        git push upstream --tags

