import argparse
import baldir_markdown_lib

parser = argparse.ArgumentParser(description='Baldir Markdown pre-processor')
parser.add_argument('path', type=str,
                    help='markdown file path')
args = parser.parse_args()
markdown_file_path = args.path

print(baldir_markdown_lib.pre_process_markdown_file_to_string(markdown_file_path))
