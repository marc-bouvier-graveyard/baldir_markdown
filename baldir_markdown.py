import argparse
import baldir_markdown_lib
import sys

parser = argparse.ArgumentParser(description='Baldir Markdown pre-processor')
parser.add_argument('path', type=str,
                    help='markdown file path')
parser.add_argument('-v', default=False,action="store_true",
                    help='verify mode. Runs the processor in dry-mode and fails if origin file does not match processed result')
args = parser.parse_args()
markdown_file_path = args.path
verify_mode = args.v

if verify_mode:
    result_matches_processed_file = baldir_markdown_lib.verify(
        markdown_file_path)
    if not result_matches_processed_file:
        print(markdown_file_path + ' is different after processing')
        print('Before : ')
        print('')
        print(baldir_markdown_lib.read_source_file(markdown_file_path))
        print('')
        print('-------------------')
        print('')
        print('After : ')
        print('')
        print(baldir_markdown_lib.pre_process_markdown_file_to_string(markdown_file_path))
        sys.exit(1)
    else:
        print(markdown_file_path + ' is the same after processing')
else:
    print(baldir_markdown_lib.pre_process_markdown_file_to_string(markdown_file_path))
