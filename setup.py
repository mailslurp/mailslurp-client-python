
from setuptools import setup, find_packages 

NAME = "mailslurp-client"
VERSION = "7.0.9"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="MailSlurp API",
    author="MailSlurp",
    author_email="contact@mailslurp.dev",
    url="https://www.mailslurp.com",
    keywords=["MailSlurp", "Email", "SMTP", "Mailer", "MailSlurp API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""Create email addresses in Python then send and receive emails and attachments. See https://www.mailslurp.com/docs/python/ for full documentation."""
)
