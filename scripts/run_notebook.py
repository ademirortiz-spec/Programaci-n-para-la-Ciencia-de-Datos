import nbformat, os, traceback
from nbconvert.preprocessors import ExecutePreprocessor

nb_path = os.path.join(os.getcwd(), "notebooks", "f3", "Notebook_F3_grupo9_POO.ipynb")
print('Executing:', nb_path)
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

try:
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(nb_path)}})
    with open(nb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print('EXECUTION_SUCCESS')
except Exception as e:
    print('EXECUTION_FAILED')
    traceback.print_exc()
    raise
