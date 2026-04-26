import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    AnnotationObject,
    AnnotationGraphiteObject,
    FindAnnotationObject,
)
from .api import Api


class Annotations:
    """The class includes all necessary methods to access the Grafana annotations API endpoints. Annotations can be organization annotations that can be shown on any dashboard by configuring an annotation data source filtered by tags. They can also be tied to a panel on a dashboard and are then only shown on that panel

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def find_annotations(self, annotation: FindAnnotationObject = None) -> list:
        """The method includes a functionality to find the corresponding annotations

        Args:
            annotation (FindAnnotationObject): Specify the find annotation object

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the result of the find annotations call
        """
        pass

    def create_annotation(
        self,
        annotation: AnnotationObject,
    ) -> int:
        """The method includes a functionality to create the corresponding annotation

        Args:
            annotation (AnnotationObject): Specify the annotation object

        Required Permissions:
            Action: annotations:create
            Scope: annotations:type:

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the annotation id
        """
        pass

    def create_graphite_annotation(self, annotation: AnnotationGraphiteObject) -> int:
        """The method includes a functionality to create the corresponding graphite annotation

        Args:
            annotation (AnnotationGraphiteObject): Specify the annotation object

        Required Permissions:
            Action: annotations:create
            Scope: annotations:type:organization

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the annotation id
        """
        pass

    def update_annotation(self, id: int, annotation: AnnotationObject):
        """The method includes a functionality to update the corresponding annotation specified by the annotation id

        Args:
            id (int): Specify the annotation object id
            annotation (AnnotationObject): Specify the annotation object

        Required Permissions:
            Action: annotations:write
            Scope: annotations:type:

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_annotation(
        self,
        id: int,
    ):
        """The method includes a functionality to delete the corresponding annotation specified by the annotation id

        Args:
            id (int): Specify the annotation object id

        Required Permissions:
            Action: annotations:write
            Scope: annotations:type:

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def find_annotation_tags(
        self,
        tag: str = None,
        limit: int = 100,
    ):
        """The method includes a functionality to find the annotation tags

        Args:
            tag (str): Specify the optional annotation tag
            limit (int): Specify the optional annotation limit (default 100)

        Required Permissions:
            Action: annotations:read
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the find annotation tags call
        """
        pass
