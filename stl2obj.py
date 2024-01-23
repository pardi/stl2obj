import numpy as np
from stl import mesh
from tqdm import tqdm

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

# Example usage
convert_stl_to_obj('input/base_link.stl', 'output/output.obj')