
from ingest.template.spreadsheet_builder import SpreadsheetBuilder

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
    "http://schema.dev.data.humancellatlas.org/type/biomaterial/latest/organoid"
]

spreadsheet_builder = SpreadsheetBuilder("all_latest_dev_template.xlsx")
spreadsheet_builder.generate_workbook(schema_urls=schemas)
spreadsheet_builder.save_workbook()