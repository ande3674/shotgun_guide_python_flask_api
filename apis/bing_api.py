import geocoder

KEY = 'Ajz2DvCoZshEaHtbHAuNFoosVjYb-Gwihd2GoSRNjFT3se0pSy0K27xUp1epc5kY'

def reverse_geocode_place(lat, lon):
    l = [lat, lon]
    place = geocoder.bing(l, method='reverse', key=KEY)
    return place.city + ", " + place.state + ", " + place.country

#p = reverse_geocode_place(44.9778, 93.2650)
#print(p)