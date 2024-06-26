from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="weatherpred",
    version="1.0.0",
    description="Weather prediction project using seasonality",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/cgp9900/Weather-Prediction",
    author="Cole Parker",
    author_email="cgp9900@gmail.com",
    keywords="weather prediction project",
    license="MIT",
    packages=["weather"],
    install_requires=["pandas", "numpy"],
    include_package_data=True,
)
