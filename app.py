import numpy as np
import gradio as gr
import joblib
import asyncio

async def predict(pregnancies, glucose, bloodpressure, skinthickness, insulin,
       bmi, diabetespedigree, age):
    x = np.array([pregnancies, glucose, bloodpressure, skinthickness, insulin,
       bmi, diabetespedigree, age])
    model = joblib.load('lg_model.pkl')
    prediction = model.predict(x.reshape(1, -1))
    return await 'You have diabetes' if prediction == True else 'No diabetes detected'

output = gr.components.Textbox()
app = gr.Interface(fn=predict, inputs=['number','number','number','number','number','number','number','number'],
      outputs=output)

asyncio.run(app)
