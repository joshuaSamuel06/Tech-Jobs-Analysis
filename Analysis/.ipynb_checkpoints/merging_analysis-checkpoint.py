import nbformat

def merge_notebooks(notebook_files, output_file):
    merged_notebook = nbformat.v4.new_notebook()

    for notebook_file in notebook_files:
        with open(notebook_file, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
            merged_notebook.cells.extend(notebook.cells)

    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(merged_notebook, f)

# List of notebook files to merge
notebook_files = [
    'Analysis\Joshua\Data_Cleaning_and_Analysis\Data_Analysis\Analysis.ipynb',
    'Analysis\Mustafa-analysis\data_analysis.ipynb',
    'Analysis\Negin-Analysis\Data-Analysis\Visualize.ipynb'
]

# Output file name
output_file = 'Tech-Job-Analysis.ipynb'

# Merge the notebooks
merge_notebooks(notebook_files, output_file)
