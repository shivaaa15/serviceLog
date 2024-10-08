import random
import pandas as pd
from persiantools.jdatetime import JalaliDate

# Define the parameters
jalali_years = [1402, 1403]
jalali_month_days = {
    1: 31, 2: 31, 3: 31, 4: 31, 5: 31, 6: 31,  # 31 days months
    7: 30, 8: 30, 9: 30, 10: 30, 11: 30,       # 30 days months
    12: 29                                       # 29 days in month 12
}
service_names = [f"service_{i}" for i in range(1, 51)]  # 50 random services
providers = ['sabtahval', 'naji', 'vezaratkeshvar', 'eadlir', 'sazmanbourse', 
             'taxgovir', 'eghtesad', 'tavnir', 'gas', 'abofazelab']  # 10 providers
consumers = [f"consumer_org_{i}" for i in range(1, 26)]  # 25 random consumer organizations
response_code_distribution = {
    '200-299': 60,  # 60% chance
    '300-399': 5,   # 5% chance
    '400-499': 20,  # 20% chance
    '500-599': 15   # 15% chance
}
response_code_ranges = {
    '200-299': range(200, 300),
    '300-399': range(300, 400),
    '400-499': range(400, 500),
    '500-599': range(500, 600)
}

# Function to generate a response code based on distribution
def get_response_code():
    rand = random.randint(1, 100)
    if rand <= 60:
        return random.choice(response_code_ranges['200-299'])
    elif rand <= 65:
        return random.choice(response_code_ranges['300-399'])
    elif rand <= 85:
        return random.choice(response_code_ranges['400-499'])
    else:
        return random.choice(response_code_ranges['500-599'])

# Function to generate daily service calls
def generate_daily_calls(jalali_year, jalali_month, jalali_day):
    num_calls = random.randint(400, 500)  # Ensure between 400-500 calls per day
    rows = []
    
    for _ in range(num_calls):
        service_name = random.choice(service_names)
        provider_name = random.choice(providers)  # One provider for many services
        consumer_name = random.choice(consumers)
        response_code = get_response_code()

        rows.append({
            'jalali_year': jalali_year,
            'jalali_month': jalali_month,
            'jalali_day': jalali_day,
            'service_name': service_name,
            'provider_name': provider_name,
            'consumer_name': consumer_name,
            'response_code': response_code
        })
    
    return rows

# Generate data for all years, months, and days
data = []
for year in jalali_years:
    for month, days_in_month in jalali_month_days.items():
        for day in range(1, days_in_month + 1):
            data.extend(generate_daily_calls(year, month, day))

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
output_file = "superset_dashboard_data.csv"
df.to_csv(output_file, index=False)

print(f"Data generation complete. The result has been saved to {output_file}.")

