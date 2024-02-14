# https://github.com/soumyadipbarman/NanoGEN/blob/5afcdf645feeb32f633eb870b4c9f9a876347956/crab_files/crabConfig_MC_generation_dyeej_2NLO3LO_5f_NLO_UNLOPS.py
from CRABClient.UserUtilities import config 
config = config()

config.section_("General")
config.General.requestName = 'cgbh_H_M400_rhott01_rhotc01_rhotu00'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'cgbh_H_M400_rhott01_rhotc01_rhotu00_cfg.py'
#config.JobType.scriptExe = 'heavygridpack_script.sh'  # For heavy tarball have to use script for coping tarball from T2 to worknode
#config.JobType.inputFiles = ['/afs/cern.ch/work/s/sobarman/private/MC@NLO/Gridpack/ttbar/date_07092020/ttbar_QCD_NLO_5f_MCNLO-delta_111_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz']
#config.JobType.inputFiles = ['/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttc/g2HDM_ttc_a0_M1000_rhotu00_rhotc01_rhott00_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz']
config.JobType.inputFiles = ['/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/cgbh/cgbh_H_M400_rhott01_rhotc01_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz']

config.section_("Data")
config.Data.outputPrimaryDataset = 'cgbh_H_M400_rhott01_rhotc01_rhotu00'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 20  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/phys_b2g/ExYukawa/bHplus/NanoGEN_2017/'
config.Data.publication = False
config.Data.outputDatasetTag = 'cgbh_H_M400_rhott01_rhotc01_rhotu00'

config.section_("Site")
#config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR','T2_DE_RWTH']
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = "T2_CH_CERN"
