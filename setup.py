# Import the setuptools library to handle packaging and distribution of the project
import setuptools

# Read the long description from the README file for displaying it on the project page (like PyPI)
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package
__version__ = "0.0.0"

# Basic metadata for the package
REPO_NAME = "Text-summarisation"            # GitHub repository name
AUTHOR_USER_NAME = "botcaps"               # Author's GitHub username
SRC_REPO = "text-summariszer"             # Source code repository name (usually same as project)
AUTHOR_EMAIL = "abhishek.7979883@gmail.com" # Contact email for project

# Call the setuptools.setup function to configure the package
setuptools.setup(
    name=SRC_REPO,                         # Package name
    version=__version__,                   # Current version of the package
    author=AUTHOR_USER_NAME,               # Author name
    author_email=AUTHOR_EMAIL,             # Author's email address
    description="A small python package for NLP app",  # Short description of the package
    long_description=long_description,     # Detailed description from README.md
    long_description_content_type="text/markdown",  # The format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # GitHub project link
    project_urls={                         # Additional project links (like issue tracker)
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},               # Tell setuptools where to find the packages (in the 'src' folder)
    packages=setuptools.find_packages(where="src"),  # Automatically find all packages inside 'src' directory
)
