try:
    from setuptools_rust import RustExtension
except ImportError:
    import subprocess
    import sys

    errno = subprocess.call(
        [sys.executable, "-m", "pip", "install", "setuptools-rust"])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import RustExtension


def build(setup_kwargs: dict):
    """
    This function is mandatory in order to build the extensions
    """
    setup_kwargs.pop('package_data', None)  # fix wrong 'package_data'
    setup_kwargs.update({
        'setup_requires': ['setuptools-rust>=0.10.1', 'wheel'],
        'rust_extensions': [RustExtension('comrak._comrak')],
    })
