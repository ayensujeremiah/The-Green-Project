from fastapi import FastAPI, File, UploadFile

import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL = tf.keras.models.load_model("saved_model")

CLASS_NAMES = ['battery', 
               'biological', 
               'clothes', 
               'glass', 
               'metal', 
               'paper', 
               'plastic', 
               'rubber', 
               'shoes', 
               'trash'
               ]


@app.get("/")
def read_root():
    return {"message": "Server started"}



def read_image_file(image_file) -> np.ndarray:
    image = np.array(Image.open(BytesIO(image_file)).resize((224,224)))

    image = image / 255.
    return image




@app.post("/predictions")
async def prediction(file: UploadFile = File(...)):
    image = read_image_file(await file.read())

    img_batch = tf.expand_dims(image, axis=0)
    predict = MODEL.predict(img_batch)
    
    predict_class = CLASS_NAMES[tf.argmax(predict[0])]

   

    return {"Close Category": predict_class}
   
    




