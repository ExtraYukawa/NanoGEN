import shutil, sys
from argparse import ArgumentParser

def copy_and_replace(template_path, destination_path, gridpack):
    # Copy the template file to the destination
    shutil.copyfile(template_path, destination_path)

    # Read the content of the template file
    with open(destination_path, 'r') as file:
        lines = file.readlines()

    # line no: 6
    line_number_to_replace = 6
    text_initials = opts.gridpack.split("/")[-1].split("_")[0:6] #cgbh_H_M400_rhott01_rhotc10_rhotu00
    replacement_text = "config.General.requestName = '"+'_'.join(text_initials)+"'"
    lines[line_number_to_replace - 1] = replacement_text + '\n'


    #config.JobType.psetName = 'cgbh_H_M400_rhott01_rhotc01_rhotu00_cfg.py'
    line_number_to_replace = 13
    text_initials = opts.gridpack.split("/")[-1].split("_")[0:6] #cgbh_H_M400_rhott01_rhotc10_rhotu00
    replacement_text = "config.JobType.psetName = '"+'_'.join(text_initials)+"_cfg.py'"
    lines[line_number_to_replace - 1] = replacement_text + '\n'
    
    # Specify the line number to replace (assuming line number 17 in this example)
    line_number_to_replace = 17
    replacement_text = "config.JobType.inputFiles = ['"+opts.gridpack+"']"
    # Replace the specified line with the replacement text
    lines[line_number_to_replace - 1] = replacement_text + '\n'

    #config.Data.outputPrimaryDataset = 'cgbh_H_M400_rhott01_rhotc01_rhotu00'
    line_number_to_replace = 20
    text_initials = opts.gridpack.split("/")[-1].split("_")[0:6] #cgbh_H_M400_rhott01_rhotc10_rhotu00
    replacement_text = "config.Data.outputPrimaryDataset = '"+'_'.join(text_initials)+"'"
    lines[line_number_to_replace - 1] = replacement_text + '\n'

    #config.Data.outputDatasetTag = 'cgbh_H_M400_rhott01_rhotc01_rhotu00'
    line_number_to_replace = 27
    text_initials = opts.gridpack.split("/")[-1].split("_")[0:6] #cgbh_H_M400_rhott01_rhotc10_rhotu00
    replacement_text = "config.Data.outputDatasetTag = '"+'_'.join(text_initials)+"'"
    lines[line_number_to_replace - 1] = replacement_text + '\n'
    
    # Write the modified content back to the destination file
    with open(destination_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    # Example usage    
    parser = ArgumentParser()
    parser.add_argument("--gridpack", dest="gridpack", default="/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/cgbh/cgbh_H_M400_rhott01_rhotc01_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz",
                        help="Gridpack for fragment creation [default: something]")
    template_file_path = "crabConfig_cgbh_H_M400_rhott01_rhotc01_rhotu00.py"
    opts = parser.parse_args()
    outstring = opts.gridpack.split("/")[-1].split("_")[0:6] #cgbh_H_M400_rhott01_rhotc10_rhotu00
    # print ("outstring: ", '_'.join(outstring)+'.py')
    #crabConfig_cgbh_H_M400_rhott01_rhotc01_rhotu00.py
    destination_file_path = 'crabConfig_'+'_'.join(outstring)+'.py'
    
    #check
    if template_file_path == destination_file_path:
        print ("copying template file, so ending here")
        sys.exit(1)

    copy_and_replace(template_file_path, destination_file_path, opts.gridpack)

    # print(f"File copied and line replaced. Destination: {destination_file_path}")
