# GXpy

**GXpy** is the umbrella installation package for the Python **GX Simulator** ecosystem, developed within [SUNCAST](https://github.com/suncast-org).

GXpy installs a compatible collection of independent packages through one pip command. Scientific functionality resides in the component packages; GXpy itself provides no scientific library or `gxpy` import. The Python suite currently supports **active-region modeling**; flare modeling is not currently supported by this suite.

## Included packages

The descriptions below follow the linked component documentation.

| Package | Documented purpose | Python import |
| --- | --- | --- |
| [pyAMPP](https://github.com/suncast-org/pyAMPP) — Python Automatic Model Production Pipeline | Automates production of 3D solar atmosphere models, including HMI data retrieval, optional AIA context data, and potential/NLFFF magnetic-field extrapolation. | `pyampp` |
| [pyGXRender](https://github.com/kuznetsov-radio/gximagecomputing) | Computes 2D maps of solar microwave (gyroresonance and free-free) and EUV (spectral-line) emission from active-region models. | `gxrender` |
| [pyEUVTools](https://github.com/suncast-org/pyEUVTools) — EUV Instrument Response Tools | Builds, inspects, and exports EUV instrument-response products. | `pyeuvtools` |
| [pyCHMP](https://github.com/suncast-org/pyCHMP) — Python Coronal Heating Modeling Pipeline | Explores parameters of EBTEL-based magneto-thermal models to fit synthetic and observational maps. | `pychmp` |

Each package retains its own repository, documentation, license, and release cycle. Individual packages can also be installed separately.

## Install the first alpha

Use a dedicated **Python 3.12** environment. For example, with Conda:

```sh
conda create -n gxpy python=3.12 pip
conda activate gxpy
python -m pip install --upgrade pip
python -m pip install "gxpy==0.1.0a1"
python -m pip check
```

This is an alpha metapackage release. Its dependency ranges are recorded in [pyproject.toml](https://github.com/suncast-org/gxpy/blob/main/pyproject.toml). Pip selects releases satisfying those ranges and the components' own requirements; it may not select the newest individual release of every component.

To update GXpy and its dependencies within the declared ranges:

```sh
python -m pip install --upgrade --upgrade-strategy eager gxpy
```

Pip permits prerelease upgrades for an already installed prerelease. Later alpha versions can also be selected explicitly by version. Python 3.12 is the initial validation target; supported platforms additionally depend on the component wheels and GUI runtimes.

## Initial checks

```sh
python -c "import pyampp, gxrender, pyeuvtools, pychmp; print('GXpy component imports OK')"
pyampp
```

The second command opens the pyAMPP model-production GUI. These checks establish initial readiness, not completion of a scientific workflow.

Use the components directly in Python:

```python
import pyampp
import gxrender
import pyeuvtools
import pychmp
```

## EBTEL tables and other data

Pip installs the software. EBTEL tables, model cubes, and observation FITS files are separate downloads. No large datasets are fetched during GXpy installation.

Follow the [EBTEL setup instructions](https://github.com/suncast-org/gxpy/blob/main/docs/data.md) to download the tables from the public [pyGXrender-test-data](https://github.com/suncast-org/pyGXrender-test-data) releases. These tables can be used without an IDL or SolarSoft installation. The data repository also supplies optional model and observational datasets for study and validation.

## Compatibility and reproducibility

The first alpha starts from the published component combination tested during tutorial preparation: pyAMPP 1.0.2, pyGXRender 0.0.3.0, pyEUVTools 0.2.1, and pyCHMP 0.2.0 on Python 3.12. Bounds permit later component updates, including pyAMPP 1.0.6, but do not claim that every future release has already been tested.

For a reproducible study, record the resolved environment and the exact input datasets:

```sh
python -m pip freeze > requirements-resolved.txt
```

GXpy does not replace component citations. Follow the citation guidance in each component repository for scientific work.

## Development and releases

See [release instructions](https://github.com/suncast-org/gxpy/blob/main/docs/releasing.md). GXpy's own packaging and documentation are MIT licensed; component packages and datasets retain their respective licenses and attribution requirements.
