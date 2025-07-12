from celery import shared_task
from datetime import datetime
import requests
import json

@shared_task
def generate_crm_report():
    query = '''
    query {
        totalCustomers
        totalOrders
        totalRevenue
    }
    '''

    try:
        response = requests.post(
            'http://localhost:8000/graphql/',
            json={'query': query},
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            data = response.json().get('data', {})
            customers = data.get('totalCustomers', 0)
            orders = data.get('totalOrders', 0)
            revenue = data.get('totalRevenue', 0.0)

            log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Report: {customers} customers, {orders} orders, {revenue} revenue\n"
            with open('/tmp/crm_report_log.txt', 'a') as log_file:
                log_file.write(log_line)
        else:
            raise Exception(f"GraphQL error: {response.status_code}")
    except Exception as e:
        with open('/tmp/crm_report_log.txt', 'a') as log_file:
            log_file.write(f"{datetime.now()} - Failed to generate report: {e}\n")
    else:
        print("CRM report generated successfully.")
    finally:
        print("Task completed.")
        print(f"Response: {response.text}")
        return response.json()