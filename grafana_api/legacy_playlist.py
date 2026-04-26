import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    PlaylistObject,
)
from .api import Api


class LegacyPlaylist:
    """The class includes all necessary methods to access the Grafana legacy playlist API endpoints.  Be aware that the functionality is a Grafana <= v9 feature

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_playlist(self, playlist_id: int) -> dict:
        """The method includes a functionality to get the playlist specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """
        pass

    def get_playlist_items(self, playlist_id: int) -> list:
        """The method includes a functionality to get the playlist items specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist items
        """
        pass

    def get_playlist_dashboards(self, playlist_id: int) -> list:
        """The method includes a functionality to get the playlist dashboards specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist dashboards
        """
        pass

    def update_playlist(self, playlist_id: int, playlist: PlaylistObject) -> dict:
        """The method includes a functionality to update a playlist specified by the playlist object and playlist_id

         Args:
            playlist_id (int): Specify the playlist_id
            playlist (PlaylistObject): Specify the playlist object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """
        pass

    def delete_playlist(self, playlist_id: int):
        """The method includes a functionality to delete a playlist specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass
