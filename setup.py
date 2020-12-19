import setuptools

setuptools.setup(
    name="f-encrypt",
    version="1.0",
    include_package_data=True,
    packages=["fencrypt"],
    install_requires=["Click", "pycryptodome"],
    entry_points={
        "console_scripts": [
            "f-encrypt = fencrypt.entrypoint:encrypt",
            "f-decrypt = fencrypt.entrypoint:decrypt",
        ]
    },
)
