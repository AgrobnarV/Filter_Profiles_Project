import logging
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def save_results_to_file(results: List[Tuple[str, bool, str]], file_name: str):
    try:
        logger.info(f"Saving results to file: {file_name}")
        with open(file_name, 'w') as file:
            for result in results:
                file.write(f"{result[0]}\n")
        logger.info(f"Results saved to file: {file_name}")
    except Exception as e:
        logger.error(f"Error saving results to file: {e}")
        print(f"Error saving results to file: {e}")
