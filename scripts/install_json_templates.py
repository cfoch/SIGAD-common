import glob
import os


SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.join(SCRIPTS_DIR, os.pardir)
JSON_SCHEMAS_DIR = os.path.join(ROOT_DIR, "json-schemas")
JSON_SCHEMAS_TEMPLATE_DIR = os.path.join(JSON_SCHEMAS_DIR, "templates")


template_filepaths = os.path.join(JSON_SCHEMAS_TEMPLATE_DIR, "*.template")
print(glob.glob(template_filepaths))
for filepath in glob.glob(template_filepaths):
    json_schema_basename = os.path.basename(os.path.splitext(filepath)[0])
    json_schema_filepath = os.path.join(JSON_SCHEMAS_DIR, json_schema_basename)
    with open(filepath, "r") as ifile, open(json_schema_filepath, "w") as ofile:
        content = ifile.read()
        content = content % JSON_SCHEMAS_TEMPLATE_DIR
        ofile.write(content)
