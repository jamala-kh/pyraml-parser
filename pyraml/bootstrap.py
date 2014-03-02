__author__ = 'ad'

import mimetypes
import yaml
from raml_elements import ParserRamlInclude, ParserRamlNotNull
from constants import RAML_CONTENT_MIME_TYPES

# Bootstrapping: making able mimetypes package to recognize RAML and YAML file types
for mtype in RAML_CONTENT_MIME_TYPES:
    mimetypes.add_type(mtype, ".raml")
    mimetypes.add_type(mtype, ".yaml")

# making able mimetypes package to recognize JSON file type
mimetypes.add_type("application/json", ".json")


yaml.add_representer(ParserRamlInclude, ParserRamlInclude.representer)
yaml.add_constructor(ParserRamlInclude.yaml_tag, ParserRamlInclude.loader)
yaml.add_representer(ParserRamlNotNull, ParserRamlNotNull.representer)
yaml.add_constructor(ParserRamlNotNull.yaml_tag, ParserRamlNotNull.loader)
