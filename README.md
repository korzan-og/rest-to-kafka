# rest-to-kafka

python3 -m venv angelovenv

source angelovenv/bin/activate

pip install -r requirements.tx

flask --app app run

end points are :

healtcheck : 
GET /health/ping

post items:
POST /items
Example JSON : 

{
    "key" : "ThisIsRequiredKey",
    "body" : "Anything could go into the json object"
}
