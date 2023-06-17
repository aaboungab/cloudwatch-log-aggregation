# CloudWatch Logs Python Boto3 Sender

This Python script allows you to send logs to Amazon CloudWatch Logs using the `boto3` library. It creates or retrieves a log group and log streams within the group, reads log lines from specified log files, and sends them as log events to CloudWatch Logs.

## Prerequisites

- Python 3.x installed
- AWS SDK for Python (`boto3`) installed. You can install it using pip:
pip install boto3

## Setup

1. Import the required modules:
 ```python
 import boto3
 import time
``` 
2. Define the function send_logs_to_cloudwatch that handles sending logs to CloudWatch:
 ```python
(line 4 cloudwatch-log-send.py) def send_logs_to_cloudwatch(log_group_name, log_streams):
``` 
3. Set the CloudWatch Logs group name (log_group_name) and log streams with their respective log file paths (log_streams)
 ```python
log_group_name = '/test/logGroup'
log_streams = {
    'log-stream-1': '<path-to-file>',
    'log-stream-2': '<path-to-file>',
    'log-stream-3': '<path-to-file>'
}
``` 
4. Call the send_logs_to_cloudwatch function to start sending logs to CloudWatch
 ```python
send_logs_to_cloudwatch(log_group_name, log_streams)
```

Usage
1. Make sure you have proper AWS credentials configured on your system. You can set them up using the AWS CLI or by using environment variables:
   (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN).

2. Execute the script using Python
```python
python cloudwatch-log-send.py

python cloudwatch-log-send.py > dev/null 2>&1 # runs as a background process
```
Notes
* The script uses the boto3 library to interact with AWS services. Make sure it is installed and up to date.
* The log group will be created if it doesn't exist. If the log group already exists, it will be retrieved.
* Each log stream will be created if it doesn't exist. If a log stream already exists, it will be retrieved.
* Logs are read from the specified log files, and each line is sent as a log event to the corresponding log stream.
* The script uses a delay of 5 seconds between sending logs from each log stream. You can adjust this value as needed.
* Optional: Uncomment the print(f"send log stream: {log_stream_name}") line to display the response for debugging purposes. Run the program using the given systemd.service file to ensure systemd manages program
* Please ensure that you have the necessary permissions and configurations set up in your AWS account to successfully send logs to CloudWatch Logs.
