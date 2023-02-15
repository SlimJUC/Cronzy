import os
import re
import datetime

# Define a mapping between human-readable times and cron frequencies
time_map = {
    "every minute": "* * * * *",
    "once per hour": "0 * * * *",
    "once per day": "0 0 * * *",
    "twice per day": "0 0,12 * * *",
    "once per week": "0 0 * * 0",
    "once per month": "0 0 1 * *",
    "once per year": "0 0 1 1 *"
}

# Ask the user for the number of cron jobs to add
num_jobs = int(input("Enter the number of cron jobs to add: "))

# Initialize the list of cron jobs
cron_jobs = []

# Iterate over the number of jobs and ask the user for each job's details
for i in range(num_jobs):
    # Ask the user to input the command or file to execute as a cron job
    command = input(f"Enter the command or file to execute as cron job {i+1}: ")

    # Ask the user to input the frequency at which the cron job should run as a human-readable time
    frequency_str = input(f"Enter the frequency at which cron job {i+1} should run (e.g. 'once per day', 'every minute', 'every month'): ")

    # Convert the human-readable time to a cron frequency
    if frequency_str in time_map:
        frequency = time_map[frequency_str]
    else:
        print("Error: invalid frequency")
        exit()

    # Ask the user if they want to log the output of the command to a file or delete it with /dev/null
    log_output = input(f"Do you want to log the output of the command '{command}' to a file? (y/n): ")
    if log_output.lower() == "y":
        log_file = input("Enter the path and name of the log file: ")
        log_option = f">> {log_file} 2>&1"
    else:
        log_option = "> /dev/null 2>&1"

    # Append the new cron job to the list of cron jobs
    new_cron_job = f"{frequency} {command} {log_option}"
    cron_jobs.append(new_cron_job)

# Read the existing cron jobs from the crontab
existing_cron_jobs = os.popen('crontab -l').read().splitlines()

# Remove any existing instances of the new cron jobs
for i in range(num_jobs):
    existing_cron_jobs = [re.sub(f"{re.escape(command)}$", "", cron_job, flags=re.MULTILINE) for cron_job in existing_cron_jobs]

# Append the new cron jobs to the existing cron jobs
all_cron_jobs = existing_cron_jobs + cron_jobs

# Write all cron jobs to the temporary file
with open('/tmp/mycron', 'w') as file:
    file.write('\n'.join(all_cron_jobs) + '\n')

# Install the cron jobs
os.system("crontab /tmp/mycron")

print("Cron jobs have been created successfully!")
