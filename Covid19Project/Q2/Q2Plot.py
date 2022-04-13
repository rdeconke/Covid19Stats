import sys
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

def main(argv):

    '''
    Create a plot using ranks
    '''

    #
    #   Check that we have been given the right number of parameters,
    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #

    if len(argv) != 3:
        print("Usage:","Q2/Q2Plot.py Q2/<data file> Q2/<graphics file>")
        sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]

    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    #
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename, ": {}".format(err), file=sys.stderr)
        sys.exit(-1)

    fig = plt.figure()

    # This creates a barplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    
    g1 = sns.barplot(x = "Public Health Unit",y = "Number of cases", hue = "Type", data = csv_df)

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graphics_filename, bbox_inches="tight")

main(sys.argv)