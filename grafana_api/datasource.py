import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    DatasourceCache,
    DatasourcePermission,
)
from .api import Api


class Datasource:
    """The class includes all necessary methods to access the Grafana datasource API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_datasources(self) -> list:
        """The method includes a functionality to get all datasources

        Required Permissions:
            Action: datasources:read
            Scope: datasources:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of all datasources
        """
        pass

    def get_datasource_by_id(self, datasource_id: int) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource id

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass

    def get_datasource_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<uid>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass

    def get_datasource_by_name(self, name: str) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource name

        Args:
            name (str): Specify the name of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:name:*, datasources:name:<name>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass

    def get_datasource_id_by_name(self, name: str) -> int:
        """The method includes a functionality to get the datasource id specified by the datasource name

        Args:
            name (str): Specify the name of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:name:*, datasources:name:<name>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns a datasource id
        """
        pass

    def create_datasource(self, data_source: dict):
        """The method includes a functionality to create a datasource specified by the datasource as dict

        Args:
            data_source (dict): Specify the datasource as dict

        Required Permissions:
            Action: datasources:create

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_datasource(self, datasource_id: int, data_source: dict):
        """The method includes a functionality to update a datasource specified by the datasource as dict and the datasource id

        Args:
            datasource_id (int): Specify the id of the datasource
            data_source (dict): Specify the datasource as dict

        Required Permissions:
            Action: datasources:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_datasource_by_id(self, datasource_id: int):
        """The method includes a functionality to delete a datasource specified by the datasource id

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources:delete
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_datasource_by_uid(self, uid: str):
        """The method includes a functionality to delete a datasource specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:delete
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<uid>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_datasource_by_name(self, name: str):
        """The method includes a functionality to delete a datasource specified by the datasource name

        Args:
            name (str): Specify the name of the datasource

        Required Permissions:
            Action: datasources:delete
            Scope: [datasources:*, datasources:name:*, datasources:name:<name>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def query_datasource_by_id(
        self, time: str, to: str, datasource_queries: list
    ) -> dict:
        """The method includes a functionality to execute a queries inside the datasource itself specified by the datasource id

        Args:
            from (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            to (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            datasource_queries (list): Specify a list of execution queries based on the DatasourceQuery class

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the specified query
        """
        pass


class DatasourcePermissions:
    """The class includes all necessary methods to access the Grafana datasource permissions API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_datasource_permissions_by_uid(self, uid: str) -> list:
        """The method includes a functionality to get the datasource permissions specified by the datasource uid. The functionality is a Grafana ENTERPRISE feature

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.permissions:read
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the datasource permissions
        """
        pass

    def update_datasource_user_access_by_uid(
        self, uid: str, id: int, datasource_user_permission: DatasourcePermission
    ):
        """The method includes a functionality to update the datasource permission specified by the datasource uid and the user id. The functionality is a Grafana ENTERPRISE feature

        Args:
            uid (str): Specify the uid of the datasource
            id (int): Specify the id of the user
            datasource_user_permission (DatasourcePermission): Specify the datasource user permission

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_datasource_team_access_by_uid(
        self, uid: str, id: int, datasource_team_permission: DatasourcePermission
    ):
        """The method includes a functionality to update the datasource permission specified by the datasource uid and the team id. The functionality is a Grafana ENTERPRISE feature

        Args:
            uid (str): Specify the uid of the datasource
            id (int): Specify the id of the team
            datasource_team_permission (DatasourcePermission): Specify the datasource team permission

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_datasource_basic_role_access_by_uid(
        self,
        uid: str,
        build_in_role_name: str,
        datasource_team_permission: DatasourcePermission,
    ):
        """The method includes a functionality to update the datasource permission specified by the datasource uid and the build in role name. The functionality is a Grafana ENTERPRISE feature

        Args:
            uid (str): Specify the uid of the datasource
            build_in_role_name (str): Specify the build in role name
            datasource_team_permission (DatasourcePermission): Specify the datasource team permission

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass


class DatasourceLegacyPermissions:
    """The class includes all necessary methods to access the Grafana legacy datasource permissions API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def enable_datasource_permissions(self, datasource_id: int):
        """The method includes a functionality to enable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def disable_datasource_permissions(self, datasource_id: int):
        """The method includes a functionality to disable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_datasource_permissions(self, datasource_id: int) -> dict:
        """The method includes a functionality to get the datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources.permissions:read
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the datasource permissions
        """
        pass

    def add_datasource_permissions(
        self, datasource_id: int, datasource_permission: dict
    ):
        """The method includes a functionality to add datasource permission specified by the datasource id and the datasource permission dict. The functionality is a Grafana ENTERPRISE feature

        Args:
            datasource_id (int): Specify the id of the datasource
            datasource_permission (dict): Specify the permission of the datasource

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_datasource_permissions(self, datasource_id: int, permission_id: int):
        """The method includes a functionality to delete datasource permission specified by the datasource id and the permission id. The functionality is a Grafana ENTERPRISE feature

        Args:
            datasource_id (int): Specify the id of the datasource
            permission_id (id): Specify the permission id

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass


class DatasourceQueryResourceCaching:
    """The class includes all necessary methods to access the Grafana datasource query and resource caching API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights. The functionality is a Grafana ENTERPRISE feature

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to get the datasource cache config specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass

    def enable_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to enable the datasource cache specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:read
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass

    def disable_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to disable the datasource cache specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass

    def clean_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to clean the datasource cache of all data sources with caching enabled. The uid of the datasource will only be used to return the configuration for that data source

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass

    def update_datasource_cache(
        self, uid: str, datasource_cache: DatasourceCache
    ) -> dict:
        """The method includes a functionality to update the datasource cache specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource
            datasource_cache (DatasourceCache): Specif the datasource cache object

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass


class DatasourceLabelBasedAccessControl:
    """The class includes all necessary methods to access the Grafana datasource label based access control for teams API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights. The functionality is a Grafana Cloud feature. Only cloud Loki data sources are supported

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_lbac_rules_for_datasource(self, uid: str) -> list:
        """The method includes a functionality to get all datasource label based access control rules for team specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all LBAC rules
        """
        pass

    def update_lbac_rules_for_datasource(self, uid: str) -> dict:
        """The method includes a functionality to enable the datasource cache specified by the datasource uid

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:write, datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource
        """
        pass
