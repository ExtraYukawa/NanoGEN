import os
import subprocess
from argparse import ArgumentParser

masses = []
rtt = 0.0000000
rtc = 0.0000000
rtu = 0.0000000
masses = [
  200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200
  , 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300
  , 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350, 350
  , 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400
  , 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500
  , 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600
  , 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700, 700
  , 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800
  , 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900
  , 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000
]

listrtt = [
  0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M200
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M300
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M350
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M400
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M500
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M600
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M700
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M800
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M900
  , 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 1.0, 1.0, 1.0, 1.0 #M1000
]

listrtc = [
  0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M200
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M300
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M350
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M400
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M500
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M600
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M700
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M800
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M900
  , 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0, 0.1, 0.4, 0.6, 1.0 #M1000
]

processes = ['bgth', 'cgbh']

def make_files(processes, masses, listrtt, listrtc):
  for process in processes:
    for (m, rtt, rtc) in zip(masses, listrtt, listrtc):
      rtt = str(rtt).replace('.', '')
      rtc = str(rtc).replace('.', '')
      if m < 700:
        gridp_path = f"/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/{process}/"
      else:
        gridp_path = f"/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc700/13TeV/madgraph/V5_2.6.5/{process}-new/"
      subprocess.run(["python", "make_files.py", "--gridpack", f"{gridp_path}{process}_H_M{m}_rhott{rtt}_rhotc{rtc}_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz"], cwd="Configuration/GenProduction/python/")

def make_cfg(processes, masses, listrtt, listrtc):
  for process in processes:
    for (m, rtt, rtc) in zip(masses, listrtt, listrtc):
      rtt = str(rtt).replace('.', '')
      rtc = str(rtc).replace('.', '')
      if m < 700:
        gridp_path = f"/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/{process}/"
      else:
        gridp_path = f"/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc700/13TeV/madgraph/V5_2.6.5/{process}-new/"
      cmsDriver_cmd = f"cmsDriver.py Configuration/GenProduction/python/{process}_H_M{m}_rhott{rtt}_rhotc{rtc}_rhotu00.py --python_filename {process}_H_M{m}_rhott{rtt}_rhotc{rtc}_rhotu00_cfg.py --eventcontent NANOAODGEN --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD --fileout file:{process}_H_M{m}_rhott{rtt}_rhotc{rtc}_rhotu00.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands \"process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(100)\"\\\\nprocess.source.numberEventsInLuminosityBlock=\"cms.untracked.uint32(303)\" --step LHE,GEN,NANOGEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 50000"
      os.system(cmsDriver_cmd)

def make_crab_files(processes, masses, listrtt, listrtc):
  for process in processes:
    for (m, rtt, rtc) in zip(masses, listrtt, listrtc):
      rtt = str(rtt).replace('.', '')
      rtc = str(rtc).replace('.', '')
      if m < 700:
        gridp_path = f"/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/{process}/"
      else:
        gridp_path = f"/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc700/13TeV/madgraph/V5_2.6.5/{process}-new/"
      subprocess.run(["python", "make_crab_files.py", "--gridpack", f"{gridp_path}{process}_H_M{m}_rhott{rtt}_rhotc{rtc}_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz"], cwd="crab_config")

def submit_crab(processes, masses, listrtt, listrtc):
  for process in processes:
    for (m, rtt, rtc) in zip(masses, listrtt, listrtc):
      rtt = str(rtt).replace('.', '')
      rtc = str(rtc).replace('.', '')
      os.system(f"crab submit -c crab_config/crabConfig_{process}_H_M{m}_rhott{rtt}_rhotc{rtc}_rhotu00.py")

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("--mkfiles", dest="mkfiles", default=False, action="store_true", help="Make files for gridpacks")
  parser.add_argument("--subcrab", dest="subcrab", default=False, action="store_true", help="Submit crab jobs")
  opts = parser.parse_args()

  if opts.mkfiles:
    make_files(processes, masses, listrtt, listrtc)
    make_crab_files(processes, masses, listrtt, listrtc)
    os.system("scram b") 
    make_cfg(processes, masses, listrtt, listrtc)

  if opts.subcrab:
    submit_crab(processes, masses, listrtt, listrtc)
