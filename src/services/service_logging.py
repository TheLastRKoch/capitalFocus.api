from services.service_time import ServiceTime


class LoggingService:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    LIGHTBLUE = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    UNDERLINE = '\033[4m'
    COMMON = '\033[0m'

    @classmethod
    def custom_log(self, message, level, color):
        timestamp = ServiceTime.get_time_standard()
        print(color, "{"+f" {timestamp} | {level} | {message} "+"}")

    @classmethod
    def trace(self, message):
        self.custom_log(message, "Trace", self.UNDERLINE)

    @classmethod
    def info(self, message):
        self.custom_log(message, "Information", self.COMMON)

    @classmethod
    def alert(self, message):
        self.custom_log(message, "Warning", self.YELLOW)

    @classmethod
    def error(self, message):
        self.custom_log(message, "Error", self.RED)
