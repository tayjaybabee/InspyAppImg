import re
from inspy_app_img.version.errors import InvalidVersionStrError


RELEASE_MAP = {
    'dev': 'Development Build',
    'alpha': 'Alpha Build',
    'beta': 'Beta Build',
    'rc': 'Release Candidate Build',
    'final': 'Final Release Build'
}
"""The release map for the project."""


class VersionParser:
    def __init__(self, version_str):
        self.version_str = version_str
        self.version_info = self.parse_version()

    def parse_version(self):
        """
        Parses the version string into its components.

        Returns:
            dict: A dictionary containing the major, minor, patch, release, and release number.

        Raises:
            ValueError: If the version string format is grossly incorrect.
        """
        parts = self.version_str.split('-')
        version_numbers = parts[0].split('.')

        # Ensure there is at least one version number
        if len(version_numbers) == 0 or not all(num.isdigit() for num in version_numbers):
            raise ValueError("Version string format is incorrect. Expected format: X.Y.Z[-TYPE[.NUM]]")

        # Provide default values for major, minor, and patch
        major = int(version_numbers[0]) if len(version_numbers) > 0 else 0
        minor = int(version_numbers[1]) if len(version_numbers) > 1 else 0
        patch = int(version_numbers[2]) if len(version_numbers) > 2 else 0

        # Default values if no release type or number is specified
        release = 'final'
        release_num = 0

        if len(parts) > 1:
            release_info = parts[1]
            release_match = re.match(r'([a-zA-Z]+)(\d+)?', release_info)
            if release_match:
                release_type = release_match.group(1)
                release_num_str = release_match.group(2)

                # Convert short release type to full form if necessary
                release_type_full = {
                    'a': 'alpha',
                    'b': 'beta',
                    'rc': 'rc'
                }.get(release_type, release_type)

                release = RELEASE_MAP.get(release_type_full, release_type_full)

                if release_num_str:
                    release_num = int(release_num_str)

        return {
            'major': major,
            'minor': minor,
            'patch': patch,
            'release': release,
            'release_num': release_num
        }

    def _print_version(self):
        print(f"Major: {self.version_info['major']}")
        print(f"Minor: {self.version_info['minor']}")
        print(f"Patch: {self.version_info['patch']}")
        print(f"Release: {self.version_info['release']}")
        print(f"Release Num: {self.version_info['release_num']}")

    def print_version(self, skip_rich=False):
        if not skip_rich:

            def print_rich():
                from rich import print
                print(self)

            try:
                return print_rich()
            except ImportError:
                pass

        else:
            self._print_version()

    def __str__(self):
        return self.version_str

    def __repr__(self):
        return f"VersionParser('{self.version_str}\n')"

    def __rich__(self):
        from rich.table import Table
        from rich import box
        table = Table(box=box.SIMPLE)
        table.add_column('Major', justify='right', style='cyan')
        table.add_column('Minor', justify='right', style='magenta')
        table.add_column('Patch', justify='right', style='green')
        table.add_column('Release', justify='right', style='yellow')
        table.add_column('Release Num', justify='right', style='blue')
        table.add_row(str(self.version_info['major']), str(self.version_info['minor']), str(self.version_info['patch']), self.version_info['release'], str(self.version_info['release_num']))
        return table
