import json
from isar.config.predefined_poses.predefined_poses import predefined_poses
from math import acos
from time import sleep
from isar.services.service_connections.request_handler import RequestHandler
from isar.services.auth.azure_credentials import AzureCredentials
from azure.identity import DefaultAzureCredential
import logging
from isar.config.settings import settings
from json import dumps
from requests import Response
from dotenv import load_dotenv
from requests.exceptions import HTTPError

def write_pose(body: dict):
    """
    Takes in a dictionary that contains info needed in the api to post pose
    """        

    client_id: str = settings.ECHO_CLIENT_ID
    scope: str = settings.ECHO_APP_SCOPE
    request_scope: str = f"{client_id}/{scope}"

    token: str = credentials.get_token(request_scope).token
    url: str = f"{settings.ECHO_API_URL}/robots/pose"
    body_json = dumps(body)

    # If 403 error. Try hardcoding token
    # token = ''
    headers = {"accept": "text/plain", "Authorization": f"Bearer {token}", "Content-Type": "text/json"}
    print(url,'\n')
    print(headers, '\n')
    print(body_json, '\n')
    try:
        response: Response = request_handler.post(
            url=url,
            headers=headers,
            data=body_json
        )
    except HTTPError as e:
        print(f"{body['tag']} has issues")

def prepare_pose_data():
    
    installation_code = 'JSV'
    tag = 'A-20PV1265A'
    description = '1ST STG SEPARATOR TRAIN 1 PRESSURISATION'

    body = {'installationCode': installation_code,
    'tag': tag,
    'name': description,
    'markerToolPosition': '',
    'position': {
        'e': 0,
        'n': 0,
        'u': 0
    },
    'lookDirectionNormalized': {
        'e': 0,
        'n': 0,
        'u': 0
    },
    'tiltDegClockwise': 0,
    'isDefault': True
    }

    print(installation_code,": ", tag)
    return body

def write_all_pre_poses():
    print("hello world")
    body = prepare_pose_data()
    write_pose(body)

if __name__=="__main__":
    load_dotenv()
    # setup_logger()
    request_handler: RequestHandler = RequestHandler()
    credentials: DefaultAzureCredential = (AzureCredentials.get_azure_credentials())
    logger = logging.getLogger("api")
    write_all_pre_poses()
