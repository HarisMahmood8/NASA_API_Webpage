import requests

def fetch_apod(api_key):
    apod_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    try:
        response = requests.get(apod_url)
        response.raise_for_status()
        apod_data = response.json()
        return apod_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching APOD data: {e}")
        return None

def main():
    api_key = 'INSERT_API_LINK_HERE'

    apod_data = fetch_apod(api_key)

    if apod_data:
        print("Astronomy Picture of the Day")
        print("----------------------------")
        print(f"Title: {apod_data['title']}")
        print(f"Date: {apod_data['date']}")
        print(f"Description: {apod_data['explanation']}")
        print(f"Image URL: {apod_data['hdurl']}")
    else:
        print("Failed to fetch APOD data.")

if __name__ == "__main__":
    main()
