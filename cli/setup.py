from setuptools import setup

setup(
    name="kettle",
    version="1.0",
    description="Command line interface for the boilerplate",
    py_modules=["kettle"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "kettle=kettle:kettle",
        ],
    },
)
