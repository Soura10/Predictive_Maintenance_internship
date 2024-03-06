import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s:] %(message)s: ')

package_name="Turbofan_Jet_Engine"

list_of_files=[

    "github/workflow/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/utils.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    "setup.py",
    "app.py",
    "requirements.txt",
    "init_setup.sh",
    f"notebook/Trials.ipynb",
    f"notebook/EDA.ipynb"
     
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #create emty file
            logging.info(f"Creating file : {filepath}")

    else:
        logging.info(f"{filename} already existed")

