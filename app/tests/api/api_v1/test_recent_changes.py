import json

import requests


def test_get_user_json_recent_changes():
    url = 'http://localhost:8080/api/v1/recent_changes/json'
    r = requests.post(url, stream=True, json={'users': ['DPLA bot', 'SuccuBot']})
    assert r.status_code == 200
    for i, line in enumerate(r.iter_lines()):
        json.loads(line)
        if i == 2:
            break


def test_get_user_contributions_over_time():
    url = 'http://localhost:8080/api/v1/contributions/stats_over_time'
    r = requests.post(url, json={'user': "Jimbo Wales",
                                 "interval": 86400})
    r.json()
    assert r.status_code == 200
