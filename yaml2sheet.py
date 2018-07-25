#!/usr/bin/env python3

import argparse

from ingest.template.spreadsheet_builder import SpreadsheetBuilder

def main(args):
	yaml = args.yaml
	output_name = args.sheet

	# make spreadsheet
	spreadsheet_builder = SpreadsheetBuilder(output_name)
	spreadsheet_builder.generate_workbook(tabs_template=yaml)
	spreadsheet_builder.save_workbook()


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Makes a yaml into a sheet.')
	parser.add_argument('--yaml', '-y', help='Filename of input yaml')
	parser.add_argument('--sheet', '-s', help='Desired filename of output spreadsheet', default = "output.xlsx")
	args = parser.parse_args()
	main(args)