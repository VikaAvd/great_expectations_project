import great_expectations as gx

# Load the existing GX context
context = gx.get_context()

# Add MSSQL datasource with local connection string (use values!)
datasource = context.sources.add_or_update_sql(
    name="mssql_trn",
    connection_string="mssql+pyodbc://robot:Vika_password123@localhost:1433/TRN?driver=ODBC+Driver+17+for+SQL+Server"
)

print("✅ MSSQL datasource 'mssql_trn' connected successfully.")
