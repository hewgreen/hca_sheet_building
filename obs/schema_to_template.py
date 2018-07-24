#!/usr/bin/env python


from ingest.template.schema_template import SchemaTemplate

# builds a full spreadsheet from dev
schemas = [
    "http://schema.dev.data.humancellatlas.org/type/project/latest/project",
    "http://schema.dev.data.humancellatlas.org/type/biomaterial/latest/cell_suspension",
    "http://schema.dev.data.humancellatlas.org/type/biomaterial/latest/specimen_from_organism",
    "http://schema.dev.data.humancellatlas.org/type/biomaterial/latest/donor_organism",
    "http://schema.dev.data.humancellatlas.org/type/file/latest/sequence_file",
    "http://schema.dev.data.humancellatlas.org/type/protocol/biomaterial_collection/latest/dissociation_protocol",
    "http://schema.dev.data.humancellatlas.org/type/protocol/biomaterial_collection/latest/enrichment_protocol",
    "http://schema.dev.data.humancellatlas.org/type/protocol/sequencing/latest/library_preparation_protocol",
    "http://schema.dev.data.humancellatlas.org/type/protocol/sequencing/latest/sequencing_protocol",
    "http://schema.dev.data.humancellatlas.org/type/protocol/imaging/latest/imaging_protocol",
    "http://schema.dev.data.humancellatlas.org/type/protocol/biomaterial_collection/latest/collection_protocol",
    "http://schema.dev.data.humancellatlas.org/type/biomaterial/latest/cell_line",
    "http://schema.dev.data.humancellatlas.org/type/biomaterial/latest/organoid",
    "http://schema.dev.data.humancellatlas.org/type/process/latest/process"
]

# latest test
# schemas = [
#     "https://schema.humancellatlas.org/type/protocol/sequencing/7.0.0/sequencing_protocol",
#     "https://schema.humancellatlas.org/type/biomaterial/6.1.1/cell_suspension",
#     "https://schema.humancellatlas.org/type/file/6.1.1/sequence_file",
#     "https://schema.humancellatlas.org/type/protocol/6.1.1/protocol",
#     "https://schema.humancellatlas.org/type/protocol/analysis/6.1.1/analysis_protocol",
#     "https://schema.humancellatlas.org/type/protocol/imaging/6.1.1/imaging_protocol",
#     "https://schema.humancellatlas.org/type/biomaterial/5.2.2/specimen_from_organism",
#     "https://schema.humancellatlas.org/type/biomaterial/5.2.1/cell_line",
#     "https://schema.humancellatlas.org/type/biomaterial/5.2.1/donor_organism",
#     "https://schema.humancellatlas.org/type/biomaterial/5.2.1/organoid",
#     "https://schema.humancellatlas.org/type/file/5.2.1/analysis_file",
#     "https://schema.humancellatlas.org/type/project/5.2.1/project",
#     "https://schema.humancellatlas.org/type/protocol/biomaterial/5.1.0/biomaterial_collection_protocol",
#     "https://schema.humancellatlas.org/type/protocol/sequencing/3.0.0/library_preparation_protocol",
#     "https://schema.humancellatlas.org/type/process/2.1.1/process",
#     "https://schema.humancellatlas.org/type/protocol/biomaterial_collection/2.0.0/dissociation_protocol",
#     "https://schema.humancellatlas.org/type/protocol/biomaterial_collection/2.0.0/enrichment_protocol",
#     "https://schema.humancellatlas.org/type/file/1.1.1/reference_file"
#     # https://schema.humancellatlas.org/type/process/analysis/5.1.0/analysis_process
#     # https://schema.humancellatlas.org/type/process/biomaterial_collection/5.1.0/collection_process
#     # https://schema.humancellatlas.org/type/process/biomaterial_collection/5.1.0/dissociation_process
#     # https://schema.humancellatlas.org/type/process/biomaterial_collection/5.1.0/enrichment_process
#     # https://schema.humancellatlas.org/type/process/imaging/5.1.0/imaging_process
#     # https://schema.humancellatlas.org/type/process/sequencing/5.1.0/library_preparation_process
#     # https://schema.humancellatlas.org/type/process/sequencing/5.1.0/sequencing_process
# ]

template = SchemaTemplate(list_of_schema_urls=schemas)

# get key from user friendly name

# tabs = TabConfig().load("tabs_human_10x.yaml")

# print (template.get_key_for_label("Biomaterial name", tab="Cell suspension"))

# # lookup where to submit this entity

# print (template.lookup("cell_suspension.schema.domain_entity"))

# # lookup text field for donor_organism.human_specific.ethnicity.text

# print (template.get_key_for_label("donor_organism.human_specific.ethnicity.text", tab="Donor organism"))



# # lookup the schema url for project_core

# print (template.lookup("project.project_core.schema.url"))

# # get the user friendly name

# print (template.lookup("project.project_core.project_title.user_friendly"))

# # dump the config in yaml or json

print(template.yaml_dump(tabs_only=True))
# print(data.json_dump())
