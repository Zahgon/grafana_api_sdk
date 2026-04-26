import json
import logging
from typing import Union

from .model import APIModel, APIEndpoints, RequestsMethods, CorrelationObject
from .api import Api


class Correlations:
    """The class includes all necessary methods to access the Grafana correlations API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_correlation(self, datasource_uid: str, correlation_uid: str) -> dict:
        """The method includes a functionality to get a specific correlation from a data source - the data source identified by source uid and the correlation uid

         Args:
            datasource_uid (str): Specify the correlation data source uid
            correlation_uid (str): Specify the correlation uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding correlation
        """
        pass

    def get_all_correlations_by_datasource_uid(self, datasource_uid: str) -> list:
        """The method includes a functionality to get all correlations from a data source - the data source identified by source uid

         Args:
            datasource_uid (str): Specify the correlation data source uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the corresponding correlations
        """
        pass

    def get_all_correlations(self) -> Union[list, dict]:
        """The method includes a functionality to get all correlations

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (Union[list, dict]): Returns the corresponding correlations
        """
        pass

    def create_correlations(self, correlation_object: CorrelationObject) -> dict:
        """The method includes a functionality to create a correlation between two data sources - the source data source identified by source uid in the path, and the target data source which is specified in the body

         Args:
            correlation_object (CorrelationObject): Specify the correlation object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the newly created correlation
        """
        pass

    def delete_correlations(self, source_datasource_uid: str, correlation_uid: str):
        """The method includes a functionality to deletes a correlation

         Args:
            source_datasource_uid (str): Specify the source data source uid
            correlation_uid (str): Specify the correlation uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_correlations(
        self,
        source_datasource_uid: str,
        correlation_uid: str,
        label: str,
        description: str,
    ) -> dict:
        """The method includes a functionality to update a correlation

         Args:
            source_datasource_uid (str): Specify the source data source uid
            correlation_uid (str): Specify the correlation uid
            label (str): Specify a label for the correlation
            description (str): Specify a description for the correlation

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated correlation
        """
        pass
