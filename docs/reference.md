This part of the project documentation focuses on
an **information-oriented** approach. You can find all helper methods
defined by the "ifft_core" module here. You'll find detailed information
about the method signatures, return types, exceptions, and examples.

The module contains the following functions:

- `get_modified_lines(repo, filename) - Get a set of modified lines for the given filename.`
- `scan_file(project_path, filename, modified_lines_set) - Scan the file for IFFT blocks and return the results.`
- `scan_files(project_path, dir_path_mock_project) - Scan the repository for modified Python files and return the results in a dictionary.`
- `validate_associated_file(associated_file_name)` - Validade if the associated file specified in IFFT block exists.

### **Note:** For the examples in this documentation, the plus sign (+) indicates a modified line.

::: ifft_core.ifft_parser
