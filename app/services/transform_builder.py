class TransformBuilder:
    def __init__(self, data):
        self.data = data
        self.transformed_data = {}

    def build(self):
        raise NotImplementedError

    def set_initial_station(self):
        raise NotImplementedError

    def set_departures_station(self):
        raise NotImplementedError

    def get_transformed_data(self):
        return self.transformed_data