import requests
import argparse

def scan_file_paths(url, paths):
    for path in paths:
        # Construct the complete URL by combining the base URL and the path
        full_url = url + path

        # Send an HTTP HEAD request to the URL
        response = requests.head(full_url)

        # Check if the response status code is 200 (indicating the file exists)
        if response.status_code == 200:
            print(f"File found: {full_url}")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='File Path Scanning Tool')
parser.add_argument('-u', '--url', help='Base URL to scan')
parser.add_argument('-p', '--paths', nargs='+', help='Paths to scan')
args = parser.parse_args()

# Perform file path scanning if all required arguments are provided
if args.url and args.paths:
    scan_file_paths(args.url, args.paths)
else:
    print("Error: Missing required arguments. Please provide the base URL and at least one path to scan.")