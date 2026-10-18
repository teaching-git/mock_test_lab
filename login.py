class LoginService:
    def __init__(self, logger):
        self.logger = logger

    def login(self, username):
        self.logger.info(f"{username} logged in")
