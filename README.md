# NanoGEN

## login to lxplus8.cern.ch

## Release CMSSW
```
cmsrel CMSSW_12_4_8
cd CMSSW_12_4_8/src
cmsenv
```

## Put the example configuration (from mcm, but thanks to Efe for providing this)
```
mkdir -p Configuration/GenProduction/python/BHplus_example_fragment.py
cp BHplus_example_fragment.py Configuration/GenProduction/python/
cp 
```

## Run cmsDriver commands
```
cmsDriver.py Configuration/GenProduction/python/cgbh_H_M400_rhott10_rhotc01_rhotu00.py --python_filename cgbh_H_M400_rhott10_rhotc01_rhotu00_cfg.py --eventcontent NANOAODGEN --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD --fileout file:cgbh_H_M400_rhott10_rhotc01_rhotu00.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(100)"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(303)" --step LHE,GEN,NANOGEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 100
```
It will create a cfg file, which will run as ``cmsRun`` 
PS: forgot where the script for different configuration maker

## TO run on CRAB
```
mkdir crab_config 
cp make_crab_files.py crab_config/
cp crabConfig_cgbh_H_M400_rhott01_rhotc01_rhotu00.py crab_config/
cd crab_config
python make_crab_files.py --gridpack "/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/cgbh/cgbh_H_M400_rhott01_rhotc01_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz"
```
Run with other ``gridapacks`` to make different configuration

## Submit on crab
```
cd $CMSSW_BASE/src
crab submit -c crab_config/crabConfig_cgbh_H_M400_rhott01_rhotc01_rhotu00.py
```
and so others





