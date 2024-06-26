# Takes a logic project, transposes everything, and bounces to MP3.
# python3 transpose.py <path_to_logic_project> <transpose_by> <output_name>
# Example: python3 transpose.py '/path/to/some\ project.logicx' 3 transposed_output


import sys
import time
import atomacos
import subprocess
import logic


def transpose(project, transpose_by, output_name):
    logic.open(project)
    logic.selectAllRegions()
    logic.transpose(transpose_by)
    logic.bounce(output_name)
    logic.close()


# If we run this script on the command line
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: transpose.py <path_to_logic_project> <transpose_by> <output_name>"
        )
        sys.exit(1)

    project = sys.argv[1]
    transpose_by = int(sys.argv[2])
    print(transpose_by)
    output_name = sys.argv[3]

    transpose(project, transpose_by, output_name)
