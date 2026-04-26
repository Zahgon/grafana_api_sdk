import json
import logging
from typing import Union

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    SSOSetting,
)
from .api import Api


class SSOSettings:
    """The class includes all necessary methods to access the Grafana sso settings API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_sso_settings(self) -> list:
        """The method includes a functionality to get the SSO settings for all providers

        Required Permissions:
            Action: settings:read
            Scope: settings:auth.{provider}:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the all SSO settings
        """
        pass

    def get_sso_settings_by_provider(self, provider: str) -> dict:
        """The method includes a functionality to get the SSO settings for the specified provider

        Args:
            provider (str): Specify the provider

        Required Permissions:
            Action: settings:read
            Scope: settings:auth.{provider}:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding provider SSO settings
        """
        pass

    def update_sso_settings(self, provider: str, sso_setting: SSOSetting):
        """The method includes a functionality to update the SSO settings specified by the provider

         Args:
            provider (str): Specify the provider
            sso_setting (SSOSetting): Specify the SSO setting

        Required Permissions:
            Action: settings:write
            Scope: settings:auth.{provider}:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_sso_settings(self, provider: str):
        """The method includes a functionality to delete the SSO settings specified by the provider

         Args:
            provider (str): Specify the provider

        Required Permissions:
            Action: settings:write
            Scope: settings:auth.{provider}:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
