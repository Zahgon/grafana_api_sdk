import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
)
from .api import Api


class QueryHistory:
    """The class includes all necessary methods to access the Grafana query history API endpoints. Be aware that it requires that the user is logged in and that query history feature is enabled in the config file

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def add_query_to_history(self, datasource_uid: str, queries: list) -> dict:
        """The method includes a functionality to add queries to query history

        Args:
            datasource_uid (str): Specify the datasource uid
            queries (list): Specify the queries as list from type QueryObject

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the added result of the query history
        """
        pass

    def search_query_history(
        self,
        datasource_uids: list,
        search_string: str,
        sort: str = "time-desc",
        only_starred: bool = False,
        pages: int = 1,
        results_per_page: int = 100,
    ) -> dict:
        """The method includes a functionality to search a query inside the query history

        Args:
            datasource_uids (list): Specify the datasource uid
            search_string (str): Specify the search string to filter the result
            sort (str): Specify the sorting order e.g. time-asc or time-desc (default time-desc)
            only_starred (bool): Specify if queries that are starred should be used for the search (default false)
            pages (int): Specify the pages as integer (default 1)
            results_per_page (int): Specify the results_per_page as integer (default 100)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding result of the query history
        """
        pass

    def delete_query_history(self, uid: str):
        """The method includes a functionality to delete a query inside the query history

        Args:
            uid (str): Specify the uid of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
             None
        """
        pass

    def update_query_history(self, uid: str, comment: str) -> dict:
        """The method includes a functionality to update a query inside the query history

        Args:
            uid (str): Specify the uid of the query
            comment (str): Specify the comment of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the modified result of the query history
        """
        pass

    def star_query_history(self, uid: str) -> dict:
        """The method includes a functionality to star a query inside the query history

        Args:
            uid (str): Specify the uid of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding stared query history
        """
        pass

    def unstar_query_history(self, uid: str) -> dict:
        """The method includes a functionality to unstar a query inside the query history

        Args:
            uid (str): Specify the uid of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding unstared query history
        """
        pass
