import logging
from typing import Union

import requests

logging.basicConfig(level=logging.INFO)


class NotifyCord:
    def __init__(
        self,
        discord_webhook_url: str,
        notification_message: Union[str, None] = None,
    ) -> None:
        self.discord_webhook_url = discord_webhook_url
        if notification_message is None:
            self.notification_message = "Finished your job!"
        else:
            self.notification_message = notification_message

    def send_complete_message(self) -> None:
        try:
            data = {"content": self.notification_message}
            response = requests.post(self.discord_webhook_url, data=data)
            response.raise_for_status()
            logging.info("Successfully transmitted to Discord!")
        except requests.exceptions.RequestException as e:
            logging.exception(e)
