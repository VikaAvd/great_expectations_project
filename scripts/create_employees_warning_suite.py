import great_expectations as gx

context = gx.get_context()

# ✅ Fluent API: build batch request from datasource and asset
batch_request = context.get_datasource("mssql_trn").get_asset("employees").build_batch_request()

# ✅ Create suite
suite_name = "employees_warning_suite"
context.add_or_update_expectation_suite(expectation_suite_name=suite_name)

# ✅ Get validator
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=suite_name,
)

# ✅ Add expectations
# employee_id: must be unique and not null
validator.expect_column_values_to_not_be_null("employee_id")
validator.expect_column_values_to_be_unique("employee_id")

# email: must be unique and not null
validator.expect_column_values_to_not_be_null("email")
validator.expect_column_values_to_be_unique("email")

# hire_date: date, must be not null and in the past
validator.expect_column_values_to_not_be_null("hire_date")

# salary: decimal(8,2), must be within reasonable range
validator.expect_column_values_to_be_of_type("salary", "DECIMAL")
validator.expect_column_values_to_be_between("salary", min_value=2500, max_value=25000)

# job_id: integer, must not be null
validator.expect_column_values_to_be_of_type("job_id", "INTEGER")
validator.expect_column_values_to_not_be_null("job_id")

# department_id: integer, must not be null
validator.expect_column_values_to_be_of_type("department_id", "INTEGER")
validator.expect_column_values_to_not_be_null("department_id")

# ✅ Save suite
validator.save_expectation_suite(discard_failed_expectations=False)

print(f"✅ Expectation suite '{suite_name}' created and saved.")
