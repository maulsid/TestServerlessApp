
class BaseRepository:
    def __init__(self, session, logger):
        self.session = session
        self.logger = logger
