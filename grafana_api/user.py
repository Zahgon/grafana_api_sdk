import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    UserObject,
)
from .api import Api


class User:
    """The class includes all necessary methods to access the Grafana user API endpoints. Be aware that all functionalities inside the class only working with basic authentication (username and password) and that the authenticated user is a Grafana Admin.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_users(
        self,
        results_per_page: int = 1000,
        page: int = 1,
        sort: str = None,
    ) -> list:
        """The method includes a functionality to get all Grafana system users specified by the optional results_per_page, page and sort option

        Required Permissions:
            Action: users:read
            Scope: global.users:*

        Args:
            results_per_page (int): Specify the results_per_page as integer (default 1000)
            page (int): Specify the page as integer (default 1)
            sort (str): Specify the sort option. Valid values are login-asc, login-desc, email-asc, email-desc, name-asc, name-desc, lastSeenAtAge-asc and lastSeenAtAge-desc. By default, if sort is not specified, the user list will be ordered by login, email in ascending order (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Grafana users
        """
        pass

    def search_users_with_paging(
        self,
        results_per_page: int = 1000,
        page: int = 1,
        query: str = None,
        sort: str = None,
    ) -> dict:
        """The method includes a functionality to get all Grafana system users specified by the optional results_per_page, page, query, sort and general paging functionality

        Required Permissions:
            Action: users:read
            Scope: global.users:*

        Args:
            results_per_page (int): Specify the results_per_page as integer (default 1000)
            page (int): Specify the page as integer (default 1)
            query (str): Specify the query (default None)
            sort (str): Specify the sort option. Valid values are login-asc, login-desc, email-asc, email-desc, name-asc, name-desc, lastSeenAtAge-asc and lastSeenAtAge-desc. By default, if sort is not specified, the user list will be ordered by login, email in ascending order (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the Grafana users
        """
        pass

    def get_user_by_id(self, id: int) -> dict:
        """The method includes a functionality to get a specific user by the id

        Required Permissions:
            Action: users:read
            Scope: users:*

        Args:
            id (int): Specify the id of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the user information
        """
        pass

    def get_user_by_username_or_email(self, username_or_email: str) -> dict:
        """The method includes a functionality to get a specific user by the username_or_email

        Required Permissions:
            Action: users:read
            Scope: global.users:*

        Args:
            username_or_email (str): Specify the username_or_email of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the user information
        """
        pass

    def update_user(self, id: int, user: UserObject):
        """The method includes a functionality to update the specified user

        Required Permissions:
            Action: users:write
            Scope: users:*

        Args:
            id (int): Specify the id of the user
            user (UserObject): Specify the used UserObject

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_user_organizations(self, id: int) -> list:
        """The method includes a functionality to get the specified user organizations

        Required Permissions:
            Action: users:read
            Scope: users:*

        Args:
            id (int): Specify the id of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of the user bound organizations
        """
        pass

    def get_user_teams(self, id: int) -> list:
        """The method includes a functionality to get the specified user teams

        Required Permissions:
            Action: users.teams:read
            Scope: users:*

        Args:
            id (int): Specify the id of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of the user bound teams
        """
        pass

    def switch_specific_user_context(self, user_id: int, org_id: int):
        """The method includes a functionality to switch the user context to the given organization

        Args:
            user_id (int): Specify the user_id
            org_id (int): Specify the org_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass


class CurrentUser:
    """The class includes all necessary methods to access the Grafana current user API endpoints. Be aware that all functionalities inside the class maybe only working with basic authentication (username and password)

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_user(self) -> dict:
        """The method includes a functionality to get the current user

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the user information
        """
        pass

    def update_password(
        self, old_password: str, new_password: str, confirm_new_password: str
    ):
        """The method includes a functionality to update the current user password

        Args:
            old_password (str): Specify the old_password
            new_password (str): Specify the new_password
            confirm_new_password (str): Specify the confirm_new_password

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def switch_current_user_context(self, org_id: int):
        """The method includes a functionality to switch the current user context to the given organization

        Args:
            org_id (int): Specify the organization id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_user_organizations(self) -> list:
        """The method includes a functionality to get the current user organizations

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of organizations
        """
        pass

    def get_user_teams(self) -> list:
        """The method includes a functionality to get the current user teams

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of teams
        """
        pass

    def star_a_dashboard(self, dashboard_id: int):
        """The method includes a functionality to star a dashboard for the current user

        Args:
            dashboard_id (int): Specify the dashboard id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def unstar_a_dashboard(self, dashboard_id: int):
        """The method includes a functionality to unstar a dashboard for the current user

        Args:
            dashboard_id (int): Specify the dashboard id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_auth_tokens(self) -> list:
        """The method includes a functionality to get the auth tokens for the current user

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of auth tokens of the current user
        """
        pass

    def revoke_auth_token(self, auth_token_id: int):
        """The method includes a functionality to revoke a specified auth token of the current user

        Args:
            auth_token_id (int): Specify the auth_token_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
