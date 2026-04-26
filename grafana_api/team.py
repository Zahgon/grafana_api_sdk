import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    TeamObject,
)
from .api import Api


class Team:
    """The class includes all necessary methods to access the Grafana team API endpoints. Be aware that all functionalities inside the class only working with the corresponding access rights, please check the following page for details: https://grafana.com/docs/grafana/latest/http_api/team/#team-api & https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/#team-sync-api

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_team(
        self, results_per_page: int = 1000, pages: int = 1, query: str = None
    ) -> dict:
        """The method includes a functionality to get the organization teams specified by the optional pagination functionality

        Required Permissions:
            Action: teams:read
            Scope: teams:*

        Args:
            results_per_page (int): Specify the results_per_page as integer (default 1000)
            pages (int): Specify the pages as integer (default 1)
            query (str): Specify the query (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization teams
        """
        pass

    def get_team_by_id(self, id: int) -> dict:
        """The method includes a functionality to get the organization team specified by the id

        Required Permissions:
            Action: teams:read
            Scope: teams:*

        Args:
            id (int): Specify the id of the team

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization team
        """
        pass

    def add_team(self, team: TeamObject) -> int:
        """The method includes a functionality to add an organization team specified by the TeamObject

        Required Permissions:
            Action: teams:create
            Scope: N/A

        Args:
            team (TeamObject): Specify the team

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
             team_id (int): Returns the team id
        """
        pass

    def update_team(self, id: int, name: str, email: str):
        """The method includes a functionality to update an organization team specified by the team_id, name and email

        Required Permissions:
            Action: teams:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            name (str): Specify the team name
            email (str): Specify the team email

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_team_by_id(self, id: int):
        """The method includes a functionality to delete an organization team specified by the team_id

        Required Permissions:
            Action: teams:delete
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_team_members(self, id: int) -> list:
        """The method includes a functionality to get all organization team users specified by the team_id

        Required Permissions:
            Action: teams.permissions:read
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the organization team members
        """
        pass

    def add_team_member(self, id: int, user_id: int):
        """The method includes a functionality to add an organization team user specified by the team_id and the user_id

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            user_id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_team_member(self, id: int, user_id: int):
        """The method includes a functionality to delete an organization team user specified by the team_id and the user_id

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            user_id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_team_preferences(self, id: int) -> dict:
        """The method includes a functionality to get the organization team preferences specified by the team_id

        Required Permissions:
            Action: teams:read
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization team preferences
        """
        pass

    def update_team_preferences(
        self,
        id: int,
        theme: str = None,
        timezone: str = None,
        home_dashboard_id: int = 0,
        home_dashboard_uid: str = None,
    ):
        """The method includes a functionality to update the organization team preferences specified by the team_id, theme, timezone and home_dashboard_id or home_dashboard_uid

        Required Permissions:
            Action: teams:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            theme (str): Specify the team theme e.g. light or dark (default Grafana None)
            timezone (str): Specify the team timezone e.g. utc or browser (default Grafana None)
            home_dashboard_id (int): Specify the home team dashboard by id (default 0)
            home_dashboard_uid (str): Specify the home team dashboard by uid (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_external_groups(
        self,
        id: int,
    ) -> list:
        """The method includes a functionality to get the team groups specified by the team_id. The functionality is a Grafana ENTERPRISE feature

        Required Permissions:
            Action: teams.permissions:read
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the organization team groups
        """
        pass

    def add_external_group(
        self,
        id: int,
        team_group: str,
    ):
        """The method includes a functionality to add a group to the team specified by the team_id and the team_group. The functionality is a Grafana ENTERPRISE feature

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            team_group (str): Specify the team group

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def remove_external_group(
        self,
        id: int,
        team_group: str,
    ):
        """The method includes a functionality to remove a group from a team specified by the team_id and the team_group. The functionality is a Grafana ENTERPRISE feature

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            team_group (str): Specify the team group

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
