import great_expectations as gx
from great_expectations.profile.user_configurable_profiler import UserConfigurableProfiler

# Load GX context
context = gx.get_context()

# Load batch for the 'employees' table
datasource = context.get_datasource("mssql_trn")
data_asset = datasource.get_asset("employees")
batch_request = data_asset.build_batch_request()

# Create or load expectation suite
suite_name = "employees_warning_suite"
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=suite_name,
)

# Use the profiler to automatically create expectations
profiler = UserConfigurableProfiler(profile_dataset=validator)
suite = profiler.build_suite()

# Save the generated suite
validator.save_expectation_suite()
print(f"✅ Expectation suite '{suite_name}' created and saved using UserConfigurableProfiler.")