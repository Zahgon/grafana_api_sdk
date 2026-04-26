import logging
import json
import base64
from typing import Union

import httpx
from httpx import ConnectError
import asyncio

from .model import RequestsMethods, ERROR_MESSAGES, APIModel


class Api:
    """The class includes all necessary methods to make API calls to the Grafana API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def call_the_api(
        self,
        api_call: str,
        method: RequestsMethods = RequestsMethods.GET,
        json_complete: str = None,
        org_id_header: int = None,
        disable_provenance_header: bool = False,
        response_status_code: bool = False,
    ) -> any:
        """The method execute a defined API call against the Grafana endpoints

        Args:
            api_call (str): Specify the API call endpoint
            method (RequestsMethods): Specify the used method (default GET)
            json_complete (str): Specify the inserted JSON as string
            org_id_header (int): Specify the optional organization id as header for the corresponding API call
            disable_provenance_header (bool): Specify the optional disable provenance as header for the corresponding API call (default False)
            response_status_code (bool): Specify if the response should include the original status code (default False)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """
        pass

    def _execute_the_api_call(
        self,
        http: httpx.Client,
        method: RequestsMethods,
        api_url: str,
        response_status_code: bool,
        json_complete: str,
    ) -> any:
        """The method includes a functionality to execute a synchronous api call

        Args:
            http (httpx.Client): Specify the used synchronous client
            method (RequestsMethods): Specify the used method
            api_url (str): Specify the used api url
            response_status_code (bool): Specify if the response code should be returned
            json_complete (str): Specify the forwarded json in case of patch, post or put calls

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """
        pass

    async def _execute_the_async_api_call(
        self,
        http: httpx.AsyncClient,
        method: RequestsMethods,
        api_url: str,
        response_status_code: bool,
        json_complete: str,
    ):
        """The method includes a functionality to execute an asynchronous api call

        Args:
            http (httpx.AsyncClient): Specify the used asynchronous client
            method (RequestsMethods): Specify the used method
            api_url (str): Specify the used api url
            response_status_code (bool): Specify if the response code should be returned
            json_complete (str): Specify the forwarded json in case of patch, post or put calls

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """
        pass

    @staticmethod
    def _check_the_api_call_response(
        response: any = None, response_status_code: bool = False
    ) -> any:
        """The method includes a functionality to check the output of API call method for errors

        Args:
            response (any): Specify the inserted response
            response_status_code (bool): Specify if the original status code should be attached to the result (default False)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """
        pass

    @staticmethod
    def _check_if_valid_json(response: str) -> bool:
        """The method includes a functionality to check if the response json is valid

        Args:
            response (str): Specify the inserted response json as string

        Returns:
            result (bool): Returns if the json is valid or not
        """
        pass

    @staticmethod
    def prepare_api_string(query_string: str) -> str:
        """The method includes a functionality to prepare the api string for the queries

        Args:
            query_string (str): Specify the corresponding query string

        Returns:
            query_string (str): Returns the adjusted query string
        """
        pass

    def create_the_http_api_client(
        self, headers: dict = None
    ) -> Union[httpx.Client, httpx.AsyncClient]:
        """The method includes a functionality to create the corresponding HTTP client

        Args:
            headers (dict): Specify the optional inserted headers (Default None)

        Returns:
            client (Union[httpx.Client, httpx.AsyncClient]): Returns the corresponding client
        """
        pass
