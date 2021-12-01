// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package picasso

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Dashboard struct {
	pulumi.ResourceState
}

// NewDashboard registers a new resource with the given unique name, arguments, and options.
func NewDashboard(ctx *pulumi.Context,
	name string, args *DashboardArgs, opts ...pulumi.ResourceOption) (*Dashboard, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DashProps == nil {
		return nil, errors.New("invalid value for required argument 'DashProps'")
	}
	var resource Dashboard
	err := ctx.RegisterRemoteComponentResource("picasso:index:Dashboard", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type dashboardArgs struct {
	// The dashboard properties json.
	DashProps string `pulumi:"dashProps"`
}

// The set of arguments for constructing a Dashboard resource.
type DashboardArgs struct {
	// The dashboard properties json.
	DashProps pulumi.StringInput
}

func (DashboardArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dashboardArgs)(nil)).Elem()
}

type DashboardInput interface {
	pulumi.Input

	ToDashboardOutput() DashboardOutput
	ToDashboardOutputWithContext(ctx context.Context) DashboardOutput
}

func (*Dashboard) ElementType() reflect.Type {
	return reflect.TypeOf((*Dashboard)(nil))
}

func (i *Dashboard) ToDashboardOutput() DashboardOutput {
	return i.ToDashboardOutputWithContext(context.Background())
}

func (i *Dashboard) ToDashboardOutputWithContext(ctx context.Context) DashboardOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DashboardOutput)
}

func (i *Dashboard) ToDashboardPtrOutput() DashboardPtrOutput {
	return i.ToDashboardPtrOutputWithContext(context.Background())
}

func (i *Dashboard) ToDashboardPtrOutputWithContext(ctx context.Context) DashboardPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DashboardPtrOutput)
}

type DashboardPtrInput interface {
	pulumi.Input

	ToDashboardPtrOutput() DashboardPtrOutput
	ToDashboardPtrOutputWithContext(ctx context.Context) DashboardPtrOutput
}

type dashboardPtrType DashboardArgs

func (*dashboardPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Dashboard)(nil))
}

func (i *dashboardPtrType) ToDashboardPtrOutput() DashboardPtrOutput {
	return i.ToDashboardPtrOutputWithContext(context.Background())
}

func (i *dashboardPtrType) ToDashboardPtrOutputWithContext(ctx context.Context) DashboardPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DashboardPtrOutput)
}

// DashboardArrayInput is an input type that accepts DashboardArray and DashboardArrayOutput values.
// You can construct a concrete instance of `DashboardArrayInput` via:
//
//          DashboardArray{ DashboardArgs{...} }
type DashboardArrayInput interface {
	pulumi.Input

	ToDashboardArrayOutput() DashboardArrayOutput
	ToDashboardArrayOutputWithContext(context.Context) DashboardArrayOutput
}

type DashboardArray []DashboardInput

func (DashboardArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Dashboard)(nil))
}

func (i DashboardArray) ToDashboardArrayOutput() DashboardArrayOutput {
	return i.ToDashboardArrayOutputWithContext(context.Background())
}

func (i DashboardArray) ToDashboardArrayOutputWithContext(ctx context.Context) DashboardArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DashboardArrayOutput)
}

// DashboardMapInput is an input type that accepts DashboardMap and DashboardMapOutput values.
// You can construct a concrete instance of `DashboardMapInput` via:
//
//          DashboardMap{ "key": DashboardArgs{...} }
type DashboardMapInput interface {
	pulumi.Input

	ToDashboardMapOutput() DashboardMapOutput
	ToDashboardMapOutputWithContext(context.Context) DashboardMapOutput
}

type DashboardMap map[string]DashboardInput

func (DashboardMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Dashboard)(nil))
}

func (i DashboardMap) ToDashboardMapOutput() DashboardMapOutput {
	return i.ToDashboardMapOutputWithContext(context.Background())
}

func (i DashboardMap) ToDashboardMapOutputWithContext(ctx context.Context) DashboardMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DashboardMapOutput)
}

type DashboardOutput struct {
	*pulumi.OutputState
}

func (DashboardOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Dashboard)(nil))
}

func (o DashboardOutput) ToDashboardOutput() DashboardOutput {
	return o
}

func (o DashboardOutput) ToDashboardOutputWithContext(ctx context.Context) DashboardOutput {
	return o
}

func (o DashboardOutput) ToDashboardPtrOutput() DashboardPtrOutput {
	return o.ToDashboardPtrOutputWithContext(context.Background())
}

func (o DashboardOutput) ToDashboardPtrOutputWithContext(ctx context.Context) DashboardPtrOutput {
	return o.ApplyT(func(v Dashboard) *Dashboard {
		return &v
	}).(DashboardPtrOutput)
}

type DashboardPtrOutput struct {
	*pulumi.OutputState
}

func (DashboardPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Dashboard)(nil))
}

func (o DashboardPtrOutput) ToDashboardPtrOutput() DashboardPtrOutput {
	return o
}

func (o DashboardPtrOutput) ToDashboardPtrOutputWithContext(ctx context.Context) DashboardPtrOutput {
	return o
}

type DashboardArrayOutput struct{ *pulumi.OutputState }

func (DashboardArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Dashboard)(nil))
}

func (o DashboardArrayOutput) ToDashboardArrayOutput() DashboardArrayOutput {
	return o
}

func (o DashboardArrayOutput) ToDashboardArrayOutputWithContext(ctx context.Context) DashboardArrayOutput {
	return o
}

func (o DashboardArrayOutput) Index(i pulumi.IntInput) DashboardOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Dashboard {
		return vs[0].([]Dashboard)[vs[1].(int)]
	}).(DashboardOutput)
}

type DashboardMapOutput struct{ *pulumi.OutputState }

func (DashboardMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Dashboard)(nil))
}

func (o DashboardMapOutput) ToDashboardMapOutput() DashboardMapOutput {
	return o
}

func (o DashboardMapOutput) ToDashboardMapOutputWithContext(ctx context.Context) DashboardMapOutput {
	return o
}

func (o DashboardMapOutput) MapIndex(k pulumi.StringInput) DashboardOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Dashboard {
		return vs[0].(map[string]Dashboard)[vs[1].(string)]
	}).(DashboardOutput)
}

func init() {
	pulumi.RegisterOutputType(DashboardOutput{})
	pulumi.RegisterOutputType(DashboardPtrOutput{})
	pulumi.RegisterOutputType(DashboardArrayOutput{})
	pulumi.RegisterOutputType(DashboardMapOutput{})
}
