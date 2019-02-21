# DD tag parser

Tags parser for [deep_disfluency](https://github.com/dsg-bielefeld/deep_disfluency/).

## Installation

    pip install dd-tag-parser

## Usage

    > import dd_tag_parser
    >
    > dd_tag_parser('<e/><tc/><diact type="b"/>')
    [
	{
	    'tag': 'e',
	    'attributes': {},
	},
	{
	    'tag': 'tc',
	    'attributes': {},
	},
	{
	    'tag': 'diact',
	    'attributes': {'type': 'b'},
	},
    ]
