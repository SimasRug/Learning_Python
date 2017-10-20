internet_speed = 88 *1000000

size_in_bits = (10**18)*8
download_in_secs = size_in_bits /internet_speed
download_in_years = download_in_secs / 31557600


print(round(download_in_years))
