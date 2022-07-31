# DeepList
List of paths and file names that match a certain suffix

This project corresponds to the first coding exercise of Cocus Challenge.

Find all files within a path, with a given file name suffix. Note that a path may contain further subdirectories and 
those subdirectories may also contain further subdirectories. There is no limit to the depth of the subdirectories.

# Quick Start

## Install

Clone this respository and run the following command:

```basg
pip install -r requirements.txt
```

## Use

Example 1: List all paths and file names inside _/var/tmp_ that have the suffix _.log_.

```bash
./deep_list.py \*.log /var/tmp/
```

Or:

```bash
./deep_list.py "*.log" "/var/tmp/"
```

For more details about the syntax, please run:

```bash
deep_list.py --help
```

## Test

To run all unit tests, please run the following command:

```bash
python -m unittest
```