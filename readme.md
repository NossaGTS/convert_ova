# OVA to QCOW2 Converter

This script extracts a VMDK file from an OVA file and converts it to QCOW2 format for use with QEMU.

## Description

The script performs the following steps:
1. Extracts the contents of an OVA file into a specified directory.
2. Retrieves the VMDK file from the extracted contents.
3. Converts the VMDK file to QCOW2 format.

## Prerequisites

- Python 3.x
- `qemu-img` tool installed on your system

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/ova-to-qcow2-converter.git
cd ova-to-qcow2-converter
```

## Usage

To run the script, use the following command:

```bash
./convert_ova.py -n <ova_name> -p <path_to_ova_file>
```

### Arguments

- `-n`, `--name` : The name of the OVA file (without the `.ova` extension).
- `-p`, `--path` : The path to the directory containing the OVA file.

### Example

```bash
./convert_ova.py -n my_ova_file -p /path/to/ova
```

## Functions

### `unzip_ova(ova_path, ova_name)`

Unzips an OVA file into a specified directory and retrieves the VMDK file.

**Parameters:**
- `ova_path` (str): The path to the OVA file to be unzipped.
- `ova_name` (str): The name of the OVA file, used to create the output directory.

**Returns:**
- `str`: The name of the VMDK file extracted from the OVA file.

**Raises:**
- `Exception`: If an error occurs during the extraction process.

### `convert_to_qcow(vmdk_file, ova_name)`

Converts a VMDK file to QCOW2 format for use with QEMU.

**Parameters:**
- `vmdk_file` (str): The path to the VMDK file to be converted.
- `ova_name` (str): The name of the OVA file, used to create the output directory and name the resulting QCOW2 file.

**Returns:**
- `None`

**Raises:**
- `Exception`: If an error occurs during the conversion process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script utilizes the `qemu-img` tool for converting VMDK files to QCOW2 format.
```