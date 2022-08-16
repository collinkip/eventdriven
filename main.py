from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host='redis-10696.c59.eu-west-1-2.ec2.cloud.redislabs.com',
    port=10696,
    password='ewkKfWeFMOTt5rOHtRRcY7yRI9LOBFIa',
    decode_responses=True
)


class Delivery(HashModel):
    budget: int = 0
    notes: str = ''

    class Meta:
        database = redis


class Event(HashModel):
    deliveryId: str = None
    type: str
    data: str

    class Meta:
        database = redis

@app.post('/deliveries/create')
async def create(request:Request):
    body =await request.json()
    delivery=Delivery(budget=body['data']['budget'],notes=body['data']['budget']).save()
    return delivery



