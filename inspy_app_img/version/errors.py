"""


Author: 
    Inspyre Softworks

Project:
    InspyAppImg

File: 
    inspy_app_img/version/errors.py
 

Description:
    

"""


class InvalidVersionStrError(ValueError):
    def __init__(self, version_str):
        self.version_str = version_str
        self.message = f'Invalid version string: {version_str}'
        super().__init__(self.message)
