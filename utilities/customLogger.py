import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:

            log_path = r"C:\Users\divya aghi\PycharmProjects\DesigningFramework\Logs"
            os.makedirs(log_path, exist_ok=True)

            fh = logging.FileHandler(os.path.join(log_path, "automation.log"), mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger
