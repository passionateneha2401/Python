# Duplicate File Removal Automation

## Project Description

This project is a Python automation script that periodically scans a specified directory, identifies duplicate files using MD5 checksum, removes duplicate files, generates a log file, and sends the log file to the specified email address.

## Features

- Scans the specified directory recursively.
- Identifies duplicate files using MD5 checksum.
- Deletes duplicate files automatically.
- Generates a log file containing operation details.
- Sends the generated log file through email.
- Performs scanning periodically based on user-defined time interval.
- Supports command-line arguments.
- Validates directory path, time interval and email address.

## Software Requirements

- Python 3.x
- Internet Connection

## Python Modules Used

- os
- sys
- time
- hashlib
- schedule
- smtplib
- email

### Install Required Module

```bash
pip install schedule
```

## How to Run

Execute the program using the following command:

```bash
python3 Assignment33_1.py <DirectoryPath> <TimeInterval> <ReceiverEmail>
```

### Example

```bash
python3 Assignment33_1.py Marvellous 1 itsneha2024@gmail.com
```

## Command Line Arguments

| Argument      | Description                              |
|---------------|------------------------------------------|
| DirectoryPath | Directory to scan for duplicate files    |
| TimeInterval  | Time interval (in minutes) between scans |
| ReceiverEmail | Email address to receive the log file    |

## Help

```bash
python3 Assignment33_1.py --h
```

Displays the help information.

## Usage

```
bash
python3 Assignment33_1.py --u
```

Displays the correct syntax to execute the script.

## Log File Information

The generated log file contains:

- Starting time of directory scanning
- Completion time of directory scanning
- Directory name scanned
- Total number of files scanned
- Total duplicate files found
- Total duplicate files deleted
- Paths of deleted duplicate files
- MD5 checksum values
- Errors encountered during execution
- Email delivery status


## Email Configuration

The application uses Gmail SMTP server.

SMTP Server : smtp.gmail.com

Port : 587

Security : TLS

Authentication : Gmail App Password


## Validation Performed

- Checks whether the directory exists.
- Checks whether the given path is a directory.
- Checks directory read permission.
- Validates the time interval.
- Validates the receiver email address.


## Expected Output

- Duplicate files are detected.
- Duplicate files are deleted.
- Log file is generated automatically.
- Log file is sent to the specified email address.
- The process repeats after the specified time interval.


## Project Structure

```
Assignment33/
│
├── Assignment33_1.py
├── README.md
├── Marvellous/
│   ├── demo.txt
│   ├── demo1.txt
│   └── ...
└── Log Files

```

## Sample Execution

```bash
python3 Assignment33_1.py Marvellous 1 itsneha2024@gmail.com
```


## Author

Name : Neha Vilas Kumbhar

Assignment : Duplicate File Removal Automation

Language : Python

Date : 23/07/2026