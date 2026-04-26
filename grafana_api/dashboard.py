import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods, PublicDashboard
from .folder import Folder
from .api import Api


class Dashboard:
    """The class includes all necessary methods to access the Grafana dashboard API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def create_or_update_dashboard(
        self,
        dashboard_path: str,
        dashboard_json: dict,
        message: str,
        overwrite: bool = False,
    ):
        """The method includes a functionality to create the specified dashboard

        Args:
            dashboard_path (str): Specify the dashboard path in which the dashboard is to be placed
            dashboard_json (dict): Specify the inserted dashboard as dict
            message (str): Specify the message that should be injected as commit message inside the dashboard
            overwrite (bool): Should the already existing dashboard be overwritten (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_dashboard_by_name_and_path(
        self, dashboard_name: str, dashboard_path: str
    ):
        """The method includes a functionality to delete the specified dashboard inside the model

        Args:
            dashboard_name (str): Specify the dashboard name of the deleted dashboard
            dashboard_path (str): Specify the dashboard path in which the dashboard is to be placed

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_dashboard_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get the dashboard from the specified uid

        Args:
            uid (str): Specify the uid of the dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dashboard
        """
        pass

    def get_dashboard_home(self) -> dict:
        """The method includes a functionality to get the home dashboard

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the home dashboard
        """
        pass

    def get_dashboard_tags(self) -> list:
        """The method includes a functionality to get the all tags of all dashboards

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all dashboard tags
        """
        pass

    def get_dashboard_uid_and_id_by_name_and_folder(
        self, dashboard_name: str, dashboard_path: str
    ) -> dict:
        """The method includes a functionality to extract the dashboard uid specified inside the model

        Args:
            dashboard_name (str): Specify the dashboard name of the dashboard
            dashboard_path (str): Specify the dashboard path of the dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dashboard uid and the id
        """
        pass

    def get_dashboard_permissions(self, id: int) -> list:
        """The method includes a functionality to extract the dashboard permissions based on the specified id

        Args:
            id (int): Specify the id of the dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the dashboard permissions of a dashboard as list
        """
        pass

    def get_dashboard_permissions_by_uid(self, uid: str) -> list:
        """The method includes a functionality to extract the dashboard permissions based on the specified uid

        Args:
            uid (str): Specify the uid of the dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the dashboard permissions of a dashboard as list
        """
        pass

    def update_dashboard_permissions(self, id: int, permission_json: dict):
        """The method includes a functionality to update the dashboard permissions based on the specified id and the permission json document

        Args:
            id (int): Specify the id of the dashboard
            permission_json (dict): Specify the inserted permissions as dict

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_dashboard_permissions_by_uid(self, uid: str, permission_json: dict):
        """The method includes a functionality to update the dashboard permissions based on the specified uid and the permission json document

        Args:
            uid (str): Specify the uid of the dashboard
            permission_json (dict): Specify the inserted permissions as dict

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_dashboard_versions(self, id: int) -> list:
        """The method includes a functionality to extract the versions of a dashboard based on the specified id

        Args:
            id (int): Specify the id of the dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all dashboard versions of a dashboard as list
        """
        pass

    def get_dashboard_versions_by_uid(self, uid: str) -> list:
        """The method includes a functionality to extract the versions of a dashboard based on the specified uid

        Args:
            uid (str): Specify the id of the dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all dashboard versions of a dashboard as list
        """
        pass

    def get_dashboard_version(self, id: int, version_id: int) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified dashboard id and a version_id of the dashboard

        Args:
            id (int): Specify the id of the dashboard
            version_id (int): Specify the version_id of a dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a dashboard version of a dashboard as dict
        """
        pass

    def get_dashboard_version_by_uid(self, uid: str, version_id: int) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified dashboard uid and a version_id of the dashboard

        Args:
            uid (str): Specify the uid of the dashboard
            version_id (int): Specify the version_id of a dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a dashboard version of a dashboard as dict
        """
        pass

    def restore_dashboard_version(self, id: int, version: dict):
        """The method includes a functionality to restore a specified version of a dashboard based on the specified dashboard id and a version as dict of the dashboard

        Args:
            id (int): Specify the id of the dashboard
            version (dict): Specify the version_id of a dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def restore_dashboard_version_by_uid(self, uid: str, version: dict):
        """The method includes a functionality to restore a specified version of a dashboard based on the specified dashboard uid and a version as dict of the dashboard

        Args:
            uid (str): Specify the uid of the dashboard
            version (dict): Specify the version_id of a dashboard

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def calculate_dashboard_diff(
        self,
        dashboard_id_and_version_base: dict,
        dashboard_id_and_version_new: dict,
        diff_type: str = "json",
    ) -> str:
        """The method includes a functionality to calculate the diff of specified versions of a dashboard based on the specified dashboard uid and the selected version of the base dashboard and the new dashboard and the diff type (basic or json)

        Args:
            dashboard_id_and_version_base (dict): Specify the version and id of the base dashboard
            dashboard_id_and_version_new (dict): Specify the version and id of the new dashboard
            diff_type (str): Specify the diff type (basic or json) (default json)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the difference of the two specified dashboards
        """
        pass

    def get_public_dashboards(self, per_page: int = None, page: int = None) -> dict:
        """The method includes a functionality to get all public available dashboards

        Required Permissions:
            Action: dashboards:read
            Scope: dashboards:uid:<dashboard UID>

        Args:
            per_page (int): Specify the value per page size
            page (int): Specify the page

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns all public available dashboards
        """
        pass

    def get_public_dashboard_by_uid(
        self,
        dashboard_uid: str,
    ) -> dict:
        """The method includes a functionality to get a public available dashboard specified by dashboard_uid

        Required Permissions:
            Action: dashboards:read
            Scope: dashboards:uid:<dashboard UID>

        Args:
            dashboard_uid (str): Specify the dashboard_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding public available dashboard
        """
        pass

    def create_public_dashboard(
        self, dashboard_uid: str, public_dashboard: PublicDashboard = PublicDashboard()
    ) -> dict:
        """The method includes a functionality to create a public available dashboard

        Required Permissions:
            Action: dashboards.public:write
            Scope: dashboards:uid:<dashboard UID>

        Args:
            dashboard_uid (str): Specify the dashboard_uid
            public_dashboard (PublicDashboard): Specify the optional public dashboard object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding public available dashboard
        """
        pass

    def update_public_dashboard(
        self,
        dashboard_uid: str,
        public_dashboard_uid: str,
        time_selection_enabled: bool = None,
        is_enabled: bool = None,
        annotations_enabled: bool = None,
        share: str = None,
    ) -> dict:
        """The method includes a functionality to update a public available dashboard

        Required Permissions:
            Action: dashboards.public:write
            Scope: dashboards:uid:<dashboard UID>

        Args:
            dashboard_uid (str): Specify the dashboard_uid
            public_dashboard_uid (str): Specify the public_dashboard_uid
            time_selection_enabled (bool): Specify the optional enablement of the time picker inside the public dashboard (default None)
            is_enabled (bool): Specify the optional enablement of the public dashboard (default None)
            annotations_enabled (bool): Specify the optional enablement of the annotations inside the public dashboard (default None)
            share (str): Specify the optional share mode of the public dashboard (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding public available dashboard
        """
        pass

    def delete_public_dashboard(
        self,
        dashboard_uid: str,
        public_dashboard_uid: str,
    ):
        """The method includes a functionality to delete a public available dashboard

        Required Permissions:
            Action: dashboards.public:write
            Scope: dashboards:uid:<dashboard UID>

        Args:
            dashboard_uid (str): Specify the dashboard_uid
            public_dashboard_uid (str): Specify the public_dashboard_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
