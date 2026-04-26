import logging
import json

import httpx

from .api import Api
from .model import APIModel, APIEndpoints, RequestsMethods


class Folder:
    """The class includes all necessary methods to access the Grafana folder API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_folders(self) -> list:
        """The method includes a functionality to extract all folders inside the organization

        Required Permissions:
            Action: folders:read
            Scope: folders:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all folders
        """
        pass

    def get_folder_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to extract all folder information specified by the uid of the folder

        Args:
            uid (str): Specify the uid of the folder

        Required Permissions:
            Action: folders:read
            Scope: folders:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a folder
        """
        pass

    def get_folder_by_id(self, id: int) -> dict:
        """The method includes a functionality to extract all folder information specified by the id of the folder

        Args:
            id (int): Specify the id of the folder

        Required Permissions:
            Action: folders:read
            Scope: folders:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a folder
        """
        pass

    def create_folder(
        self, title: str, uid: str = None, parent_uid: str = None
    ) -> dict:
        """The method includes a functionality to create a new folder inside the organization specified by the defined title and the optional uid

        Args:
            title (str): Specify the title of the folder
            uid (str): Specify the uid of the folder (default None)
            parent_uid (str): Specify the parent_uid of the folder (default None)

        Required Permissions:
            Action: folders:create, folders:write
            Scope: folders:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a newly created folder
        """
        pass

    def update_folder(
        self, title: str, uid: str, version: int = 0, overwrite: bool = False
    ) -> dict:
        """The method includes a functionality to update a folder information inside the organization specified by the uid, the title, the version of the folder or if folder information be overwritten

        Args:
            title (str): Specify the title of the folder
            uid (str): Specify the uid of the folder
            version (int): Specify the version of the folder (default 0)
            overwrite (bool): Should the already existing folder information be overwritten (default False)

        Required Permissions:
            Action: folders:write
            Scope: folders:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns an updated folder
        """
        pass

    def move_folder(self, uid: str, parent_uid: str = None):
        """The method includes a functionality to move a folder inside the organization specified by the defined uid. This feature is only relevant if nested folders are enabled

        Args:
            uid (str): Specify the uid of the folder
            parent_uid (str): Specify the parent_uid of the folder. If the value is None, then the folder is moved under the root (default None)

        Required Permissions:
            Action: folders:create, folders:write
            Scope: folders:*, folders:uid:<destination folder UID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the moved folder
        """
        pass

    def delete_folder(self, uid: str):
        """The method includes a functionality to delete a folder inside the organization specified by the defined uid

        Args:
            uid (str): Specify the uid of the folder

        Required Permissions:
            Action: folders:delete
            Scope: folders:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_folder_permissions(self, uid: str) -> list:
        """The method includes a functionality to extract the folder permissions inside the organization specified by the defined uid

        Args:
            uid (str): Specify the uid of the folder

        Required Permissions:
            Action: folders.permissions:read
            Scope: folders:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of folder permissions
        """
        pass

    def update_folder_permissions(self, uid: str, permission_json: dict):
        """The method includes a functionality to update the folder permissions based on the specified uid and the permission json document

        Args:
            uid (str): Specify the uid of the folder
            permission_json (dict): Specify the inserted permissions as dict

        Required Permissions:
            Action: folders.permissions:write
            Scope: folders:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_folder_id_by_dashboard_path(self, dashboard_path: str) -> int:
        """The method includes a functionality to extract the folder id specified inside model dashboard path

        Args:
            dashboard_path (str): Specify the dashboard path

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            folder_id (int): Returns the folder id
        """
        pass

    def get_all_folder_ids_and_names(self) -> list:
        """The method extract all folder id and names inside the complete organisation

        Returns:
            folders (list): Returns a list of dicts with folder ids and the corresponding names
        """
        pass
