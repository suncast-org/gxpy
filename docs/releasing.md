# Releasing GXpy

## Initial PyPI setup

Configure a pending GitHub Trusted Publisher in the maintainer's [PyPI account publishing settings](https://pypi.org/manage/account/publishing/):

| Field | Value |
| --- | --- |
| PyPI project name | `gxpy` |
| Owner | `suncast-org` |
| Repository | `gxpy` |
| Workflow filename | `publish-pypi.yml` |
| Environment | `pypi` |

The workflow file is `.github/workflows/publish-pypi.yml`. Use the filename only in the PyPI form. Create the matching GitHub `pypi` environment. No PyPI API token needs to be stored in GitHub.

A pending publisher **does not reserve the PyPI name**. Only the first successful upload creates the project. See [PyPI's trusted-publishing instructions](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/).

## Release procedure

1. Update the version and dependency bounds in `pyproject.toml`, and update `CHANGELOG.md` and version-specific README examples.
2. Build and check distributions:

   ```sh
   python -m pip install build twine
   python -m build
   python -m twine check --strict dist/*
   ```

   Use a clean `dist` directory for each version.
3. Install the wheel with dependencies in a clean Python 3.12 environment, run `pip check` and `tools/smoke_check.py`, and inspect CI results on all three operating systems. Smoke checks do not replace scientific workflow validation.
4. Commit and tag the exact release version, for example `v0.1.0a1`.
5. Publish a GitHub release marked **prerelease** for an alpha. This triggers PyPI publication. Alternatively, dispatch the `Publish PyPI` workflow with the version tag.
6. Confirm the uploaded version on PyPI and install it in a new environment.

A version already uploaded to PyPI cannot be overwritten. Increment the version to correct artifacts.

## Dependency policy

The initial lower bounds reflect the component set used in the clean tutorial installation. Upper bounds keep the pre-1.0 dependencies within their current minor series and pyAMPP within major version 1. They are compatibility boundaries, not a guarantee about untested future versions. Update bounds deliberately as the components evolve.

The initial pyAMPP requirement accepts the planned 1.0.6 release when it becomes available. A new GXpy release is not necessary solely to make that version eligible. Existing users can use the documented eager upgrade command to update dependencies even when GXpy's own version has not changed.
