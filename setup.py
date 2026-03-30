from setuptools import find_pakages,setup
from typing import List
HYPEN_E_DOT = '-e.'
def  get_requirements(file_path:str)->List[str]:

    requirments=[]

    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments=[req.replace('\n',"")for req in requirments]
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments



setup(
    name = "mlprojrct",
    author ="shrihari",
    author_email="shriharikulkarni312003@gmail.com",
    packges=find_packages(),
    install_requirs=get_requirements('requirements.txt')
)