import os
import sys
import logging


# Retrieve Job-defined env vars
TASK_INDEX = os.getenv("CLOUD_RUN_TASK_INDEX", 0)
TASK_ATTEMPT = os.getenv("CLOUD_RUN_TASK_ATTEMPT", 0)


def main():
    logging.info(f"Starting Task #{TASK_INDEX}, Attempt #{TASK_ATTEMPT}...")
    # main application code goes here
    logging.info(f"Completed Task #{TASK_INDEX}.")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logging.error("""Task #%s, Attempt #%s failed: %s""",
                      TASK_INDEX, TASK_ATTEMPT, str(err))
        sys.exit(1)  # Retry Job Task by exiting the process
