#! bin/bash
mkdir -p ../Configuration/GenProduction/python/
cp BHplus_example_fragment.py ../Configuration/GenProduction/python/
cp make_files.py ../Configuration/GenProduction/python/
mkdir ../crab_config 
cp make_crab_files.py ../crab_config/
cp crabConfig_cgbh_H_M400_rhott01_rhotc01_rhotu00.py ../crab_config/
cp produceNanoGEN.py ../
