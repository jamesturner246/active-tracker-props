
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import json
from stl import Mesh
from sklearn.decomposition import PCA


def main():
    #prop = 'jpt_mallet'
    prop = 'jpt_screwdriver'
    #prop = 'kth_hammer'
    #prop = 'kth_screwdriver'
    #prop = 'kth_spanner'

    # load initial
    with open(f'./{prop}/{prop}_markers.json', 'r') as f:
        markers1 = json.load(f)
        markers1 = np.array([v for v in markers1.values()])
    mesh1 = Mesh.from_file(f'./{prop}/{prop}_decimated.stl').vectors

    # PCA of mesh and markers
    pca = PCA()
    mesh2 = mesh1.reshape(-1, 3)
    mesh2 = pca.fit_transform(mesh2)
    mesh2_min = mesh2.min(0)
    mesh2_max = mesh2.max(0)
    mesh2_mid = mesh2_min / 2 + mesh2_max / 2
    mesh2 -= mesh2_mid
    mesh2 = mesh2.reshape(-1, 3, 3)
    markers2 = pca.transform(markers1)
    markers2 -= mesh2_mid

    collection1 = mplot3d.art3d.Poly3DCollection(mesh1, facecolors='red')
    collection2 = mplot3d.art3d.Poly3DCollection(mesh2, facecolors='green')

    # save final
    with open(f'./{prop}/{prop}_markers_final.json', 'w') as f:
        json.dump(markers2, f)
    mesh2.save(f'./{prop}/{prop}_final.stl')

    # plot
    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    ax.add_collection3d(collection1)
    ax.scatter(markers1[:, 0], markers1[:, 1], markers1[:, 2], color='blue')
    ax.add_collection3d(collection2)
    ax.scatter(markers2[:, 0], markers2[:, 1], markers2[:, 2], color='gold')
    ax.set_xlim([-150, 150])
    ax.set_ylim([-150, 150])
    ax.set_zlim([-150, 150])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # ax1 = fig.add_subplot(121, projection='3d')
    # ax1.add_collection3d(collection1)
    # ax1.scatter(markers1[:, 0], markers1[:, 1], markers1[:, 2], color='blue')
    # ax1.set_xlim([-150, 150])
    # ax1.set_ylim([-150, 150])
    # ax1.set_zlim([-150, 150])
    # ax1.set_xlabel('x')
    # ax1.set_ylabel('y')
    # ax1.set_zlabel('z')

    # ax2 = fig.add_subplot(122, projection='3d')
    # ax2.add_collection3d(collection2)
    # ax2.scatter(markers2[:, 0], markers2[:, 1], markers2[:, 2], color='gold')
    # ax2.set_xlim([-150, 150])
    # ax2.set_ylim([-150, 150])
    # ax2.set_zlim([-150, 150])
    # ax2.set_xlabel('x')
    # ax2.set_ylabel('y')
    # ax2.set_zlabel('z')


    plt.show()


if __name__ == '__main__':
    main()
