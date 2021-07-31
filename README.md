# Whatsapp_Dialogflow_Chatbot

Hi all, here is the app.py file described in this video tutorial for setting up a Whatsapp_Twilio_Flask_Dialogflow_AWS Lambda (serverless). Some part of the code shown in the video was not working. For example, without 'from twilio.twiml.messaging_response import MessagingResponse' libraries, there is a schema validation warning (Warning - 12200).

In addition to what is mentioned in the video tutorial, I added a knowledge base intent detection using the line 'from google.cloud import dialogflow_v2beta1 as dialogflow'. Hence, the chatbot can return primary intent and also provide FAQ / QnA capabilities.

![Capture](https://user-images.githubusercontent.com/62549753/127736600-a9eb91e9-5ea6-4e4f-b8a9-6f88b0003899.JPG)
