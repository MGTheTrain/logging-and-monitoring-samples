# Reference: https://github.com/sleleko/devops-kb/blob/master/python/push-to-loki.py
import requests
import json
import datetime
import pytz
import argparse

def push_log(loki_url):
    curr_datetime = datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg'))
    curr_datetime = curr_datetime.isoformat('T')
    host = 'test-host'
    msg = f'On server {host} detected error'

    url = f'http://{loki_url}/api/prom/push'
    headers = {'Content-type': 'application/json'}

    payload = {
        'streams': [
            {
                'labels': f'{{source="test-loki",job="test-loki-job", host="{host}"}}',
                'entries': [
                    {
                        'ts': curr_datetime,
                        'line': '[WARN] ' + msg
                    }
                ]
            }
        ]
    }
    payload = json.dumps(payload)
    answer = requests.post(url, data=payload, headers=headers)
    print(answer)
    response = answer
    print(response)

def main():
    parser = argparse.ArgumentParser(description='Push logs to Loki')
    parser.add_argument('--loki-url', help='Specify the Loki URL (e.g., 192.168.99.100:3100)', required=True)
    args = parser.parse_args()

    push_log(args.loki_url)

if __name__ == '__main__':
    main()
