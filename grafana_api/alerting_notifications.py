import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class AlertingNotifications:
    """The class includes all necessary methods to access the Grafana alerting notifications API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_notification_channels(self) -> list:
        """The method includes a functionality to get all alerting notification channels

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all notification channels
        """
        pass

    def get_all_notification_channels_lookup(self) -> list:
        """The method includes a functionality to lookup and get reduced information of all alerting notification channels

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all notification channels as reduced information
        """
        pass

    def get_notification_channel_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get an alerting notification channel specified by the uid

        Args:
            uid (str): Specify the uid of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the specified notification channel
        """
        pass

    def get_notification_channel_by_id(self, id: int) -> dict:
        """The method includes a functionality to get an alerting notification channel specified by the id

        Args:
            id (int): Specify the id of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the specified notification channel
        """
        pass

    def create_notification_channel(self, notification_channel: dict) -> dict:
        """The method includes a functionality to create an alerting notification channel specified by the notification channel dict

        Args:
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the newly created notification channel
        """
        pass

    def update_notification_channel_by_uid(
        self, uid: str, notification_channel: dict
    ) -> dict:
        """The method includes a functionality to update an alerting notification channel specified by the notification channel dict and the uid

        Args:
            uid (str): Specify the uid of the notification channel
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated notification channel
        """
        pass

    def update_notification_channel_by_id(
        self, id: int, notification_channel: dict
    ) -> dict:
        """The method includes a functionality to update an alerting notification channel specified by the notification channel dict and the id

        Args:
            id (int): Specify the id of the notification channel
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated notification channel
        """
        pass

    def delete_notification_channel_by_uid(self, uid: str):
        """The method includes a functionality to delete an alerting notification channel specified by the uid

        Args:
            uid (uid): Specify the uid of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_notification_channel_by_id(self, id: int):
        """The method includes a functionality to delete an alerting notification channel specified by the id

        Args:
            id (int): Specify the id of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def test_notification_channel(self, notification_channel: dict):
        """The method includes a functionality to test an alerting notification channel specified by the notification_channel

        Args:
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
