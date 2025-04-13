import great_expectations as gx
import great_expectations.expectations as gxe

# Create a file-based GX context (folder will be created automatically)
context = gx.get_context(mode="file")

print("✅ Context created at:", context.root_directory)


