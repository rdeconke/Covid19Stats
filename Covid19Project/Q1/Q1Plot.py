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
      print("Usage:", "Q1/Q1Plot.py Q1/<data file> Q1/<graphics file>")
      sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]

    try:
      csv_df = pd.read_csv(csv_filename,skiprows = 1)
    except IOError as err:
        print("Unable to open source file", csv_filename,": {}".format(err), file=sys.stderr)
        sys.exit(-1)
    # skip the first row since we read the title previously

    try:
        titleFile = open(csv_filename,"r",encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)
    graphtitle = titleFile.readline()

    fig = plt.figure()
    
    # This creates a barplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    
    g1 = sns.barplot(x = "Date",y = "Percentage",data = csv_df)
    g1.xaxis.set_major_locator(ticker.MaxNLocator(8))
    # choose the major 8 dates
    plt.xticks(rotation = 45, ha = 'right')
    # rotate to fit in graph
    g1.set(title = graphtitle)

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graphics_filename, bbox_inches="tight")

main(sys.argv)