
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh

def main():
    #m = mesh.Mesh.from_file('screwdriver.stl')
    m = mesh.Mesh.from_file('screwdriver-decimated.stl')

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.auto_scale_xyz(m.vectors[:, :, 0], m.vectors[:, :, 1], m.vectors[:, :, 2])

    collection = mplot3d.art3d.Poly3DCollection(m.vectors)
    ax.add_collection3d(collection)

    x = [0.0,   0.0,  5.0,   -5.0 ]
    y = [78.0,  78.0, 119.9, 163.9]
    z = [13.5, -13.5, 0.0,   0.0  ]
    ax.scatter(x, y, z, color='r')

    plt.show()


    # regression of orientation




    # WE HAVE 3D ORIENTATION/TRANSLATION FROM VICON

    # rotation / translation / scale matrices for numpy array




if __name__== '__main__':
    main()
