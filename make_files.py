import shutil
from argparse import ArgumentParser

def copy_and_replace(template_path, destination_path, replacement_text):
    # Copy the template file to the destination
    shutil.copyfile(template_path, destination_path)

    # Read the content of the template file
    with open(destination_path, 'r') as file:
        lines = file.readlines()

    # Specify the line number to replace (assuming line number 7 in this example)
    line_number_to_replace = 7

    # Replace the specified line with the replacement text
    lines[line_number_to_replace - 1] = replacement_text + '\n'

    # Write the modified content back to the destination file
    with open(destination_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    # Example usage    
    parser = ArgumentParser()
    parser.add_argument("--gridpack", dest="gridpack", default="/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/cgbh/cgbh_H_M400_rhott01_rhotc01_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz",
                        help="Gridpack for fragment creation [default: something]")
    template_file_path = "BHplus_example_fragment.py"
    opts = parser.parse_args()
    outstring = opts.gridpack.split("/")[-1].split("_")[0:6]
    # print ("outstring: ", '_'.join(outstring)+'.py')
    destination_file_path = '_'.join(outstring)+'.py' #"BHplus_example_fragment_one.py"
    # gripack = "/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/cgbh/cgbh_H_M400_rhott01_rhotc01_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz"
    replacement_string = "args = cms.vstring('"+opts.gridpack.replace("\"", "") + "'),"
    print ("replacement_string: ", replacement_string)

    copy_and_replace(template_file_path, destination_file_path, replacement_string)

    # print(f"File copied and line replaced. Destination: {destination_file_path}")
