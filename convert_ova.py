#!/usr/bin/env python3
import os
import argparse
import shutil
import glob
import subprocess

def unzip_ova(ova_path, ova_name):
    """
    Unzips an OVA file into a specified directory and retrieves the VMDK file.

    This function takes the path to an OVA file and an OVA name, creates a 
    directory named after the OVA file, extracts the contents of the OVA file 
    into this directory, and retrieves the name of the VMDK file from the extracted contents.

    Parameters:
    ova_path (str): The path to the OVA file to be unzipped.
    ova_name (str): The name of the OVA file, used to create the output directory.

    Returns:
    str: The name of the VMDK file extracted from the OVA file.

    Raises:
    Exception: If an error occurs during the extraction process.
    """
    try:
        output_dir = output_path + f"/{ova_name}"
        print("Making output directory....")
        os.mkdir(output_dir)
        print("Extracting ova in output directory...")
        shutil.unpack_archive(filename=ova_path, extract_dir=output_dir, format="tar", filter="data")
        os.chdir(output_dir)
        print(f"Getting vmdk file from {output_dir}")
        vmdk_file = glob.glob("*.vmdk")[0]
    except Exception as e:
        print(e)
    return vmdk_file

def convert_to_qcow(vmdk_file, ova_name):
    """
    Converts a VMDK file to QCOW2 format for use with QEMU.

    This function takes the path to a VMDK file and an OVA name, and converts
    the VMDK file to QCOW2 format. The resulting QCOW2 file is saved in a
    directory named after the OVA file.

    Parameters:
    vmdk_file (str): The path to the VMDK file to be converted.
    ova_name (str): The name of the OVA file, used to create the output directory
                    and name the resulting QCOW2 file.

    Returns:
    None

    Raises:
    Exception: If an error occurs during the conversion process.

    """
    try:
        output_dir = output_path + f"/{ova_name}"
        os.chdir(output_dir)
        print("Converting vmdk to qcow2")
        result = subprocess.run(f"/usr/bin/qemu-img convert -f vmdk -O qcow2 {vmdk_file} {ova_name}.qcow2", capture_output=True,shell=True)

        if result.returncode == 0:
            print("Conversion completed successfully!")

    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", type=str, help="name of the ova file", required=True)
    parser.add_argument("-p", "--path", type=str, help="path of the ova file", required=True)
    args = parser.parse_args()
    ova_file = f"{args.name}.ova"
    ova_path = args.path+ "/" + ova_file
    global output_path
    output_path = os.path.expanduser(args.path)
    if os.path.exists(ova_path):
        ova_name = args.name
        vmdk_file = unzip_ova(ova_path, ova_name)
        convert_to_qcow(vmdk_file, ova_name)

if __name__ == "__main__":
    main()