import os
import requests
import datetime as dt

API_TOKEN = os.environ.get("TELEGRAM_API")
CHAT_ID = os.environ.get("CHAT_ID")


def _get_postcode() -> str:
    url = f"https://pickmypostcode.com/api/index.php/entry/ref/aHR0cHM6Ly9waWNrbXlwb3N0Y29kZS5jb20v/campaign/27079/cid/landing/?_={round(dt.datetime.now().timestamp())}"

    response = requests.get(url)

    postcode = response.json()["data"]["drawResults"]["main"]["result"]

    return postcode


def _send_message(
    token: str,
    chat_id: str,
    message: str,
) -> None:
    url = (
        f"https://api.telegram.org/bot{token}/sendMessage?text={message}&chat_id="
        + chat_id
    )

    try:
        requests.post(url)
    except Exception as e:
        raise Exception(f"Error sending message to Telegram: {e}")


def main() -> None:
    if not API_TOKEN or not CHAT_ID:
        raise ValueError("API_TOKEN or CHAT_ID not set")

    postcode = _get_postcode()

    _send_message(API_TOKEN, CHAT_ID, f"Today's postcode is {postcode}")


def lambda_handler(event, context):
    main()
