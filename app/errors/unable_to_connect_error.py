class UnableToConnectError(Exception):
    def __init__(self):
        self.message = "Unable to connect"
        super().__init__(self.message)