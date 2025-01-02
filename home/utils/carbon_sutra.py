import requests

API_URL = "https://carbonsutra1.p.rapidapi.com/electricity_estimate"
API_KEY = "c530308ad6msh242ce5c350742d2p1bd135jsn99961a5f2d90"
AUTHORIZATION_TOKEN = "fQ98oU704xFvsnXcQLVDbpeCJHPglG1DcxiMLKfpeNEMGumlbzVf1lCI6ZBx"

def get_electricity_emission(electricity_usage_kwh):
    """
    Call Carbon Sutra API to estimate electricity usage emissions.
    :param electricity_usage_kwh: float, Electricity usage in kWh
    :return: float, estimated emissions in tonnes CO2
    """
    payload = {"country_name": "India",
               "electricity_value": electricity_usage_kwh,
               "electricity_unit": "kWh"
    }
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "carbonsutra1.p.rapidapi.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {AUTHORIZATION_TOKEN}"
    }

    try:
        response = requests.post(API_URL, data=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("emissions", 0)  # Emissions in tonnes
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return 0
    except Exception as e:
        print(f"Exception while calling API: {e}")
        return 0
