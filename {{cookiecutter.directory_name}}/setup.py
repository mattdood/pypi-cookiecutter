import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.1",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}",
    project_urls={
        "Bug Tracker": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "{{cookiecutter.project_name}}"},
    packages=setuptools.find_packages(where="{{cookiecutter.project_name}}"),
    package_data={},
    python_requires=">={{cookiecutter.min_python_version}}",
)
