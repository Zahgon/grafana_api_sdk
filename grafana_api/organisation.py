import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class Organisation:
    """The class includes all necessary methods to access the Grafana organisation API endpoint

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_current_organization(self) -> dict:
        """The method includes a functionality to get the current organization

        Required Permissions:
            Action: orgs:read
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the current organization
        """
        pass

    def get_all_users_by_the_current_organization(self) -> list:
        """The method includes a functionality to get all users from the current organization

        Required Permissions:
            Action: org.users:read
            Scope: users:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the users of the current organization
        """
        pass

    def get_all_users_by_the_current_organization_lookup(self) -> list:
        """The method includes a functionality to get the lookup information of all users from the current organization

        Required Permissions:
            Action: org.users:read
            Scope: users:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the users of the current organization
        """
        pass

    def update_organization_user_role_by_user_id(self, user_id: int, role: str):
        """The method includes a functionality to update the current organization user by the user id

        Args:
            user_id (int): Specify the id of the user
            role (str): Specify the role of the user

        Required Permissions:
            Action: org.users.role:update
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_organization_user_by_user_id(self, user_id: int):
        """The method includes a functionality to delete the current organization user by the user id

        Args:
            user_id (int): Specify the id of the user

        Required Permissions:
            Action: org.users:remove
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_current_organization(self, name: str):
        """The method includes a functionality to update the current organization

        Args:
            name (str): Specify the new name of the current organization

        Required Permissions:
            Action: orgs:write
            Scope: N/A

        Raises
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def add_new_user_to_current_organization(
        self, login_or_email: str, role: str
    ) -> int:
        """The method includes a functionality to add a new user to the current organization

        Args:
            login_or_email (str): Specify the added user
            role (str): Specify the added role for the user

        Required Permissions:
            Action: org.users:add
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            user_id (int): Returns the id of the created user
        """
        pass


class OrganisationAdmin:
    """The class includes all necessary methods to access the Grafana organisation Admin API endpoint. Be aware that all functionalities inside the class only working with basic authentication (username and password)

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_organization_by_id(self, org_id: int) -> dict:
        """The method includes a functionality to get an organization by the id

        Args:
            org_id (int): Specify the organization id

        Required Permissions:
            Action: orgs:read
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization as dict
        """
        pass

    def get_organization_by_name(self, name: str) -> dict:
        """The method includes a functionality to get an organization by the name

        Args:
            name (str): Specify the organization name

        Required Permissions:
            Action: orgs:read
            Scope: N/A
            Note: Needs to be assigned globally.

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization as dict
        """
        pass

    def get_organizations(self) -> list:
        """The method includes a functionality to get all organizations

        Required Permissions:
            Action: orgs:read
            Scope: N/A
            Note: Needs to be assigned globally.

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
             api_call (list): Returns all organizations as list
        """
        pass

    def create_organization(self, name: str) -> int:
        """The method includes a functionality to create an organization

        Args:
            name (str): Specify the organization name

        Required Permissions:
            Action: orgs:create
            Scope: N/A
            Note: Needs to be assigned globally.

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            org_id (int): Returns the id of the created organization
        """
        pass

    def update_organization(self, org_id: int, name: str):
        """The method includes a functionality to update an organization

        Args:
            org_id (int): Specify the organization id
            name (str): Specify the organization name

        Required Permissions:
            Action: orgs:write
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_organization(self, org_id: int):
        """The method includes a functionality to delete an organization

        Args:
            org_id (int): Specify the organization id

        Required Permissions:
            Action: orgs:delete
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_organization_users(self, org_id: int) -> list:
        """The method includes a functionality to get all organization users specified by the organization id

        Args:
            org_id (int): Specify the organization id

        Required Permissions:
            Action: org.users:read
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all organization users as list
        """
        pass

    def add_organization_user(self, org_id: int, login_or_email: str, role: str) -> int:
        """The method includes a functionality to add a user to an organization

        Args:
            org_id (int): Specify the organization id
            login_or_email (str): Specify the added user
            role (str): Specify the added role for the user

        Required Permissions:
            Action: org.users:add
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            user_id (int): Returns the added user id
        """
        pass

    def update_organization_user(self, org_id: int, user_id: int, role: str):
        """The method includes a functionality to update organization user specified by the organization id, the user_id and the role

        Args:
            org_id (int): Specify the organization id
            user_id (int): Specify the user id
            role (str): Specify the added role for the user

        Required Permissions:
            Action: org.users.role:update
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_organization_user(self, org_id: int, user_id: int):
        """The method includes a functionality to remove an organization users specified by the organization id and the user id

        Args:
            org_id (int): Specify the organization id
            user_id (int): Specify the user id

        Required Permissions:
            Action: org.users:remove
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
