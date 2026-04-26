import json
import logging
from httpx import Response

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    GlobalUser,
)
from .api import Api


class Admin:
    """The class includes all necessary methods to access the Grafana admin API endpoints. Be aware that all functionalities inside the class only working with basic authentication (username and password) and that the authenticated user is a Grafana Admin.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_settings(self) -> dict:
        """The method includes a functionality to get the settings

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding settings
        """
        pass

    def update_settings(self, updates: dict = None, removals: dict = None):
        """The method includes a functionality to update the settings. Be aware that the functionality is a Grafana v8.0+ feature and you can find detailed information about the dict values here: https://grafana.com/docs/grafana/latest/developers/http_api/admin/#update-settings

        Args:
            updates (dict): Specify the updates object
            removals (dict): Specify the removals object

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_stats(self) -> dict:
        """The method includes a functionality to get the admin statistics

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding statistics
        """
        pass

    def get_preview_report(self) -> dict:
        """The method includes a functionality to get a preview report

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the preview report
        """
        pass

    def create_global_user(self, user: GlobalUser) -> int:
        """The method includes a functionality to create a global user

        Args:
            user (GlobalUser): Specify the global user object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the corresponding user id
        """
        pass

    def update_user_password(self, id: int, password: str):
        """The method includes a functionality to update the global user password

        Args:
            id (int): Specify the user id
            password (str): Specify the user new password

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_user_permissions(self, id: int, is_grafana_admin: bool = None):
        """The method includes a functionality to update the global user permissions

        Args:
            id (int): Specify the user id
            is_grafana_admin (bool): Specify if the user is admin or not

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_global_user(self, id: int):
        """The method includes a functionality to delete a global user

        Args:
            id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def pause_all_alerts(self):
        """The method includes a functionality to pause all alerts

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def unpause_all_alerts(self):
        """The method includes a functionality to unpause all alerts

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_user_auth_token(self, id: int) -> list:
        """The method includes a functionality to get the corresponding user auth token

        Args:
            id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the corresponding user auth tokens
        """
        pass

    def revoke_user_auth_token(self, id: int, auth_token_id: int):
        """The method includes a functionality to get the corresponding user auth token

        Args:
            id (int): Specify the user id
            auth_token_id (int): Specify the auth token id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def logout_user(self, id: int):
        """The method includes a functionality to log out the corresponding user

        Args:
            id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def reload_dashboards_provisioning_configuration(self):
        """The method includes a functionality to reload the dashboards provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def reload_datasources_provisioning_configuration(self):
        """The method includes a functionality to reload the datasources provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def reload_plugins_provisioning_configuration(self):
        """The method includes a functionality to reload the plugins provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def reload_notifications_provisioning_configuration(self):
        """The method includes a functionality to reload the notifications provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def reload_access_controls_provisioning_configuration(self):
        """The method includes a functionality to reload the access-controls provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def reload_ldap_configuration(self):
        """The method includes a functionality to reload the ldap configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def rotate_data_encryption_keys(self):
        """The method includes a functionality to rotate the data encryption keys

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
