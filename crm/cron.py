import datetime
import requests

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_entry = f"{timestamp} CRM is alive\n"
    log_path = "/tmp/crm_heartbeat_log.txt"

    # Log the heartbeat
    with open(log_path, "a") as log_file:
        log_file.write(log_entry)

    # Optional: Check GraphQL hello query
    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        if response.ok:
            print("GraphQL endpoint responded:", response.json())
        else:
            print("GraphQL query failed:", response.status_code)
    except Exception as e:
        print("GraphQL heartbeat check failed:", e)
    print("CRM heartbeat logged successfully.")