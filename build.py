from setuptools_rust import RustExtension


def build(setup_kwargs: dict):
    """
    This function is mandatory in order to build the extensions
    """
    setup_kwargs.update({
        "rust_extensions": [RustExtension("comrak._comrak")],
    })
