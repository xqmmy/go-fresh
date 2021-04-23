from ratelimit import limits

import requests

FIFTEEN_MINUTES = 900


@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response


if __name__ == "__main__":
    for i in range(20):
        call_api("http://www.baidu.com")