import requests 
import datetime
import reverse_geocoder as rg



URL = "http://api.open-notify.org/iss-now.json"
def main():
    iss = requests.get(URL).json()

    dt = datetime.datetime.fromtimestamp(iss['timestamp'])
    lat = iss['iss_position']['latitude']
    lon = iss['iss_position']['longitude']
    coords = (lat, lon)

    pos = rg.search(coords, verbose=False)
    pos_name = pos[0]['name'] + ", " + pos[0]['admin1']
    # print(pos)

    print("Location of the ISS at " + str(dt) +  "\nLon: " + str(lon) + "\nLat: " + str(lat) + "\nPlace on Earth: " + pos_name) 

if __name__== "__main__":
    main()
