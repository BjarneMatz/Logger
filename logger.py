import time

# Color definitions
yellow = "\033[93m"
red = "\033[91m"
green = "\033[92m"
purple = "\033[95m"
gray = "\033[90m"

class Logger:
    def __init__(self, name: str) -> None:
        self.name = name
        self.path = f"logs/{name}.log".replace(" ", "_")
    def log(self, message: str, level: str = "info", type: str = "console") -> None:
        """Logging the given message with the given level either to the console or to a file.

        Args:
            message (str): The message to log.
            level (str, optional): What level (color) the log should have. Defaults to "info".
                0: info (gray)
                1: warning (yellow)
                2: error (red)
                3: success (green)
                4: debug (purple)
            type (str, optional): Defines the type of log. Defaults to "console".
        """
        if type == "console":
            if level == 0:
                print(f"{gray} [{self.name}] [INFO] {message}")
            elif level == 1:
                print(f"{yellow} [{self.name}] [WARNING] {message}")
            elif level == 2:
                print(f"{red} [{self.name}] [ERROR] {message}")
            elif level == 3:
                print(f"{green} [{self.name}] [SUCCESS] {message}")
            elif level == 4:
                print(f"{purple} [{self.name}] [DEBUG] {message}")
        elif type == "file":
            with open(self.path, "a") as file_data:
                if level == 0:
                    log = f"[{time.strftime('%H:%M:%S')}] [INFO] {message}"
                elif level == 1:
                    log = f"[{time.strftime('%H:%M:%S')}] [WARNING] {message}"
                elif level == 2:
                    log = f"[{time.strftime('%H:%M:%S')}] [ERROR] {message}"
                elif level == 3:
                    log = f"[{time.strftime('%H:%M:%S')}] [SUCCESS] {message}"
                elif level == 4:
                    log = f"[{time.strftime('%H:%M:%S')}] [DEBUG] {message}"
        else:
            raise ValueError("Invalid type of log.")
    def change_name(self, name: str) -> None:
        """Changes the name of the logger.

        Args:
            name (str): The new name of the logger.
        """
        self.name = name
        
    def change_path(self, path: str) -> None:
        """Changes the path of the logger.

        Args:
            path (str): The new path of the logger.
        """
        self.path = path
        
    def get_name(self) -> str:
        """Returns the name of the logger.

        Returns:
            str: The name of the logger.
        """
        return self.name
    
    def get_path(self) -> str:
        """Returns the path of the logger.

        Returns:
            str: The path of the logger.
        """
        return self.path