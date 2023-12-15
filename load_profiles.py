import sys
import json
import logging
from typing import List
from profile_scheme import Profile

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def load_profiles(file_name: str) -> List[Profile]:
    try:
        logger.info(f"Loading profiles from file: {file_name}")
        with open(file_name, 'r') as file:
            profiles_data = json.load(file)
        logger.debug(f"Loaded {len(profiles_data)} profiles")
        return [Profile(**profile) for profile in profiles_data]
    except FileNotFoundError:
        logger.error(f"File not found: {file_name}")
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON in '{file_name}': {e}")
        print(f"Error decoding JSON in '{file_name}': {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error loading profiles from file: {e}")
        print(f"Error loading profiles from file: {e}")
        sys.exit(1)
