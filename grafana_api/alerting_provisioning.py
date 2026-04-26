import json
import logging
from typing import List

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    AlertRule,
    AlertQuery,
    AlertRuleQueryModel,
    AlertRuleQueryModelCondition,
    EmbeddedContactPoint,
    Route,
    Matcher,
    MuteTimeInterval,
    TimeInterval,
    TimeRange,
)
from .api import Api


class AlertingProvisioning:
    """The class includes all necessary methods to access the Grafana alerting provisioning API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alert_rule(self, uid: str) -> dict:
        """The method includes a functionality to get the alert rule specified by the uid

        Args:
            uid (str): Specify the alert rule uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the alert rule
        """
        pass

    def add_alert_rule(self, alert_rule: AlertRule, disable_provenance: bool = False):
        """The method includes a functionality to create a new alert rule

        Args:
            alert_rule (AlertRule): Specify the alert rule
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_alert_rule(
        self, uid: str, alert_rule: AlertRule, disable_provenance: bool = False
    ):
        """The method includes a functionality to update an existing alert rule

        Args:
            uid (str): Specify the alert rule uid
            alert_rule (AlertRule): Specify the alert rule
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_the_interval_of_a_alert_rule_group(
        self,
        folder_uid: str,
        group: str,
        alert_rule_group_interval: int,
        disable_provenance: bool = False,
    ):
        """The method includes a functionality to update the interval of a alert rule group

        Args:
            folder_uid (str): Specify the folder uid
            group (str): Specify the group
            alert_rule_group_interval (int): Specify the alert rule group interval
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_alert_rule(self, uid: str, disable_provenance: bool = False):
        """The method includes a functionality to delete an alert rule

        Args:
            uid (str): Specify the alert rule uid
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call
        Returns:
            None
        """
        pass

    def get_all_contact_points(self) -> list:
        """The method includes a functionality to get all contact points

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all contact points
        """
        pass

    def add_contact_point(
        self,
        embedded_contact_point: EmbeddedContactPoint,
        disable_provenance: bool = False,
    ):
        """The method includes a functionality to create a contact point

        Args:
            embedded_contact_point (EmbeddedContactPoint): Specify the embedded contact point
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_contact_point(
        self,
        uid: str,
        embedded_contact_point: EmbeddedContactPoint,
        disable_provenance: bool = False,
    ):
        """The method includes a functionality to update a contact point

        Args:
            uid (str): Specify the uid of the contact point
            embedded_contact_point (EmbeddedContactPoint): Specify the embedded contact point
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_contact_point(self, uid: str):
        """The method includes a functionality to delete a contact point

        Args:
            uid (str): Specify the uid of the contact point

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_notification_policies(self) -> dict:
        """The method includes a functionality to get the notification policy tree

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the notification policy tree
        """
        pass

    def add_notification_policies(self, route: Route, disable_provenance: bool = False):
        """The method includes a functionality to set the notification policy tree

        Args:
            route (Route): Specify the alert rule routes
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_all_mute_timings(self) -> list:
        """The method includes a functionality to get all mute timings

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all mute timings
        """
        pass

    def get_mute_timing(self, name: str) -> dict:
        """The method includes a functionality to get a mute timings specified by the name

        Args:
            name (str): Specify the mute timing name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the mute timing
        """
        pass

    def add_mute_timing(
        self, mute_time_interval: MuteTimeInterval, disable_provenance: bool = False
    ):
        """The method includes a functionality to create a mute timing

        Args:
            mute_time_interval (MuteTimeInterval): Specify the mute time interval
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def update_mute_timing(
        self,
        name: str,
        mute_time_interval: MuteTimeInterval,
        disable_provenance: bool = False,
    ):
        """The method includes a functionality to update an existing mute timing

        Args:
            name (str): Specify the mute timing name
            mute_time_interval (MuteTimeInterval): Specify the mute time interval
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_mute_timing(self, name: str):
        """The method includes a functionality to delete a mute timings specified by the name

        Args:
            name (str): Specify the mute timing name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_all_message_templates(self) -> list:
        """The method includes a functionality to get all message templates

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all message templates
        """
        pass

    def get_message_template(self, name: str) -> dict:
        """The method includes a functionality to get a message template specified by the name

        Args:
            name (str): Specify the message template name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the message template
        """
        pass

    def create_or_update_message_template(
        self, name: str, message_template: str, disable_provenance: bool = False
    ):
        """The method includes a functionality to create or update a message template

        Args:
            name (str): Specify the message template name
            message_template (str): Specify the message template
            disable_provenance (bool): Specify if the provenance header should be set or not (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_message_template(self, name: str):
        """The method includes a functionality to delete a message template

        Args:
            name (str): Specify the message template name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def _create_mute_timing_dictionary(
        self, mute_time_interval: MuteTimeInterval
    ) -> dict:
        """The method includes a functionality to create the mute timing dictionary

        Args:
            mute_time_interval (MuteTimeInterval): Specify the mute time interval

        Returns:
            result (dict): Returns the mute timing dictionary
        """
        pass

    def _create_mute_timing_interval_list(
        self, time_intervals: List[TimeInterval]
    ) -> (list, None):
        """The method includes a functionality to create the mute timing interval list

        Args:
            time_intervals (List[TimeInterval]): Specify the list of time intervals

        Returns:
            result (list, None): Returns the mute time interval list or None
        """
        pass

    @staticmethod
    def _create_time_range_list(timing: List[TimeRange]) -> (list, None):
        """The method includes a functionality to create the time range list

        Args:
            timing (List[TimeRange]): Specify the list of time points

        Returns:
            timing_list (list): Returns the time list
        """
        pass

    def _create_alert_route_dictionary(self, route: Route) -> dict:
        """The method includes a functionality to create the alert route dictionary

        Args:
            route (Route): Specify the route

        Returns:
            result (dict): Returns the alert route dictionary
        """
        pass

    def _create_alert_routes_list(self, routes: List[Route]) -> (list, None):
        """The method includes a functionality to create the alert route list

        Args:
            routes (List[Route]): Specify the list of alert routes

        Returns:
            result (list, None): Returns the alert routes list or None
        """
        pass

    @staticmethod
    def _create_object_matcher_list(matchers: List[Matcher]) -> (list, None):
        """The method includes a functionality to create the object matcher list

        Args:
            matchers (List[Matcher]): Specify the list of object matchers

        Returns:
            route_matchers_list (list): Returns the list of object matchers
        """
        pass

    def _create_alert_rule_dictionary(self, alert_rule: AlertRule) -> dict:
        """The method includes a functionality to create the alert rule dictionary

        Args:
            alert_rule (AlertRule): Specify the alert rule

        Returns:
            result (dict): Returns the alert rule dictionary
        """
        pass

    def _create_alert_rule_query_list(self, alert_queries: List[AlertQuery]) -> list:
        """The method includes a functionality to create the alert rule query list

        Args:
            alert_queries (List[AlertQuery]): Specify the alert rule query list

        Returns:
            alert_rule_queries_list (list): Returns the alert rule query list
        """
        pass

    def _create_alert_rule_query_model_dictionary(
        self, alert_query_model: AlertRuleQueryModel
    ) -> dict:
        """The method includes a functionality to create the alert rule query model dictionary

        Args:
            alert_query_model (AlertRuleQueryModel): Specify the alert rule query model

        Returns:
            result (dict): Returns the alert rule query model dictionary
        """
        pass

    @staticmethod
    def _create_alert_rule_query_model_condition_list(
        alert_rule_query_model_conditions: List[AlertRuleQueryModelCondition],
    ) -> list:
        """The method includes a functionality to create the alert rule query model condition list

        Args:
            alert_rule_query_model_conditions (List[AlertRuleQueryModelCondition]): Specify the alert rule query model conditions list

        Returns:
            alert_rule_query_model_conditions_list (list): Returns the alert rule query model conditions list
        """
        pass
