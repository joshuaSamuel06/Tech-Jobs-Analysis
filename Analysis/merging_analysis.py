import nbformat

def merge_notebooks(notebook_files, output_file):
    merged_notebook = nbformat.v4.new_notebook()

    for notebook_file in notebook_files:
        print(f"Processing {notebook_file}...")
        try:
            with open(notebook_file, 'r', encoding='utf-8') as f:
                notebook = nbformat.read(f, as_version=4)
                merged_notebook.cells.extend(notebook.cells)
        except Exception as e:
            print(f"Failed to process {notebook_file}: {e}")

    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(merged_notebook, f)
    print(f"Merged notebook saved to {output_file}")

# List of notebook files to merge
notebook_files = [
    'Analysis/Joshua/Data_Cleaning_and_Analysis/Data_Analysis/Analysis.ipynb',
    'Analysis/Mustafa-analysis/data_analysis.ipynb',
    'Analysis/Negin-Analysis/Data-Analysis/Visualize.ipynb'
]

# Output file name
output_file = 'merged_notebook.ipynb'

# Merge the notebooks
merge_notebooks(notebook_files, output_file)
