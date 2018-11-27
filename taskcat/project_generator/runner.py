# TODO delete this file after integrating with cli option parser
#      this is only here to illustrate generator's usage
# run as: python path/to/runner.py <project_destination>
#

import sys
from generator import ProjectConfiguration, ProjectGenerator
from filesystem import FilesystemService

destination = sys.argv[1]
config = ProjectConfiguration(
    'owner@example.com',
    'awesome_quickstart',
    'quickstart',
    ['us-east-1', 'us-west-2']
)
ProjectGenerator(
    config,
    destination,
    FilesystemService()
).generate()
