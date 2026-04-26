import datetime
import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    Silence,
    AlertmanagerConfig,
)
from .api import Api


class Alerting:
    """The class includes all necessary methods to access the Grafana alerting API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alertmanager_alerts(self, datasource_uid: str = "grafana") -> list:
        """The method includes a functionality to get the Alertmanager alerts specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Alertmanager alerts
        """
        pass

    def create_or_update_alertmanager_alerts(
        self, alerts: list, datasource_uid: str = "grafana"
    ):
        """The method includes a functionality to create or update the Alertmanager alerts specified by the datasource_uid and the alerts list

        Args:
            alerts (list): Specify a list of the alert objects
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_alertmanager_group_alerts(self, datasource_uid: str = "grafana") -> list:
        """The method includes a functionality to get the Alertmanager group alerts specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Alertmanager group alerts
        """
        pass

    def delete_alertmanager_silence_by_id(
        self, silence_id: str, datasource_uid: str = "grafana"
    ):
        """The method includes a functionality to delete the Alertmanager silence specified by the silence id and the datasource_uid

        Args:
            silence_id (str): Specify the silence id of the alerts
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_alertmanager_silence_by_id(
        self, silence_id: str, datasource_uid: str = "grafana"
    ) -> dict:
        """The method includes a functionality to get the Alertmanager silence specified by the silence id and the datasource_uid

        Args:
            silence_id (str): Specify the silence id of the alerts
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of Alertmanager silence alert
        """
        pass

    def get_alertmanager_silences(self, datasource_uid: str = "grafana") -> list:
        """The method includes a functionality to get all Alertmanager silences specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Alertmanager silence alerts
        """
        pass

    def create_or_update_alertmanager_silence(
        self, silence: Silence, datasource_uid: str = "grafana"
    ) -> dict:
        """The method includes a functionality to create or update the Alertmanager silence specified by the silence object and the datasource_uid

        Args:
            silence -> Specify the silence object
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of newly created silence alert
        """
        pass

    def get_alertmanager_status(self, datasource_uid: str = "grafana") -> dict:
        """The method includes a functionality to get the Alertmanager status specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the Alertmanager status
        """
        pass

    def delete_alertmanager_config(self, datasource_uid: str = "grafana"):
        """The method includes a functionality to delete the Alertmanager config specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_alertmanager_config(self, datasource_uid: str = "grafana") -> dict:
        """The method includes a functionality to get the Alertmanager config specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the Alertmanager config
        """
        pass

    def create_or_update_alertmanager_config(
        self,
        alertmanager_config: AlertmanagerConfig,
        datasource_uid: str = "grafana",
        template_files: dict = None,
    ):
        """The method includes a functionality to create or update the Alertmanager config specified by the Alertmanager config object, datasource_uid and template_files

        Args:
            alertmanager_config (AlertmanagerConfig): Specify the Alertmanager config object
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)
            template_files(dict): Specify the optional template files (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def test_alertmanager_receivers(
        self, alert: dict, receivers: list, datasource_uid: str = "grafana"
    ):
        """The method includes a functionality to test the Alertmanager receivers specified by the alert dict, receivers object and the datasource_uid

        Args:
            alert (dict): Specify the alert dict
            receivers (list): Specify the list of AlertmanagerReceivers objects
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_prometheus_alerts(self, datasource_uid: str = "grafana") -> dict:
        """The method includes a functionality to get all prometheus alerts specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the prometheus alerts
        """
        pass

    def get_prometheus_rules(self, datasource_uid: str = "grafana") -> dict:
        """The method includes a functionality to get all prometheus rules specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the prometheus rules
        """
        pass

    def get_ruler_rules(self, datasource_uid: str = "grafana") -> dict:
        """The method includes a functionality to get all ruler rules specified by the datasource_uid

        Args:
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the ruler rules
        """
        pass

    def delete_ruler_namespace(self, namespace: str, datasource_uid: str = "grafana"):
        """The method includes a functionality to delete a ruler namespace specified by the namespace name and the datasource_uid

        Args:
            namespace (str): Specify the namespace name
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_ruler_groups_by_namespace(
        self, namespace: str, datasource_uid: str = "grafana"
    ) -> dict:
        """The method includes a functionality to get all ruler groups specified by the namespace name and the datasource_uid

        Args:
            namespace (str): Specify the namespace name
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the ruler groups
        """
        pass

    def create_or_update_ruler_group_by_namespace(
        self,
        namespace: str,
        group_name: str,
        rules: list,
        datasource_uid: str = "grafana",
        interval: int = 0,
    ):
        """The method includes a functionality to create or update a ruler group specified by the namespace name, a ruler group name, a ruler rule object list, the datasource_uid and an interval

        Args:
            namespace (str): Specify the namespace name
            group_name (str): Specify the ruler group name
            rules (list): Specify the ruler rule object list
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)
            interval (int): Specify the interval of the ruler (default 0)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_ruler_group(
        self, namespace: str, group_name: str, datasource_uid: str = "grafana"
    ):
        """The method includes a functionality to delete a ruler group specified by the namespace name, a ruler group name and the datasource_uid

        Args:
            namespace (str): Specify the namespace name
            group_name (str): Specify the ruler group name
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_ruler_group(
        self, namespace: str, group_name: str, datasource_uid: str = "grafana"
    ) -> dict:
        """The method includes a functionality to get a ruler group specified by the namespace name, a ruler group name and the datasource_uid

        Args:
            namespace (str): Specify the namespace name
            group_name (str): Specify the ruler group name
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of all ruler groups
        """
        pass

    def test_rule(self, data_queries: list) -> dict:
        """The method includes a functionality to test a rule specified by a list of datasource rule query objects

        Args:
            data_queries (list): Specify a list of datasource rule query objects

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the result of the specified query
        """
        pass

    def test_datasource_uid_rule(
        self,
        expr: str,
        condition: str,
        data_queries: list,
        datasource_uid: str = "grafana",
    ) -> dict:
        """The method includes a functionality to test a datasource uid rule specified by the expr, the condition, a list of data queries and the datasource_uid

        Args:
            expr (str): Specify a list of datasource rule query objects
            condition (str): Specify the condition
            data_queries (list): Specify a list of datasource rule query objects
            datasource_uid (str): Specify the datasource uid or recipient of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the specified datasource_uid rule
        """
        pass

    def test_backtest_rule(self, condition: str, data_queries: list) -> dict:
        """The method includes a functionality to test a rule specified by the condition and a list of data queries

        Args:
            condition (str): Specify the condition
            data_queries (list): Specify a list of datasource rule query objects

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the specified rule
        """
        pass

    def delete_ngalert_organization_configuration(self):
        """The method includes a functionality to delete the NGAlert organization admin configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_ngalert_organization_configuration(self) -> dict:
        """The method includes a functionality to get the NGAlert organization admin configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the NGAlert organization configuration
        """
        pass

    def create_or_update_ngalert_organization_configuration(
        self, alert_managers: list, alertmanagers_choice: str = "all"
    ):
        """The method includes a functionality to create or update the NGAlert organization admin configuration

        Args:
            alert_managers (list): Specify the list of alert manager names
            alertmanagers_choice (str): Specify the Alertmanagers choice (default all)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_ngalert_alertmanagers_by_organization(self) -> dict:
        """The method includes a functionality to get the discovered and dropped Alertmanagers of the user's organization and based on the specified configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the NGAlert Alertmanagers
        """
        pass
