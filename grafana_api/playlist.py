import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    PlaylistObject,
)
from .api import Api


class Playlist:
    """The class includes all necessary methods to access the Grafana playlist API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_playlist(self, query: str = None, limit: int = None) -> list:
        """The method includes a functionality to get the organization playlist's specified by the optional pagination functionality

         Args:
            query (str): Specify the query to limit response to playlist having a name like this value(default None)
            limit (int): Specify the limit as integer of the response (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the organization playlist's
        """
        pass

    def get_playlist(self, playlist_uid: str) -> dict:
        """The method includes a functionality to get the playlist specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """
        pass

    def get_playlist_items(self, playlist_uid: str) -> list:
        """The method includes a functionality to get the playlist items specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist items
        """
        pass

    def get_playlist_dashboards(self, playlist_uid: str) -> list:
        """The method includes a functionality to get the playlist dashboards specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist dashboards
        """
        pass

    def create_playlist(self, playlist: PlaylistObject) -> dict:
        """The method includes a functionality to create a playlist specified by the playlist object

         Args:
            playlist (PlaylistObject): Specify the playlist object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """
        pass

    def update_playlist(self, playlist_uid: str, playlist: PlaylistObject) -> dict:
        """The method includes a functionality to update a playlist specified by the playlist object and playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid
            playlist (PlaylistObject): Specify the playlist object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """
        pass

    def delete_playlist(self, playlist_uid: str):
        """The method includes a functionality to delete a playlist specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
