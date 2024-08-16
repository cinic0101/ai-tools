
class Version:
    V1 = 1
    V2 = 2


class Versioning:
    version: Version
    version_behaviors: dict[str, str]

    def __init__(self, version: Version):
        self.version = version
