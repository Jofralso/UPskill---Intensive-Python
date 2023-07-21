import json

def read_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_specific_values(data):
    values = [item['value'] for item in data['items']]
    return values

def modify_data(data):
    for item in data['items']:
        item['value'] *= 2

def generate_report(values):
    report = "Report: \n "
    for i, value in enumerate(values, start=1):
        report += f"{i}.{value}\n"
    return report


file_path = 'data.json'
data = read_json_data(file_path)

print("Data:", data)  # Debug print statement

specific_values = extract_specific_values(data)
print("Specific values:", specific_values)

modify_data(data)

report = generate_report(specific_values)
print(report)
