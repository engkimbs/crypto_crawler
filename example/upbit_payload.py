import jwt
import uuid


# Press the green button in the gutter to run the script.
from config import UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY

if __name__ == '__main__':

    payload = {
        'access_key': UPBIT_ACCESS_KEY,
        'nonce': str(uuid.uuid4())
    }

    jwt_token = jwt.encode(payload, UPBIT_SECRET_KEY)
    authorization_token = 'Bearer {}'.format(jwt_token)
