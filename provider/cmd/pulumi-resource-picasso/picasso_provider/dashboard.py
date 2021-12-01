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

    index_query: pulumi.Input[str]
    """The query."""

    @staticmethod
    def from_inputs(inputs: Inputs) -> 'DashboardArgs':
        return DashboardArgs(index_query=inputs['indexQuery'])

    def __init__(self, index_query: pulumi.Input[str]) -> None:
        self.index_query = index_query


class Dashboard(pulumi.ComponentResource):
    def __init__(self,
                 name: str,
                 args: DashboardArgs,
                 props: Optional[dict] = None,
                 opts: Optional[ResourceOptions] = None) -> None:
                 
        super().__init__('picasso:index:Dashboard', name, props, opts)

        sysdig_monitor_url = "https://ec2-100-24-42-119.compute-1.amazonaws.com/"
        sysdig_monitor_insecure_tls = True
        sysdig_monitor_api_token = "9c0e2d3a-adac-482c-9fc1-11ee2c12f1e5"

        dashabord_args = ps.monitor.DashboardArgs(
            name="test-picasso",
            description="testing Magic Picasso",
            public=True
        )

        self.dashboard_panel_args = [ps.monitor.DashboardPanelArgs(
            name="testPanel",
            description="ciao descr",
            height=15,
            width=15,
            pos_x=0,    
            pos_y=0,
            transparent_background=True,
            type="timechart",
            queries=[ps.monitor.DashboardPanelQueryArgs(
                promql="pippo{id=pluto}",
                unit="percent"
            )]
        )]

        # self.dashboard_scope_args = ps.monitor.DashboardScopeArgs

        dashabord = ps.monitor.Dashboard(
            name="test-picasso"
            description="testing Magic Picasso"

        )

        self.register_outputs({
            # 'bucket': bucket,
            # 'websiteUrl': bucket.website_endpoint,
        })