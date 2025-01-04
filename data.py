import requests as rq

parameters = {
    "amount":10,
    "type":"boolean",
}

db = rq.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
db.raise_for_status()
data = db.json()
question_data = data["results"]