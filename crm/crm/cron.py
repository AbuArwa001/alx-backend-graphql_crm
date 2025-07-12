import datetime
from itertools import product
import sys
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport, post



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


def update_low_stock():
    graphql_url = 'http://127.0.0.1:8000/graphql/'
    mutation = '''
    mutation {
        updateLowStockProducts {
            updatedProducts {
                id
                name
                stock
            }
            message
        }
    }
    '''
    transport = RequestsHTTPTransport(
        url=graphql_url,
        verify=False,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)
    try:
        response = client.execute(gql(mutation))
        print("Low stock products updated successfully:", response)
    except Exception as e:
        print(f"Error updating low stock products: {e}")
        sys.exit(1)
        raise ValueError(_("Price cannot be negative."))
    return product