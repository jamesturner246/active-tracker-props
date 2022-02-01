
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import json
import stl
from sklearn.decomposition import PCA


def main():
    prop = 'jpt_mallet'
    #prop = 'jpt_screwdriver'
    #prop = 'kth_hammer'
    #prop = 'kth_screwdriver'
    #prop = 'kth_spanner'

    # load initial
    with open(f'./{prop}/{prop}_markers.json', 'r') as f:
        markers1 = json.load(f)
        markers2 = markers1.copy()
    mesh = stl.Mesh.from_file(f'./{prop}/{prop}_decimated.stl')
    np_mesh1 = mesh.vectors.copy()
    np_mesh2 = np_mesh1.copy()

    # PCA of mesh and markers
    pca = PCA()
    np_mesh2 = np_mesh2.reshape(-1, 3)
    np_mesh2 = pca.fit_transform(np_mesh2)
    np_mesh2 = np_mesh2.reshape(-1, 3, 3)
    for marker_name in markers1.keys():
        new_marker = np.array([markers1[marker_name]])
        new_marker = pca.transform(new_marker)
        markers2[marker_name] = new_marker[0].tolist()

    # centre on markers midpoint (Vicon root segment)
    np_markers2 = np.array([m for m in markers2.values()])
    np_markers2_mid = np_markers2.mean(0)
    np_mesh2 -= np_markers2_mid
    for marker_name in markers2.keys():
        new_marker = markers2[marker_name]
        new_marker -= np_markers2_mid
        markers2[marker_name] = new_marker.tolist()

    # save final
    mesh.vectors[:] = np_mesh2
    mesh.save(f'./{prop}/{prop}_mesh_final.stl')
    with open(f'./{prop}/{prop}_markers_final.json', 'w') as f:
        json.dump(markers2, f)

    # plot
    fig = plt.figure()
    np_markers1 = np.array([m for m in markers1.values()])
    np_markers2 = np.array([m for m in markers2.values()])
    collection1 = mplot3d.art3d.Poly3DCollection(np_mesh1, facecolors='red')
    collection2 = mplot3d.art3d.Poly3DCollection(np_mesh2, facecolors='green')

    # ax = fig.add_subplot(projection='3d')
    # ax.add_collection3d(collection1)
    # ax.scatter(np_markers1[:, 0], np_markers1[:, 1], np_markers1[:, 2], color='blue')
    # ax.add_collection3d(collection2)
    # ax.scatter(np_markers2[:, 0], np_markers2[:, 1], np_markers2[:, 2], color='gold')
    # ax.set_xlim([-150, 150])
    # ax.set_ylim([-150, 150])
    # ax.set_zlim([-150, 150])
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('z')

    ax1 = fig.add_subplot(121, projection='3d')
    ax1.add_collection3d(collection1)
    ax1.scatter(np_markers1[:, 0], np_markers1[:, 1], np_markers1[:, 2], color='blue')
    ax1.set_xlim([-150, 150])
    ax1.set_ylim([-150, 150])
    ax1.set_zlim([-150, 150])
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')

    ax2 = fig.add_subplot(122, projection='3d')
    ax2.add_collection3d(collection2)
    ax2.scatter(np_markers2[:, 0], np_markers2[:, 1], np_markers2[:, 2], color='gold')
    ax2.set_xlim([-150, 150])
    ax2.set_ylim([-150, 150])
    ax2.set_zlim([-150, 150])
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('z')

    plt.show()


if __name__ == '__main__':
    main()
