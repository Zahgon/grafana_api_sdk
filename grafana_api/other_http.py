import logging
from typing import Union
import asyncio

from httpx import AsyncClient, Client, BasicAuth, Response

import json

from .model import APIModel, APIEndpoints
from .api import Api


class OtherHTTP:
    """The class includes all necessary methods to access other Grafana API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_frontend_settings(self) -> dict:
        """The method includes a functionality to get the frontend settings

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding frontend settings
        """
        pass

    def renew_login_session_based_on_remember_cookie(self):
        """The method includes a functionality to renew the login session based on the remember cookie

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_health_status(self) -> dict:
        """The method includes a functionality to get the health information

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the health information
        """
        pass

    def get_metrics(
        self, basic_auth_username: str = None, basic_auth_password: str = None
    ) -> str:
        """The method includes a functionality to get the Grafana metrics information

        Args:
            basic_auth_username (str): Specify the optional basic auth username
            basic_auth_password (str): Specify the optional basic auth password

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the metrics information
        """
        pass

    def get_plugin_metrics(
        self,
        plugin_id: str,
        basic_auth_username: str = None,
        basic_auth_password: str = None,
    ) -> str:
        """The method includes a functionality to get the Grafana plugin metrics information

        Args:
            plugin_id (str): Specify the plugin id
            basic_auth_username (str): Specify the optional basic auth username
            basic_auth_password (str): Specify the optional basic auth password

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the metrics information
        """
        pass

    def _basic_get_call_without_token_auth(
        self, http: Union[Client, AsyncClient], url: str, basic_auth: BasicAuth = None
    ) -> Response:
        """The method includes a functionality to perform a basic GET call to an endpoint with optional BasicAuth

        Args:
            http (Union[Client, AsyncClient]): Specify the used client
            url (str): Specify the url of the performed api call
            basic_auth (BasicAuth): Specify the optional basic auth credentials (Default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (Response): Returns the corresponding result of the api call
        """
        pass
