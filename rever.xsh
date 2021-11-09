$PROJECT = 'cython_fortran_file'
$ACTIVITIES = [
              'version_bump',  # Changes the version number in various source files (setup.py, __init__.py, etc)
              'tag',  # Creates a tag for the new version number
              'push_tag',  # Pushes the tag up to the $TAG_REMOTE
              'pypi',  # Sends the package to pypi
              # 'conda_forge',  # Creates a PR into your package's feedstock
              'ghrelease'  # Creates a Github release entry for the new tag
               ]
$VERSION_BUMP_PATTERNS = [  # These note where/how to find the version numbers
                         ('cython_fortran_file/__init__.py', '__version__\s*=.*', "__version__ = '$VERSION'"),
                         ('setup.cfg', 'version\s*=.*,', "version = '$VERSION',")
                         ]
$PUSH_TAG_REMOTE = 'git@github.com:cphyc/cython_fortran_file.git'  # Repo to push tags to

$GITHUB_ORG = 'cphyc'  # Github org for Github releases and conda-forge
$GITHUB_REPO = 'cython_fortran_file'  # Github repo for Github releases  and conda-forge
