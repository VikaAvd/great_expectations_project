import great_expectations as gx

context = gx.get_context()

# Register a new SQL datasource using the fluent v3 API
datasource = context.sources.add_sql(
    name="mssql_trn",
    connection_string="mssql+pyodbc://robot:Vika_password123@host.docker.internal:1433/TRN?driver=ODBC+Driver+17+for+SQL+Server"
)

# Add a table asset to this datasource (e.g., 'employees')
datasource.add_table_asset(name="employees", table_name="employees")

print("✅ Datasource 'mssql_trn' and asset 'employees' were registered.")
