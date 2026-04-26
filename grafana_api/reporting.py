import json
import logging
from typing import Union

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    Report,
    ReportBrandingSettings,
)
from .api import Api


class Reporting:
    """The class includes all necessary methods to access the Grafana reporting API endpoints. Be aware that the functionality is a Grafana ENTERPRISE v7.0+ feature

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_reports(self) -> list:
        """The method includes a functionality to get all reports

        Required Permissions:
            Action: reports:read
            Scope: [reports:*, reports:id:*]

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all reports
        """
        pass

    def get_report_by_id(self, id: int) -> dict:
        """The method includes a functionality to get a report specified by the report id

        Args:
            id (int): Specify the report id

        Required Permissions:
            Action: reports:read
            Scope: [reports:*, reports:id:*, reports:id:<report_id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the report
        """
        pass

    def create_report(self, report: Report) -> int:
        """The method includes a functionality to create a report

        Args:
            report (Report): Specify the report object

        Required Permissions:
            Action: reports:create
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the report id
        """
        pass

    def update_report(self, id: int, report: Report):
        """The method includes a functionality to update a report

        Args:
            id (int): Specify the report id
            report (Report): Specify the report object

        Required Permissions:
            Action: reports:write
            Scope: [reports:*, reports:id:*, reports:id:<report_id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def delete_report(self, id: int):
        """The method includes a functionality to delete a report specified by the report id

        Args:
            id (int): Specify the report id

        Required Permissions:
            Action: reports:delete
            Scope: [reports:*, reports:id:*, reports:id:<report_id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def send_report(
        self, id: int, emails: str = None, use_emails_from_report: bool = None
    ):
        """The method includes a functionality to send a report to a specified email addresses

        Args:
            id (int): Specify the id of forwarded report. It is the same as in the URL when editing a report, not to be confused with the id of the dashboard.
            emails (str): Specify the comma-separated list of emails to which to send the report to. Overrides the emails from the report. Required if useEmailsFromReport is not present (default None)
            use_emails_from_report (bool): Specify if the emails inside the report should be used. Required if emails is not present (default None)

        Required Permissions:
            Action: reports:send
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def get_report_branding_settings(self) -> dict:
        """The method includes a functionality to get the report branding settings

        Required Permissions:
            Action: reports.settings:read
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the report branding settings
        """
        pass

    def save_report_branding_settings(self, branding_settings: ReportBrandingSettings):
        """The method includes a functionality to save the report branding settings

        Args:
            branding_settings (ReportBrandingSettings): Specify the report branding settings object.

        Required Permissions:
            Action: reports.settings:write
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    def send_report_test_email(self, report: Report):
        """The method includes a functionality to send a test report email

        Args:
            report (Report): Specify the report object

        Required Permissions:
            Action: reports: send
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        pass

    @staticmethod
    def _validate_report_object(report: Report) -> Union[bool, dict]:
        pass
