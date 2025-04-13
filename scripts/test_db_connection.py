import great_expectations as gx

# Load context
context = gx.get_context()

# Get the datasource
datasource = context.get_datasource("mssql_trn")

# Access an asset (table)
# If not registered yet, we need to register it first (we can do that next)
asset = datasource.get_asset("employees")

# Build the batch request
batch_request = asset.build_batch_request()

# Load a validator
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name="test_suite"
)

# Show some data
print("✅ Connection successful! Here's a preview of your data:")
print(validator.head())
