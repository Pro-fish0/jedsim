#!/bin/bash

# Create directory structure
mkdir -p src/{data,models,simulation,analysis,visualization} tests/{test_data,test_models,test_simulation,test_analysis} data/{raw,processed} notebooks results/{figures,reports} configs logs

# Create __init__.py files
touch src/__init__.py
touch src/{data,models,simulation,analysis,visualization}/__init__.py
touch tests/__init__.py

# Create main Python files
touch src/main.py
touch src/data/{loaders.py,preprocessors.py}
touch src/models/{grid.py,ambulance.py,hospital.py}
touch src/simulation/{engine.py,events.py}
touch src/analysis/{response_time.py,optimization.py}
touch src/visualization/mapplot.py

# Create other necessary files
touch requirements.txt setup.py README.md .gitignore
touch configs/simulation_params.yaml
touch notebooks/exploratory_analysis.ipynb

echo "Project structure created successfully!"