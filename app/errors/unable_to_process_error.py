class UnableToProcessError(Exception):
    def __init__(self):
        self.message = "Unable to transform"
        super().__init__(self.message)