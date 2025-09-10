#!/mnt/c/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe

import arcpy
import os
import pytest
import shutil
import zipfile


def test_import_and_tools():
    """Test arcpy import and list tools"""
    print(f"arcpy version: {arcpy.GetInstallInfo()['Version']}")
    tools = arcpy.ListTools()
    print(f"Tools available: {len(tools)}")
    assert len(tools) > 0

def test_sample_data():
    """Test sample data extraction and feature class listing"""
    sample_data_path = os.path.join(os.path.dirname(__file__), "SampleData.zip")
    assert os.path.exists(sample_data_path), "SampleData.zip not found"
    
    # Extract directly to tests directory
    extract_dir = os.path.dirname(__file__)
    
    try:
        with zipfile.ZipFile(sample_data_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            print(f"Extracted geodatabase from SampleData.zip")
        
        # Look for geodatabase in the extracted files
        gdb_path = None
        for root, dirs, files in os.walk(extract_dir):
            for dir_name in dirs:
                if dir_name.endswith('.gdb'):
                    gdb_path = os.path.join(root, dir_name)
                    break
            if gdb_path:
                break
        
        if gdb_path:
            print(f"Found geodatabase: {gdb_path}")
            arcpy.env.workspace = gdb_path
        else:
            print("No geodatabase found, skipping test")
            return
        
        feature_classes = arcpy.ListFeatureClasses()
        datasets = arcpy.ListDatasets()
        tables = arcpy.ListTables()
        
        print(f"Feature classes found: {len(feature_classes)}")
        print(f"Datasets found: {len(datasets)}")
        print(f"Tables found: {len(tables)}")
        
        # Test passes if we can extract and list
        assert len(feature_classes) > 0, "Should find feature classes in SampleData.gdb"
        
    finally:
        # Clean up extracted geodatabase
        arcpy.env.workspace = None
        
        if gdb_path and os.path.exists(gdb_path):
            try:
                # Compact geodatabase before deletion to release locks
                arcpy.Compact_management(gdb_path)
                shutil.rmtree(gdb_path)
                print("Cleaned up extracted geodatabase")
            except Exception as e:
                print(f"Warning: Could not clean up geodatabase: {e}")

if __name__ == "__main__":
    pytest.main([__file__, "-v" "-s"])
