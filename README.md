
# Cronzy - Cron Job Creation Wizard

Cronzy is a Python script that allows you to create cron jobs on a Linux system. The script asks the user for the details of the cron jobs to be created, including the command or file to execute, the frequency at which the job should run, and whether to log the output of the command to a file or delete it with /dev/null.

## Requirements

This script requires Python 3 and a Linux system with the `crontab` command installed.

## Usage

1. Open a terminal and navigate to the directory where the script is saved.

2. Run the script using the command `python3 cronzy.py`.

3. Follow the prompts to enter the details of the cron jobs to be created.

4. The script will create the new cron jobs and install them in the system's crontab.

5. The cron jobs will then run at the specified frequency.

Note: This script is not designed to modify existing cron jobs. If you need to modify or delete an existing cron job, you will need to do so manually using the `crontab -e` command.

## License

This script is released under the MIT License. See LICENSE for more details.

## Authors

This script was created by [Your Name Here]. If you have any questions or feedback, please feel free to contact me at [Your Email Here].
