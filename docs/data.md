# EBTEL data setup

IDL and SolarSoft are not required for this download or for reading these tables in Python.

1. Open the [EBTEL release](https://github.com/suncast-org/pyGXrender-test-data/releases/tag/ebtel-gxsimulator-euv).
2. Download `ebtel_gxsimulator_euv.tar.gz` from **Assets** (about 83 MB). Do not use the automatically generated source-code archives.
3. In the download directory, extract it into a permanent data location:

   ```sh
   python -m tarfile -e ebtel_gxsimulator_euv.tar.gz ebtel_tables --filter data
   ```

The tables are under `ebtel_tables/ebtel_gxsimulator_euv/`. This bundle includes `ebtel.sav`, `ebtel_ss.sav`, and six heating-table variants. Choose the table appropriate to the scientific workflow; the following initial check uses `ebtel.sav`.

For a Conda environment, save its absolute path (replace the example with your actual path):

```sh
conda env config vars set GXIMAGECOMPUTING_EBTEL_PATH="/full/path/to/ebtel_tables/ebtel_gxsimulator_euv/ebtel.sav"
conda deactivate
conda activate gxpy
```

On Windows, use the corresponding quoted Windows path. Outside Conda, set `GXIMAGECOMPUTING_EBTEL_PATH` in your shell environment, or supply an explicit EBTEL path to the workflow you are using. The value must identify the file, not its directory.

Verify loading:

```sh
python -c "from gxrender.io.ebtel import resolve_ebtel_path, load_ebtel; p=resolve_ebtel_path(); load_ebtel(p); print('EBTEL table loaded:', p)"
```

For optional integrity verification, compare the archive's SHA-256 with `ebtel_gxsimulator_euv.bundle.sha256` from the same release:

```sh
python -c "import hashlib; print(hashlib.file_digest(open('ebtel_gxsimulator_euv.tar.gz', 'rb'), 'sha256').hexdigest())"
```

The test-data repository also hosts completed models and observational maps. Download only the assets required by your exercise; cloning the repository does not download the release datasets.
