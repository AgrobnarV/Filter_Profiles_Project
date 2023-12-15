import argparse
import logging
from load_profiles import load_profiles
from filter_profiles import filter_profiles, experienced_python_dev
from save_result_profiles_to_file import save_results_to_file

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="CLI program to filter profiles based on conditions.")
    parser.add_argument("--filter", help="Choose filter function", required=True)
    parser.add_argument("--input", help="Input JSON file with profiles", required=True)
    parser.add_argument("--output", help="Output TXT file to save results")

    args = parser.parse_args()

    try:
        profiles = load_profiles(args.input)

        if args.filter == "experienced_python_dev":
            results = filter_profiles(experienced_python_dev, profiles)
        else:
            print("Invalid filter specified.")
            return

        for result in results:
            print(result[0])

        if args.output:
            save_results_to_file(results, args.output)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
