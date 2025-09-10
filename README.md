# Arcpy3 WSL2

![Tech Stacks](https://skillicons.dev/icons?i=python,linux,bash,docker)

## Overview

This project provides a seamless way to use ArcGIS Pro's Python (arcpy) from within WSL2 (Windows Subsystem for Linux). It allows you to:

1. Access Windows ArcGIS Pro's arcpy functionality from WSL2
2. Run automated tests to verify arcpy functionality
3. Work with sample data and geodatabases in a Linux environment

## Quick Start

### Prerequisites

- Windows 10/11 with WSL2 enabled
- ArcGIS Pro installed on Windows

### Running Tests

#### Basic ArcPy Test
```bash
"/mnt/c/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe" -m pytest tests/test.py 2>/dev/null
```

#### Test with verbose output
```bash
"/mnt/c/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe" -m pytest tests/test.py -v -s 2>/dev/null
```

#### Using ArcPy from WSL2
```bash
"/mnt/c/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe" xxx.py
```

#### Test with Docker (Experimental)
```bash
docker-compose up --build
```

## Version Compatibility

- **ArcGIS Pro**: 3.1.2+ (tested with 3.1.2)
- **Python**: 3.9.16 (ArcGIS Pro default)
- **WSL2**: Ubuntu 24.04 LTS
- **Docker**: Any recent version
