# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DashboardArgs', 'Dashboard']

@pulumi.input_type
class DashboardArgs:
    def __init__(__self__, *,
                 dash_props: pulumi.Input[str]):
        """
        The set of arguments for constructing a Dashboard resource.
        :param pulumi.Input[str] dash_props: The dashboard properties json.
        """
        pulumi.set(__self__, "dash_props", dash_props)

    @property
    @pulumi.getter(name="dashProps")
    def dash_props(self) -> pulumi.Input[str]:
        """
        The dashboard properties json.
        """
        return pulumi.get(self, "dash_props")

    @dash_props.setter
    def dash_props(self, value: pulumi.Input[str]):
        pulumi.set(self, "dash_props", value)


class Dashboard(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dash_props: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Dashboard resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dash_props: The dashboard properties json.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Dashboard resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DashboardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dash_props: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardArgs.__new__(DashboardArgs)

            if dash_props is None and not opts.urn:
                raise TypeError("Missing required property 'dash_props'")
            __props__.__dict__["dash_props"] = dash_props
        super(Dashboard, __self__).__init__(
            'picasso:index:Dashboard',
            resource_name,
            __props__,
            opts,
            remote=True)

