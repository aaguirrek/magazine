from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in magazine/__init__.py
from magazine import __version__ as version

setup(
	name="magazine",
	version=version,
	description="Magazine",
	author="Peru Intercorp",
	author_email="admin@peruintercorp.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
