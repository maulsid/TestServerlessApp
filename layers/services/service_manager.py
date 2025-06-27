
class ServiceManager:
    @staticmethod
    def get_logger():
        import logging
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
