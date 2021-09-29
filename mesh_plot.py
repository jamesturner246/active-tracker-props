
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh

def main():
    #m = mesh.Mesh.from_file('screwdriver.stl')
    m = mesh.Mesh.from_file('screwdriver-decimated.stl')

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # ax.auto_scale_xyz(m.vectors[:, :, 0], m.vectors[:, :, 1], m.vectors[:, :, 2])

    # collection = mplot3d.art3d.Poly3DCollection(m.vectors)
    # ax.add_collection3d(collection)

    # screwdriver.stl marker coordinates
    x = [0.0,   0.0,   5.0,   -5.0  ]
    y = [78.0,  78.0,  120.0,  164.0]
    z = [13.5, -13.5,  0.0,    0.0  ]

    markers1 = np.array([
	[ 0.0,  78.0,   13.5 ], # handle_1
	[ 0.0,  78.0,  -13.5 ], # handle_2
	[ 5.0,  120.0,  0.0  ], # shaft_base
	[-5.0,  164.0,  0.0  ], # shaft_tip
    ])












    exit(0)


    ax.scatter(x, y, z, color='r')
    plt.show()


    # regression of orientation


    from sklearn.multioutput import MultiOutputRegressor
    from sklearn.linear_model import LinearRegression

    regressor = MultiOutputRegressor(LinearRegression())

    # x is vicon translation and rotation
    # y is dv pixel coordinates



    #regressor.fit()



    # given marker coordinates in vicon space, do regression to find matrix which transforms stl to correct
    # translation and orientation in numpy space (separate from calibration regression)




if __name__== '__main__':
    main()
