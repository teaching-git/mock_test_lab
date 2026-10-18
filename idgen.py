class IdGeneratorUser:
    def __init__(self, generator):
        self.generator = generator

    def create_three_ids(self):
        return [
            self.generator.next_id(),
            self.generator.next_id(),
            self.generator.next_id(),
        ]
