import os

Notebook_name= "Arvind_Notebook_info.ipynb"
output_format="pdf"

os.system(f"jupyter nbconverter --to {output_format} {Notebook_name}")