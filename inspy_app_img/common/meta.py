__all__ = [
    'AUTHORS',
    'PROG_NAME',
    'RELEASE_MAP',
    'SOFTWARE_ORG',
    'URLS',
    'VERSION'
]

PROG_NAME = 'InspyAppImg'

URLS = dict(
    developer_url='https://inspyre.tech',
    docs_url='https://InspyAppImg.readthedocs.io/en/latest',
    github_url='https://github.com/Inspyre-Softworks/',
    pypi_url='https://pypi.org/project/InspyAppImg',
)
"""The URLs used in the project."""

AUTHORS = [
    ('Inspyre-Softworks', URLS['developer_url']),
    ('Taylor-Jayde Blackstone', '<t.blackstone@inspyre.tech>')
]
"""The authors of the project."""

SOFTWARE_ORG, SOFTWARE_ORG_URL = AUTHORS[0]

RELEASE_MAP = {
    'dev': 'Development Build',
    'alpha': 'Alpha Build',
    'beta': 'Beta Build',
    'rc': 'Release Candidate Build',
    'final': 'Final Release Build'
}
"""The release map for the project."""

VERSION = {
    'major': 1,
    'minor': 0,
    'patch': 0,
    'release': 'dev',
    'release_num': 1
}
"""The version information for the project."""
