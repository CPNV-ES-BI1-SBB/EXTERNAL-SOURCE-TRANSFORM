class UnableToReachServerError(Exception):
    def __init__(self):
        self.message = "Unable to reach server"
        super().__init__(self.message)