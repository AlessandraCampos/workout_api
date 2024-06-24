from fastapi import FastAPI 
from fastapi_pagination import add_pagination

app = FastAPI(title='WorkoutApi')


add_pagination(app)





