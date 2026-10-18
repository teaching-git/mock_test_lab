class FileService:
    def __init__(self, storage):
        self.storage = storage

    def save(self, data):
        try:
            self.storage.write(data)
            return "OK"
        except IOError:
            return "FAILED"
