import json
import logging
import re

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class Alerting:
    """The class includes all necessary methods to access the Grafana legacy alerting API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alerts(
        self,
        custom_querystring: str = None,
    ) -> list:
        """The method includes a functionality to get the legacy alerts

        Args:
            custom_querystring (str): Specify the custom querystring (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of all alerts
        """
        pass

    def get_alerts_by_dashboard_ids(
        self,
        dashboard_ids: list,
    ) -> list:
        """The method includes a functionality to get legacy alerts specified by the dashboard ids

        Args:
            dashboard_ids (list): Specify the list of dashboard ids

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of alerts
        """
        pass

    def get_alert_by_id(self, id: int) -> dict:
        """The method includes a functionality to get the legacy alert specified by the alert id

        Args:
            id (int): Specify the id of the legacy alert

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns an alert
        """
        pass

    def pause_alert_by_id(self, id: int, paused: bool = True):
        """The method includes a functionality to pause/ unpause a legacy alert specified by the alert id

        Args:
            id (int): Specify the id of the legacy alert
            paused (bool): Specify the pause/ unpause parameter (default True)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
