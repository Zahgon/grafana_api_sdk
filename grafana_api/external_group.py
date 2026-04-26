import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class ExternalGroup:
    """The class includes all necessary methods to access the Grafana external group API endpoints.

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_external_groups(
        self,
        team_id: int,
    ) -> list:
        """The method includes a functionality to get the corresponding external groups specified by the team id

        Args:
            team_id (int): Specify the team id

        Required Permissions:
            Action: teams.permissions:read
            Scope: teams:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the external groups
        """
        pass

    def add_external_group(
        self,
        team_id: int,
        group_id: str,
    ):
        """The method includes a functionality to add the corresponding external groups specified by the team id and group id

        Args:
            team_id (int): Specify the team id
            group_id (str): Specify the group id (e.g. cn=editors,ou=groups,dc=grafana,dc=org)

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the external groups
        """
        pass

    def remove_external_group(
        self,
        team_id: int,
        group_id: str,
    ):
        """The method includes a functionality to remove the corresponding external groups specified by the team id and group id

        Args:
            team_id (int): Specify the team id
            group_id (str): Specify the group id (e.g. cn=editors,ou=groups,dc=grafana,dc=org)

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the external groups
        """
        pass
