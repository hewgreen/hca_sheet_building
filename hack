#!/usr/bin/env python

'''
Makes full user friendly YAML and sheet from dev latest. This can be edited and deleted as appropreate.
'''
import sys, argparse

from ingest.template.schema_template import SchemaTemplate
from ingest.template.spreadsheet_builder import SpreadsheetBuilder
from ingest.api.ingestapi import IngestApi


def main(args):
	if args.env is "master":
		ingest_api_root = "http://api.ingest.humancellatlas.org"
	elif args.env is "develop":
		ingest_api_root = "http://api.ingest.dev.data.humancellatlas.org"
	else:
		print('--env must be "master" or "develop"')
		sys.exit()


	schemas_api = ingest_api_root + "/schemas"
	latest_type_schemas_search = schemas_api + "/search/filterLatestSchemas?highLevelEntity=type"
	latest_schemas_resources = IngestApi._getAllObjectsFromSet(latest_type_schemas_search, "schemas", 50)


	latest_schemas_ = list(map(lambda schema_resource: schema_resource['_links']['json-schema']['href'], latest_schemas_resources))

	# remove some known irrelevent types
	remove_list = ['https://schema.humancellatlas.org/type/protocol/analysis/7.0.0/analysis_protocol',
	'https://schema.humancellatlas.org/type/file/5.2.1/analysis_file',
	'https://schema.humancellatlas.org/type/process/analysis/5.1.0/analysis_process',
	'https://schema.humancellatlas.org/type/process/3.0.0/process',
	'https://schema.humancellatlas.org/type/protocol/6.1.1/protocol',
	'https://schema.humancellatlas.org/type/process/analysis/5.1.0/analysis_process',
	'https://schema.humancellatlas.org/type/process/imaging/5.1.0/imaging_process',
	'https://schema.humancellatlas.org/type/process/3.0.0/process',
	'https://schema.humancellatlas.org/type/process/biomaterial_collection/5.1.0/collection_process',
	'https://schema.humancellatlas.org/type/process/biomaterial_collection/5.1.0/enrichment_process',
	'https://schema.humancellatlas.org/type/process/sequencing/5.1.0/library_preparation_process',
	'https://schema.humancellatlas.org/type/process/sequencing/5.1.0/sequencing_process',
	'https://schema.humancellatlas.org/type/process/biomaterial_collection/5.1.0/dissociation_process'
	]
	latest_schemas = [x for x in latest_schemas_ if x not in remove_list]



	print('\nMatt: git pull ingest-client locally for most up to date version!!!\n')

	print('\n\nUsing schemas:\n')
	# print(latest_schemas)
	print("\n latest_schemas size: " + str(len(latest_schemas)))

	# make yaml
	template = SchemaTemplate(list_of_schema_urls=latest_schemas)
	with open('config.yaml', 'w') as o:
		print(template.yaml_dump(tabs_only=True), file=o)

	# make spreadsheet
	spreadsheet_builder = SpreadsheetBuilder(args.sheet)
	spreadsheet_builder.generate_workbook(tabs_template=args.yaml)
	spreadsheet_builder.save_workbook()


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Gets latest complete list of schemas and makes a config YAML and a spreadsheet.')
	parser.add_argument('--env', '-e', help='Which env should it get schemas from? "develop" or "master"', default = "master")
	parser.add_argument('--sheet', '-s', help='Name of output spreadsheet', default = "dev_full_latest.xlsx")
	parser.add_argument('--yaml', '-y', help='Name of output yaml', default = "config.yaml")
	args = parser.parse_args()
	main(args)