from fastapi import FastAPI, Request, status, HTTPException
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from pymongo import MongoClient
import os

client = MongoClient(os.getenv('MONGO_URI'))
db = client["comet-db"]
app = FastAPI()


@app.post("/register", status_code=status.HTTP_200_OK)
def register(name, password, profile_picture="default"):
  users = db["users"]

  if users.find_one({"name": name}):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                        detail="name already exists")
  users.insert_one({
      "name": name,
      "password": password,
      profile_picture: profile_picture,
      "meal_history": [],
      "nutrition_history": {
          "calorie": 0,
          "protein": 0,
          "fat": 0,
          "carbs": 0
      },
      "goals": {
          "calorie": 0,
          "protein": 0,
          "fat": 0,
          "carbs": 0
      }
  })
  return {"message": "created user"}


if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, reload=True)
