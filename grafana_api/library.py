import json
import logging

from .model import APIModel, APIEndpoints, SortDirection, RequestsMethods
from .api import Api


class Library:
    """The class includes all necessary methods to access the Grafana library API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_library_elements(
        self,
        results_per_page: int = 100,
        pages: int = 1,
        search_string: str = None,
        kind: int = 1,
        sort_direction: SortDirection = SortDirection.DESC,
        types_filter: str = None,
        exclude_uid: str = None,
        folder_filter_ids: str = None,
    ) -> dict:
        """The method includes a functionality to get a list of all library elements the authenticated user has permission to view. Use the perPage query parameter to control the maximum number of library elements returned, The default limit is 100. You can also use the page query parameter to fetch library elements from any page other than the first one

         Args:
            results_per_page (int): Specify the results_per_page as integer (default 100)
            pages (int): Specify the pages as integer (default 1)
            search_string (str): Specify the search string (default None)
            kind (int): Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)
            sort_direction (SortDirection): Specify the sort order of elements. Use alpha-asc for ascending and alpha-desc for descending sort order (default alpha-desc)
            types_filter (str): Specify a comma separated list of types to filter the elements by (default None)
            exclude_uid (str): Specify the element uid to exclude from search results (default None)
            folder_filter_ids (str): Specify a comma separated list of folder ID(s) to filter the elements by (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the library elements
        """
        pass

    def get_library_element_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get a library element with the given uid

         Args:
            uid (str): Specify the uid of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding library element
        """
        pass

    def get_library_element_by_name(self, name: str) -> dict:
        """The method includes a functionality to get a library element with the given name

         Args:
            name (str): Specify the name of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding library element
        """
        pass

    def get_library_element_connections(self, uid: str) -> dict:
        """The method includes a functionality to get a list of connections for a library element based on the specified uid

         Args:
            uid (str): Specify the uid of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding list of connections
        """
        pass

    def create_library_element(
        self,
        folder_id: int,
        model: dict,
        kind: int = 1,
        folder_uid: str = None,
        name: str = None,
        uid: str = None,
    ) -> dict:
        """The method includes a functionality to create a library element based on the specified folder id and model

         Args:
             folder_id (int): Specify the folder where the library element is stored. It is deprecated since Grafana v9
             model (dict): Specify the JSON model for the library element
             kind (int): Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)
             folder_uid (str): Specify the uid of the folder where the library element is stored. Specify an empty string when it is general folder (default None)
             name (str): Specify the name of the library element (default None)
             uid (str): Specify the uid of the library element (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the newly created library element
        """
        pass

    def update_library_element(
        self,
        uid: str,
        folder_id: int,
        folder_uid: str,
        name: str,
        model: dict,
        version: int,
        kind: int = 1,
    ) -> dict:
        """The method includes a functionality to update a library element

         Args:
             uid (str): Specify the uid of the library element
             folder_id (int): Specify the folder where the library element is stored. It is deprecated since Grafana v9
             folder_uid (str): Specify the uid of the folder where the library element is stored. Specify an empty string when it is general folder
             name (str): Specify the name of the library element
             model (dict): Specify the JSON model for the library element
             version (int): Specify the version for the library element
             kind (int): Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated library element
        """
        pass

    def delete_library_element(self, uid: str):
        """The method includes a functionality to delete a library element specified by the uid

         Args:
             uid (str): Specify the uid of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
