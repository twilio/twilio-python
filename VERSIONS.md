# Versioning Strategy

`twilio-python` uses a modified version of [Semantic Versioning][semver] for all 
changes to the helper library.  It is strongly encouraged that you pin at least 
the major version and potentially the minor version to avoid pulling in breaking 
changes.

Semantic Versions take the form of `MAJOR`.`MINOR`.`PATCH`

When bugs are fixed in the library in a backwards compatible way, the `PATCH` 
level will be incremented by one.  When new features are added to the library 
in a backwards compatible way, the `PATCH` level will be incremented by one.
`PATCH` changes should _not_ break your code and are generally safe for upgrade.

When a new large feature set comes online or a small breaking change is 
introduced, the `MINOR` version will be incremented by one and the `PATCH` 
version reset to zero. `MINOR` changes _may_ require some amount of manual code
change for upgrade. These backwards-incompatible changes will generally be limited 
to a small number of function signature changes.

The `MAJOR` version is used to indicate the family of technology represented by 
the helper library.  It increased from `5.x.x` to `6.x.x` when Twilio moved to 
auto generation of helper libraries.  Breaking changes that requires extensive 
reworking of code (like the `5.x.x` to `6.x.x` upgrade) will case the `MAJOR` 
version to be incremented by one, the `MINOR` and `PATCH` versions will be reset 
to zero.  Twilio understands that this can be very disruptive, we will only 
introduce this type of breaking change when absolutely necessary. New `MAJOR` 
versions will be communicated in advance with `Release Candidates` and a 
schedule.

## Supported Versions

`twilio-python` follows an evergreen model of support.  New features and 
functionality will only be added to the current version.  The current version - 
1 will continue to be supported with bugfixes and security updates, but no new 
features.

## Edge Features (alpha Branch)

Twilio frequently rolls out new features in public and private beta periods.
Twilio strives to ship early and often and bake customer feedback back into our 
products.  To support that mission, the `twilio-python` helper library has an 
`Edge` version based off the `alpha` branch.  This version is identified with an
`a` metadata tag on the version number.

The way the `Edge` artifact is created is by playing the `Edge` features on top
of our stable artifact.  The `Edge` artifact will always have the same version 
number as the stable artifact it was created from, but with an `a` suffix.

For example, `6.0.0a1` is the `6.0.0` branch with `Edge` features included.
If there is a change to one of the `Edge` features we may regenerate the `Edge`
artifact and release a new `6.0.0a2`, new `Edge` artifacts simply increment
the number after the `a` suffix.  All `Edge` features are considered
unstable and a backwards incompatible change in an `Edge` feature will not cause
any version change so you should take care when upgrading from one `a`
version to another.  

Once an `Edge` feature has matured it will be considered `Mainline` and included
in the stable artifact, with a `MAJOR` or `MINOR` version bump.

To use an `Edge` artifact in your PYTHON project you will have to make sure that 
you pin the artifact with `a` stability in your `setup.py` or `requirements.txt`.

[semver]: http://semver.org/
