import pulumi
import table_resource

# Create the table resource
user_table = table_resource.Table("user-table", 
    table_name="anuj",
    size=100,
    read_only=False
)



# Export outputs
pulumi.export("table_name", user_table.name)
pulumi.export("table_id", user_table.id)
pulumi.export("created_at", user_table.created_at)

