import argparse
import os

# this attaches an action (if specified with 'action=MakeAbsolutePathAction')
# relative paths are converted to absolute paths for strictness
class MakeAbsolutePathAction(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		setattr(namespace, self.dest, os.path.abspath(values))


def setup_args():
	"""
	This method sets up the potential commandline arguments.
	Add/edit here
	"""
	parser = argparse.ArgumentParser()

	parser.add_argument("-d", "--dir", 
				required=True, 
				help="Full path to the project directory.",
				action=MakeAbsolutePathAction,
				dest="project_directory")

	parser.add_argument("-g", "--genome", 
				required=True,
				help="The reference genome." ,
				dest="genome")

	parser.add_argument("-o", "--output",
				required=True,
				help="Full path to the output directory.",
				action=MakeAbsolutePathAction,
				dest="output_location")

	parser.add_argument("-s", "--samples",
				required=True,
				help="The path to a sample annotation file (for formatting, see documentation).",
				action=MakeAbsolutePathAction,
				dest="sample_annotation_file")

	parser.add_argument("-a", "--aligner",
				required=False,
				help="The name of the aligner to use.",
				dest="aligner")

	parser.add_argument("-c", "--contrasts",
				required=False,
				help="The path to a contrast annotation file (for formatting, see documentation).",
				action=MakeAbsolutePathAction,
				dest="contrast_file")

	parser.add_argument("-config",
				required=False,
				default=None,
				help="Path to a custom project configuration file.",
				action=MakeAbsolutePathAction,
				dest="project_configuration_file")

	parser.add_argument("-skip_align",
				action="store_true",
				default=False,
				required=False,
				help="If skipping alignment (already have SAM/BAM files)",
				dest="skip_align")

	parser.add_argument("-paired",
				action="store_true",
				required=False,
				default=False,
				help="If paired alignment, with two FASTQ files",
				dest="paired_alignment")

	parser.add_argument("-skip_analysis",
				action="store_true",
				required=False,
				default=False,
				help="If skipping analysis.",
				dest="skip_analysis")

	parser.add_argument("-t","--target",
				required=False,
				default='bam',
				help="A tag (string) for selecting a particular set of (existing) BAM files to use with analysis.",
				dest="target_bam")

	return parser


def read():
	"""
	This reads the commandline arguments and returns a dictionary
	
	"""
	parser = setup_args()
	return vars(parser.parse_args())












 
