
## About
*make_dev_full_latest.py*
Outputs full yams and full sheet from dev latest. If new types are created these will need to be manually added.

Functionality
1. goes to the 'latest' endpoints to get the most up to date lists of latest schema (known missing feature: pull in deprecated types if they are the latest, the script is hard coded to remove some of these - working on a better solution)
2. makes a YAML file (known missing feature- the tabs and columns are not nicely ordered and no links are added)
3. use the YAML to make a spreadsheet

## Install

The code needs ingest-client:

You could try to install ingest-client with pip but I need the flexibility to install the dev code. Ingest-cli is a dependency and was broken when I was first trying this.

Install with pip:

`pip install hca-ingest`

But do this in a virtual env so:

`pip3 install virtualenv`
`virtualenv -p python3 hca-ingest-env`
`source hca-ingest-env/bin/activate`
`pip install hca-ingest`

If you need dev code (if stuff is broken and you want to run dev versions):

Again start a virtualenv.

Clone ingest-client locally I used `pip3 install -e ~/Google\ Drive/ingest-client/` this is install in the dev mode. Go to /Users/hewgreen/Google Drive/ingest-client and pull for latest build before using these scripts.

Working now `pip freeze` gives

hca==3.4.5
hca-cli==0.1.0
-e git+https://github.com/HumanCellAtlas/ingest-client@b5ba2a63a47dafe5f15611ce0b6b1acac7c8def4#egg=hca_ingest

If you get any errors it may be worth running `pip install -r requirements.txt`


Notes:

Old code is obsoleted in obs (archive directory) this may be in the .gitignore