import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class Preferences:
    """The class includes all necessary methods to access the Grafana preferences API endpoints.

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_current_user_preferences(
        self,
    ) -> dict:
        """The method includes a functionality to get the current user preferences

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the current user preferences
        """
        pass

    def update_current_user_preferences(
        self,
        theme: str = None,
        timezone: str = None,
        home_dashboard_id: int = 0,
        home_dashboard_uid: str = None,
    ):
        """The method includes a functionality to update the current user preferences

        Args:
            theme (str): Specify the theme e.g. light, dark, or an empty string for the default theme (default None)
            home_dashboard_id (int): Specify the dashboard id of the home folder (default 0)
            home_dashboard_uid (str): Specify the home team dashboard by uid (default None)
            timezone (str): Specify the timezone e.g. utc, browser, or an empty string for the default (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_current_org_preferences(
        self,
    ) -> dict:
        """The method includes a functionality to get the current org preferences

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the current user preferences
        """
        pass

    def update_current_org_preferences(
        self,
        theme: str = None,
        home_dashboard_id: int = 0,
        home_dashboard_uid: str = None,
        timezone: str = None,
    ):
        """The method includes a functionality to update the current org preferences

        Args:
            theme (str): Specify the theme e.g. light, dark, or an empty string for the default theme (default None)
            home_dashboard_id (int): Specify the dashboard id of the home folder (default 0)
            home_dashboard_uid (str): Specify the home team dashboard by uid (default None)
            timezone (str): Specify the timezone e.g. utc, browser, or an empty string for the default (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
