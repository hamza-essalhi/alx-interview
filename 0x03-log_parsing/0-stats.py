#!/usr/bin/env python3
import sys
import signal

# Dictionary to store the total file size and count of each status code
file_size_total = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_statistics():
    print(f"File size: {file_size_total}")
    for code in sorted(status_code_count):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")
    print()

# Register the signal handler for interrupt (Ctrl+C)
signal.signal(signal.SIGINT, lambda signal, frame: print_statistics())

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            ip, date, method, path, version, status_code, file_size = parts[0], parts[3][1:], parts[5][1:], parts[6], parts[8], int(parts[10]), int(parts[11])
            if method == "GET" and path == "/projects/260" and version == "HTTP/1.1":
                file_size_total += file_size
                status_code_count[status_code] += 1

                if line_count % 10 == 0:
                    print_statistics()

        except (ValueError, IndexError):
            # Skip lines with incorrect format
            pass

except KeyboardInterrupt:
    # Handle Ctrl+C interrupt and print final statistics
    print_statistics()
    sys.exit(0)

