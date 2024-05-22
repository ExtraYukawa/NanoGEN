# NanoGEN

## login to lxplus8.cern.ch

## Release CMSSW
```
cmsrel CMSSW_12_4_12
cd CMSSW_12_4_12/src
cmsenv
scram b
```

## Get the repository and prepare setup
```
git clone git@github.com:ExtraYukawa/NanoGEN.git
cd NanoGEN
source setup.sh
```

## Run produceNanoGEN.py
```
cd $CMSSW_BASE/src
python produceNanoGEN.py --mkfiles
```
This command will produce all necessary configuration files to run both locally and on CRAB

## To run job locally
Use the command:
```cmsRun bgth(cgbh)_H_MX00_rhottX_rhotcX_rhotu00_cfg.py``` 

## To run on CRAB
```
cd $CMSSW_BASE/src
python produceNanoGEN.py --subcrab
```
This command will submit jobs for all the mass points and couplings given in the produceNanoGEN.py macro






