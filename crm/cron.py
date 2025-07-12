import datetime
import sys
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_entry = f"{timestamp} CRM is alive\n"
    log_path = "/tmp/crm_heartbeat_log.txt"

    # Log the heartbeat
    with open(log_path, "a") as log_file:
        log_file.write(log_entry)

    # Optional: Check GraphQL hello query
    try:
        response = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=False,
            retries=3,
        ).execute(gql("{ hello }"))
        if response:
            print("GraphQL endpoint is responsive.")
    except Exception as e:
        response = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=False,
            retries=3,
        ).execute(gql("{ hello }"))
        print(f"Error checking GraphQL endpoint: {e}")
        sys.exit(1)
        
    print("CRM heartbeat logged successfully.")