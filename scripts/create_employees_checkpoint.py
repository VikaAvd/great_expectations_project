import great_expectations as gx

# Load GX context
context = gx.get_context()

# Define checkpoint
checkpoint = context.add_or_update_checkpoint(
    name="employees_checkpoint",
    validations=[
        {
            "batch_request": {
                "datasource_name": "mssql_trn",
                "data_asset_name": "employees",
            },
            "expectation_suite_name": "employees_warning_suite",  # or use "employees_profiled_suite"
        }
    ]
)

# Run the checkpoint
results = checkpoint.run()

# Check success status
if results["success"]:
    print("✅ Checkpoint succeeded! Data meets expectations.")
else:
    print("❌ Checkpoint failed! Some expectations did not pass.")
