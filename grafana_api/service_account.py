import json
import logging

from .api import Api
from .model import APIModel, APIEndpoints, RequestsMethods


class ServiceAccount:
    """The class includes all necessary methods to access the Grafana service account API endpoints. Be aware that the functionality inside the class only works with basic authentication (username and password) and that the authenticated user is a Grafana Admin

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_service_account(
        self, results_per_page: int = 1000, pages: int = 1, query: str = None
    ) -> dict:
        """The method includes a functionality to get the service accounts specified by the optional pagination functionality

        Required Permissions:
            Action: serviceaccounts:read
            Scope: global:serviceaccounts:*

        Args:
            results_per_page (int): Specify the results_per_page as integer (default 1000)
            pages (int): Specify the pages as integer (default 1)
            query (str): Specify the query (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service accounts
        """
        pass

    def get_service_account_by_id(self, id: int) -> dict:
        """The method includes a functionality to get a service account specified by the id

        Required Permissions:
            Action: serviceaccounts:read
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service account
        """
        pass

    def create_service_account(self, name: str, role: str) -> dict:
        """The method includes a functionality to create a service account

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            name (str): Specify the name of the service account
            role (str): Specify the role of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the created service account
        """
        pass

    def update_service_account(self, id: int, name: str, role: str) -> dict:
        """The method includes a functionality to update a service account specified by the id, name and role

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account
            name (str): Specify the name of the service account
            role (str): Specify the role of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service account
        """
        pass

    def delete_service_account(self, id: int):
        """The method includes a functionality to delete a service account specified by the id

        Required Permissions:
            Action: serviceaccounts:delete
            Scope: serviceaccounts:id:*

        Args:
            id (int): Specify the id of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_service_account_tokens_by_id(self, id: int) -> list:
        """The method includes a functionality to get a service account tokens specified by the id

        Required Permissions:
            Action: serviceaccounts:read
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the service account tokens
        """
        pass

    def create_service_account_token_by_id(self, id: int, name: str, role: str) -> dict:
        """The method includes a functionality to create a service account token specified by the id

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account
            name (str): Specify the name of the service account
            role (str): Specify the role of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service account token
        """
        pass

    def delete_service_account_token_by_id(self, id: int, token_id: int):
        """The method includes a functionality to delete a service account token specified by the id

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account
            token_id (int):

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def migrate_api_keys_to_service_accounts(self):
        """The method includes a functionality to migrate all api keys to service accounts

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def migrate_api_key_to_service_account(self, key_id: int):
        """The method includes a functionality to migrate an api key to a service account specified by the key id

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            key_id (int): Specify the api key id of the api key

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_service_account_migration_status(self) -> bool:
        """The method includes a functionality to get the corresponding api key migration status

        Required Permissions:
            Action: serviceaccounts:read
            Scope: serviceaccounts:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the api key migration status
        """
        pass

    def hide_the_api_keys_tab(self):
        """The method includes a functionality to hide the api keys tab inside the UI

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def revert_service_account_token_to_api_key(self, id: int, key_id: int):
        """The method includes a functionality to revert a service account and transform it to the legacy api token specified by the service account id and the key id

        Required Permissions:
            Action: serviceaccounts:delete
            Scope: serviceaccounts:id:*

        Args:
            id (int): Specify the id of the service account
            key_id (int): Specify the api key id of the api key

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
