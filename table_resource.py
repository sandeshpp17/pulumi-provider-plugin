import pulumi
from typing import Optional
from table_provider import TableProvider

class Table(pulumi.dynamic.Resource):
    name: pulumi.Output[str]
    size: pulumi.Output[int]
    read_only: pulumi.Output[bool]
    created_at: pulumi.Output[str]
    modified_at: pulumi.Output[str]

    def __init__(self, 
                 resource_name: str,
                 *,  # Force keyword arguments
                 table_name: pulumi.Input[str],
                 size: pulumi.Input[int],
                 read_only: pulumi.Input[bool],
                 opts: Optional[pulumi.ResourceOptions] = None):
        
        config = pulumi.Config("mock-service")
        endpoint = config.require("endpoint")
        
        props = {
            "name": table_name,
            "size": size,
            "read_only": read_only,
            "endpoint": endpoint,
            "created_at": None,
            "modified_at": None
        }

        super().__init__(TableProvider(), resource_name, props, opts)

