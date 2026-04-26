import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods, CustomRole
from .api import Api


class RBAC:
    """The class includes all necessary methods to access the Grafana RBAC API endpoints. Be aware that the functionality is a Grafana ENTERPRISE feature

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_status(self) -> bool:
        """The method includes a functionality to get the status if role-based access control is enabled or not

        Required Permissions:
            Action: status:accesscontrol
            Scope: services:accesscontrol

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (bool): Return a flag indicating if the role-based access control is enabled or not
        """
        pass

    def get_all_roles(self, include_hidden_roles: bool = False) -> list:
        """The method includes a functionality gets all existing roles. The response contains all global and organization local roles, for the organization which user is signed in

        Args:
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: roles:read
            Scope: roles:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return all global and organization local roles
        """
        pass

    def get_role(self, uid: str) -> dict:
        """The method includes a functionality get a role specified by the uid

        Args:
            uid (str): Specify the uid of the role

        Required Permissions:
            Action: roles:read
            Scope: roles:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Return the corresponding role
        """
        pass

    def create_role(self, role_definition: CustomRole) -> dict:
        """The method includes a functionality create a new custom role and maps given permissions to that role. Note that roles with the same prefix as Fixed roles canâ€™t be created

        Args:
            role_definition (CustomRole): Specify the corresponding role definition

        Required Permissions:
            Action: roles:write
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Return the newly created role
        """
        pass

    def update_role(self, uid: str, role_definition: CustomRole) -> dict:
        """The method includes a functionality to update the role with the given uid, and its permissions. The operation is idempotent and all permissions of the role will be replaced based on the request content. You need to increment the version of the role with each update, otherwise the request will fail

        Args:
            uid (str): Specify the corresponding uid of the custom role
            role_definition (CustomRole): Specify the corresponding role definition

        Required Permissions:
            Action: roles:write
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Return the updated role
        """
        pass

    def delete_role(self, uid: str, force: bool = False, global_role: bool = False):
        """The method includes a functionality to delete a role with the given uid

        Args:
            uid (str): Specify the corresponding uid of the custom role
            force (bool): Specify the corresponding if the role will be deleted with all itâ€™s assignments or not (default False)
            global_role (bool): Specify the corresponding if the role is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: roles:delete
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_user_assigned_roles(
        self, user_id: int, include_hidden_roles: bool = False
    ) -> list:
        """The method includes a functionality to get the roles that have been directly assigned to a given user specified by the user id. The list does not include basic roles (Viewer, Editor, Admin or Grafana Admin), and it does not include roles that have been inherited from a team

        Args:
            user_id (int): Specify the corresponding user_id of the user
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: users.roles:read
            Scope: users:id:<user ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding user roles
        """
        pass

    def get_user_assigned_permissions(self, user_id: int) -> list:
        """The method includes a functionality to get the permissions that have been directly assigned to a given user specified by the user id

        Args:
            user_id (int): Specify the corresponding user_id of the user

        Required Permissions:
            Action: users.permissions:read
            Scope: users:id:<user ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding user permissions
        """
        pass

    def add_user_role_assignment(
        self, user_id: int, role_uid: str, global_assignment: bool = False
    ):
        """The method includes a functionality to assign a role to a specific user

        Args:
            user_id (int): Specify the corresponding user_id of the user
            role_uid (str): Specify the corresponding uid of the role
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def remove_user_role_assignment(self, user_id: int, role_uid: str):
        """The method includes a functionality to revoke a role to a specific user

        Args:
            user_id (int): Specify the corresponding user_id of the user
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_user_role_assignments(
        self,
        user_id: int,
        role_uids: list,
        include_hidden_roles: bool = False,
        global_assignment: bool = False,
    ):
        """The method includes a functionality to update the user role assignments to match the provided set of uid's. This will remove any assigned roles that arenâ€™t in the request and add roles that are in the set but are not already assigned to the user

        Args:
            user_id (int): Specify the corresponding user_id of the user
            role_uids (list): Specify the corresponding uids of the role
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add, users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_service_account_assigned_roles(
        self, service_account_id: int, include_hidden_roles: bool = False
    ) -> list:
        """The method includes a functionality to get the roles that have been directly assigned to a given service account. The list does not include basic roles (Viewer, Editor, Admin or Grafana Admin)

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: users.roles:read
            Scope: users:id:<service account ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding service account roles
        """
        pass

    def get_service_account_assigned_permissions(self, service_account_id: int) -> list:
        """The method includes a functionality to get the permissions that a given service account has

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account

        Required Permissions:
            Action: users.permissions:read
            Scope: users:id:<service account ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding service account permissions
        """
        pass

    def add_service_account_role_assignment(
        self, service_account_id: int, role_uid: str, global_assignment: bool = False
    ):
        """The method includes a functionality to assign a role to a specific service account

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            role_uid (str): Specify the corresponding uid of the role
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def remove_service_account_role_assignment(
        self, service_account_id: int, role_uid: str
    ):
        """The method includes a functionality to revoke a role to a specific service account

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_service_account_role_assignments(
        self,
        service_account_id: int,
        role_uids: list,
        include_hidden_roles: bool = False,
        global_assignment: bool = False,
    ):
        """The method includes a functionality to update the service account role assignments to match the provided set of uid's. This will remove any assigned roles that arenâ€™t in the request and add roles that are in the set but are not already assigned to the user

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            role_uids (list): Specify the corresponding uids of the role
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add, users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_team_assigned_roles(
        self, team_id: int, include_hidden_roles: bool = False
    ) -> list:
        """The method includes a functionality to get that have been directly assigned to a given team.

        Args:
            team_id (int): Specify the corresponding team_id of the team
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: teams.roles:read
            Scope: teams:id:<team ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding team roles
        """
        pass

    def add_team_role_assignment(self, team_id: int, role_uid: str):
        """The method includes a functionality to assign a role to a specific team

        Args:
            team_id (int): Specify the corresponding team_id of the team
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: teams.roles:add
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def remove_team_role_assignment(self, team_id: int, role_uid: str):
        """The method includes a functionality to revoke a role to a specific team

        Args:
            team_id (int): Specify the corresponding team_id of the team
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: teams.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_team_role_assignments(
        self,
        team_id: int,
        role_uids: list,
        include_hidden_roles: bool = False,
    ):
        """The method includes a functionality to update the service account role assignments to match the provided set of uid's. This will remove any assigned roles that arenâ€™t in the request and add roles that are in the set but are not already assigned to the user

        Args:
            team_id (int): Specify the corresponding team_id of the team
            role_uids (list): Specify the corresponding uids of the role
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: teams.roles:add, teams.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def reset_basic_roles_to_their_default(self):
        """The method includes a functionality to reset basic roles permissions to their default

        Required Permissions:
            Action: roles:write
            Scope: permissions:type:escalate

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
