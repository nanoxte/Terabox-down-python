import requests

def get_details(id):
    try:
        response = requests.get(f"https://terabox-app-pearl.vercel.app/api?data={id}")
        return response.json()
    except Exception as e:
        print(e)
