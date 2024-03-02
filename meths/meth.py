import requests
import json

# Beautify the top
def banner():
    print("""\033[30;46m Simple IP OSINT (Open Source Intelligence) \033[0m\n""")
banner()

# Ask the IP that you want to extract
#ip = input("\033[30;43m Enter the Target IP \033[0m : ")

# We use the site ipinfo.io
def geoip(ip):
    url = "https://ipinfo.io/"+ip+"/json"
    response = requests.get(url)

    # If the generated status code is 200, the extraction was successful
    if response.status_code == 200:
        result = response.json()
        
        # Create a dictionary with the required information
        output = {
            "IP": result.get("ip"),
            "Hostname": result.get("hostname"),
            "Anycast": result.get("anycast"),
            "City": result.get("city"),
            "Region": result.get("region"),
            "Country": result.get("country"),
            "Location": result.get("loc"),
            "Organization": result.get("org"),
            "ZIP/Postal Code": result.get("postal"),
            "Time Zone": result.get("timezone")
        }
        
        # Print the output dictionary
        print(json.dumps(output, indent=4))
    else:
        # Unless the status code is 200, the extraction failed
        print("There is something wrong! The web is unreachable. HTTP Response:", response.status_code)
