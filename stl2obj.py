import numpy as np
from stl import mesh
from tqdm import tqdm
import argparse
import os

def convert_stl_to_obj(stl_file, obj_file):
    # Read STL file
    stl_mesh = mesh.Mesh.from_file(stl_file)

    # Open OBJ file for writing
    with open(obj_file, 'w') as obj:
        # Write each vertex
        for v in np.unique(stl_mesh.vectors.reshape(-1, 3), axis=0):
            obj.write(f"v {v[0]} {v[1]} {v[2]}\n")

        # Write each face
        for _, f in tqdm(enumerate(stl_mesh.vectors), total=stl_mesh.vectors.shape[0]):
            # Find the index of each vertex in the unique list of vertices
            indices = [np.where((np.unique(stl_mesh.vectors.reshape(-1, 3), axis=0) == vertex).all(axis=1))[0][0] + 1 for vertex in f]
            obj.write(f"f {indices[0]} {indices[1]} {indices[2]}\n")

# # Example usage
# convert_stl_to_obj('input/base_link.stl', 'output/output.obj')

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Set the verbosity level", action="store_true")
    parser.add_argument("-i", "--input", help="Select the directory or file to convert", required=True)
    parser.add_argument("-o", "--output", help="Select the directory or file to save the output, default is: output/", default="output")
    args = parser.parse_args()
    
    abs_output_path = os.path.join(os.getcwd(), args.output)
    abs_input_path = os.path.join(os.getcwd(), args.input)
    
    # Create output folder
    if not os.path.isdir(abs_output_path):
        os.mkdir(abs_output_path)
    
    # Obtain the files
    stl_files = []

    if os.path.isdir(abs_input_path):
        for f in os.listdir(abs_input_path):
            if f.endswith('.stl'):
                stl_files.append(f)
    elif abs_input_path.endswith('.stl'):
        stl_files = [abs_input_path]
        
    if abs.verbose:
        print(f'{len(stl_files)} stl files found')
        
    for idx, stl_in in tqdm(enumerate(stl_files)):
        print(f'#{idx} file started')
        convert_stl_to_obj(os.path.join(abs_input_path, stl_in), os.path.join(abs_output_path, stl_in.removesuffix('.stl') + '.obj'))
