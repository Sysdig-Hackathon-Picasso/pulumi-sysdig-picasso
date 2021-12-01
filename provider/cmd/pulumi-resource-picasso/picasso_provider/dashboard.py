# Copyright 2016-2021, Pulumi Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from typing import Optional

from pulumi import Inputs, ResourceOptions
import pulumi_sysdig as ps
import pulumi


class DashboardArgs:

    dash_props: pulumi.Input[str]
    """The properties."""

    @staticmethod
    def from_inputs(inputs: Inputs) -> 'DashboardArgs':
        return DashboardArgs(dash_props=inputs['dashProps'])

    def __init__(self, dash_props: pulumi.Input[str]) -> None:
        # self.dash_props = dash_props
        self.dash_props = """
        {
            "name": "[P0] NATS Queue Backlog",
            "description": "This is the alert/dashboard for NATS Queue Backlog",
            "scope": "kubertnes.cluster.name in prod*",
            "dashboard":[
                {
                    "runbook": "# Runbook Title\nThis runbook describes something.",
                    "query": "pippo.pluto",
                    "threashold": "",
                    "unit": "percent"
                }
            ],
            "alert": {
                "query": "",
                "duration": "",
                "channels": [1,2,3],
                "renotification_minutes": 10,
                "severity": 4,
                "trigger_after_minutes": 5,
            }
        }
        """

class Dashboard(pulumi.ComponentResource):
    dashboard = None
    alert = None

    def __init__(self,
                 name: str,
                 args: DashboardArgs,
                 props: Optional[dict] = None,
                 opts: Optional[ResourceOptions] = None) -> None:

        super().__init__('picasso:index:Dashboard', name, props, opts)

        dashProps = json.loads(args.dash_props)

        dashboard_name = self.get_dashboard_name(dashProps["name"])
        alert_name = dashProps["name"]

        dashboard_panel_args = self.get_dashboard_panel_args(
            dashProps["dashboard"])

        dashboard_args = ps.monitor.DashboardArgs(
            name=dashboard_name,
            description=dashProps["description"],
            public=False,
            panels=dashboard_panel_args
        )

        # self.dashboard_scope_args = ps.monitor.DashboardScopeArgs

        dashboard = ps.monitor.Dashboard(
            resource_name=dashboard_name,  # TODO check what resource name is
            args=dashboard_args,
            scopes=None
        )

        alert_args = ps.monitor.AlertPromqlArgs(
            enabled=True,
            name=alert_name,
            promql=dashProps["alert"]["query"],
            notification_channels=dashProps["alert"]["channels"],
            scope=dashProps["scope"],
            renotification_minutes=dashProps["renotification_minutes"],
            severity=dashProps["severity"],
            trigger_after_minutes=dashProps["trigger_after_minutes"]

        )
        alert = ps.monitor.AlertPromql(
            resource_name=alert_name,  # TODO check what resource name is
            args=alert_args
        )

        self.dashboard = dashboard
        self.alert = alert

        self.register_outputs({
            # "dashboard": dashboard,
            # "alert": alert
        })

    @staticmethod
    def get_dashboard_name(name):
        return "Alert - " + name

    @staticmethod
    def get_dashboard_panel_args(dashboard):
        dash_panels = list()
        for dash_item in dashboard:
            runbook = ps.monitor.DashboardPanelArgs(
                height=5,
                width=15,
                pos_x=0,
                pos_y=0,
                transparent_background=True,
                type="text",
                content=dash_item["runbook"]
            )

            plot = ps.monitor.DashboardPanelArgs(
                name="testPanel",
                description="ciao descr",
                height=15,
                width=15,
                pos_x=0,
                pos_y=5,
                type="timechart",
                queries=[
                    ps.monitor.DashboardPanelQueryArgs(
                        promql=dash_item["query"],
                        unit=dash_item["unit"]
                    ),
                    ps.monitor.DashboardPanelQueryArgs(
                        promql=dash_item["threshold"],
                        unit=dash_item["unit"]
                    )
                ]
            )
            dash_panels.append(runbook)
            dash_panels.append(plot)

        return dash_panels
