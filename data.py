from flask import Flask, request
import requests
import json
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'MetEireann API is running'

@app.route('/get_data', methods=['GET', 'POST'])
def trigger_function():
    if request.method == 'POST':
        data = request.get_json()
        
    elif request.method == 'GET':
        data = request.args
    elif request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 204, headers
    

    start_date = data['start_date'].split('T')[0].replace('/', '-').replace('%2F', '-')
    start_time = data['start_date'].split('T')[1].replace('%3A', ':')
    end_date = data['end_date'].split('T')[0].replace('/', '-')
    end_time = data['end_date'].split('T')[1].replace('%3A', ':')
    station_id = data['station_id']

    url = f"https://wowapi.metweb.ie/graph/{station_id}?start_date={start_date}&start_time={start_time}&end_date={end_date}&end_time={end_time}"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    app.run()

'''
Sample POST request data, put it here to copy for testing
{
	"start_date":"2024/07/19T23:10",
  	"end_date":"2024/07/21T23:10",
	"station_id":"e04e0d31-3f5d-e911-b048-0003ff596eab"
}
'''