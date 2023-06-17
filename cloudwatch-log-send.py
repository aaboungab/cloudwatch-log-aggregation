import boto3
import time

def send_logs_to_cloudwatch(log_group_name, log_streams):
    # Create a CloudWatch Logs client
    client = boto3.client('logs')

    # Create or retrieve the log group
    try:
        response = client.create_log_group(logGroupName=log_group_name)
    except client.exceptions.ResourceAlreadyExistsException:
        # Log group already exists, retrieve it
        response = client.describe_log_groups(logGroupNamePrefix=log_group_name)
        log_group = response['logGroups'][0]

    while True:
        for log_stream_name, log_file_path in log_streams.items():
            # Create a new log stream
            try:
                client.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)
            except client.exceptions.ResourceAlreadyExistsException:
                # Log stream already exists, retrieve it
                response = client.describe_log_streams(logGroupName=log_group_name, logStreamNamePrefix=log_stream_name)
                log_stream = response['logStreams'][0]

            # Read log lines from the file
            with open(log_file_path, 'r') as log_file:
                log_lines = log_file.readlines()

            # Put log events to the log stream
            log_events = []
            for log_line in log_lines:
                log_events.append({
                    'timestamp': int(time.time() * 1000),
                    'message': log_line.strip()
                })

            # Send log events
            kwargs = {
                'logGroupName': log_group_name,
                'logStreamName': log_stream_name,
                'logEvents': log_events
            }

            response = client.put_log_events(**kwargs)
            print(f"send log stream: {log_stream_name}")  # Optional: Print the response for debugging

            time.sleep(5)  # Delay for 5 seconds before sending logs from the next stream

# Set the CloudWatch Logs group name
log_group_name = 'log-group-kafka'

# Set the log streams and their respective log file paths
log_streams = {
    'log-stream-1': '<path-to-file>',
    'log-stream-2': '<path-to-file>',
    'log-stream-3': '<path-to-file>'
}

# Send logs to CloudWatch from each stream in intervals of 5 seconds
send_logs_to_cloudwatch(log_group_name, log_streams)
