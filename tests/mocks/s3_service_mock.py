from tests.initial_data_example import get_initial_data_example

class S3ServiceMock:
    def __init__(self):
        self.data = get_initial_data_example()

    def load(self):
        return self.data