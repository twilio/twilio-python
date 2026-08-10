# Twilio Python SDK — Release Plan

## ci.yml (CI)

**Triggers:** PRs to main | Push to main | Manual dispatch | Cron (Monday 9AM IST)

### Jobs

1. **lockfile-hygiene** _(all triggers)_
   - Checkout
   - [`uv-lockfile-hygiene`](https://github.com/twilio/sdk-actions/blob/main/uv-lockfile-hygiene/action.yml) action (scan only, no clean-room install)
   - Fails if internal Artifactory hosts found in `requirements*.txt`

2. **test** (Python matrix) — _needs: lockfile-hygiene_ _(all triggers)_
   - Checkout
   - [Artifactory OIDC Auth](https://github.com/twilio/sdk-actions/tree/main/artifactory-oidc) (`ecosystem: python`)
   - Setup Python
   - `pip install virtualenv` + `make install test-install` + `make prettier`
   - `make test-with-coverage`
   - Cluster tests (`make cluster-test` with 7 secrets)
   - Verify docs generation (`make docs`)
   - Matrix: `3.12` on PRs/pushes, `[3.8–3.13]` on cron/manual with `all`

3. **deploy-dry-run** (Release Readiness Check - Build artifact) — _needs: test_ _(cron + manual dispatch only)_
   - Checkout
   - Artifactory OIDC Auth
   - Setup Python 3.12
   - Validate version format is semver (`X.Y.Z`)
   - Build sdist + wheel (`python -m build`)
   - Verify with `twine check dist/*`
   - List artifacts + print summary
   - **Does NOT publish**

---

## deploy.yml — Publish to PyPI

**Trigger:** Tag push matching `v*`

### How to release

1. Bump `version` in `setup.py`, merge to `main`
2. Tag and push: `git tag v9.0.1 && git push --tags`
3. Workflow fires automatically
4. Approve the `production` environment gate when prompted
5. Verify: `pip install twilio==9.0.1` + check attestations on pypi.org

### Jobs

1. **lockfile-hygiene**
   - Checkout
   - [`uv-lockfile-hygiene`](https://github.com/twilio/sdk-actions/blob/main/uv-lockfile-hygiene/action.yml) scan (no clean-room install)

2. **test** (Python 3.8–3.13 full matrix) — _needs: lockfile-hygiene_
   - Checkout
   - [Artifactory OIDC Auth](https://github.com/twilio/sdk-actions/tree/main/artifactory-oidc) (`ecosystem: python`)
   - Setup Python
   - `pip install virtualenv` + `make install test-install` + `make prettier`
   - `make test-with-coverage`

3. **deploy** (Publish to PyPI) — _needs: test, requires `production` env approval_
   - Checkout
   - Create GitHub Release (auto-generated notes)
   - Artifactory OIDC Auth
   - Setup Python 3.12
   - Validate tag format (`vX.Y.Z`) + matches `setup.py` version
   - Build sdist + wheel (`python -m build`)
   - Verify with `twine check dist/*`
   - Publish to PyPI (OIDC trusted publishing, PEP 740 attestations)

---

## End-to-end Release Day Flow

| Step | Action |
| --- | --- |
| Weekly | Monday cron runs CI workflow — confirms infra is healthy (full matrix + dry run) |
| On every PR | CI workflow runs lockfile-hygiene + test (3.12) + cluster tests + docs |
| 1 | [ **_Librarian_** ] PR: bump `setup.py` version, merge to `main` |
| 2 | [ **_Librarian_** ] `git tag vX.Y.Z && git push --tags` |
| 3 | `deploy.yml` fires automatically on tag creation, tests run (3.8–3.13) |
| 4 | [ **_Manual_** ] Approve `production` environment gate |
| 5 | GitHub Release created, package published to PyPI |
| 6 | [ **_Manual_** ] Verify: `pip install twilio==X.Y.Z` + check attestations on pypi.org |

---

## Platform Team Dependencies

| Dependency | Owner | Breaks if... |
| --- | --- | --- |
| Artifactory OIDC provider (`github-actions`) | SSC / Platform | Repo renamed, org changed, trust not configured |
| `vars.ARTIFACTORY_URL` | Repo admin | Variable not set or URL changes |
| `production` GitHub environment | Repo admin | Environment doesn't exist or approvals misconfigured |
| `ubuntu-x64` runner group | Enterprise admin | Repo not added to runner group, or runner pool down |
| PyPI trusted publisher | PyPI org admin | Not registered, or workflow filename / environment mismatch |
