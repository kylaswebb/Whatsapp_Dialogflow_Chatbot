from http.client import responses
from flask import Flask
from flask import request, jsonify, Response
import os
from google.cloud import dialogflow_v2beta1 as dialogflow
from flask.globals import session
from google.api_core.exceptions import InvalidArgument
import requests
import twilio.twiml
from twilio.twiml.messaging_response import MessagingResponse

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
DIALOGFLOW_PROJECT_ID = 'whatsapp-twilio-flask-dia-svau'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def root():
    return "Hello World"

@app.route('/api/getMessage', methods=['POST'])
def home():
    message = request.form.get('Body')
    mobnum = request.form.get('From')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=message, language_code = DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    #knowledge_base_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
    #        DIALOGFLOW_PROJECT_ID, 'MTc2ODMyMzY2MDIzMTIxMzA1Ng'
    #    )
    #query_params = dialogflow.QueryParameters(
    #        knowledge_base_names=[knowledge_base_path]
    #    )

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)

        knowledge_answers = response.query_result.knowledge_answers
        for answers in knowledge_answers.answers:
            print(" - Answer: {}".format(answers.answer))
            print(" - Confidence: {}".format(answers.match_confidence))


    except InvalidArgument: # When an exception is raised, no further statements in the current block of code are executed.
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)

    responses = MessagingResponse()
    responses.message(response.query_result.fulfillment_text)
    return Response(str(responses), mimetype="application/xml")


if __name__ == '__main__':
    app.run()
