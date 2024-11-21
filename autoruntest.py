import os
from pathlib import Path

#structure path
structures=os.listdir(r"C:\Users\folan\Research\Aryl Hydrocarbon\Structures\pdbqtbabel")

#main config file path string
config= r'--config "C:\Users\folan\Research\Aryl Hydrocarbon\Main\dockconftemplate.txt"'

for drug in structures:
    #define ligand path, may be redundant but eh it works
    ligand = "C:\\Users\\folan\\Research\\Aryl Hydrocarbon\\Structures\\pdbqtbabel\\" + str(drug)

    #designate output file with name of drug in pdbqt
    out = "C:\\Users\\folan\\Research\\Aryl Hydrocarbon\\Outputs\\Docking\\" + str(drug)

    #log only needs txt ext
    filename = Path(drug).stem
    log = "C:\\Users\\folan\\Research\\Aryl Hydrocarbon\\Outputs\\Logs\\" + str(filename)+ "log.txt"

    command= (config+
              " --ligand="+f'"{ligand}"'
              + " --out="+ f'"{out}"'
              + " --log="+ f'"{log}"')
    print(command)


    os.system("vina "+command)