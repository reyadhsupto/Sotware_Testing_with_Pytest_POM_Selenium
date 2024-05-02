import logging
import os

directory = r"E:\Internship\SDET_selenium\Sotware_Testing_with_Pytest_POM_Selenium\Logs"
filename = "automation.log"

# Construct the full file path
full_path = os.path.join(directory, filename)

# Normalize the path
normalized_path = os.path.normpath(full_path)
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename = normalized_path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger