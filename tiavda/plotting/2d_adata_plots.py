import matplotlib.pyplot as plt

import tiavda.color.color_palette as cp


def _preflight_check(adata, coordinate_space):
    assert coordinate_space in adata.obsm_keys(), "Please choose from {}".format(adata.obsm_keys())


def plot_adata(adata):
    """
    :param adata: AnnData object.
    :return: Nothing.
    """

    _preflight_check(adata, 'X_emb')
    emb = adata.obsm['X_emb']
    df = adata.obs
    i = 0
    # TODO: Change vin_colors to my own color palette.
    colors = cp.rainbow_tiavda_colors()
    for state in df['state_info'].unique():
        print(state)
        cell_index = df.loc[df['state_info'] == state].index.astype(int)
        x_emb, y_emb = emb[cell_index][:, 0], emb[cell_index][:, 1]
        plt.scatter(x_emb, y_emb, c=colors[i], alpha=0.2)
        i += 1
        plt.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
        plt.box(False)
        # These lines hide the edges and ticks.


def plot_adata_subset(adata, states, color_theme, coordinate_space, alpha=0.2, xlabel="", ylabel="", title="",
                      show_edges=True):
    """
    Function for plotting a subset of cells from AnnData (adata).
    Parameters:
    -----------
    adata [required]
        AnnData object. Documentation: https://anndata.readthedocs.io/en/latest/
    states [required]
        String array of desired state_info in adata (e.g. Neutrophil, Monocyte, Baso)
    color_theme [required]
        The "theme" of colors on the graph (currently either "Rainbow" or "Cool", case-insensitive).
    coordinate_space [required]
        The choice of embedding. Should be found in adata.obsm_keys()
    xlabel
        The x-axis label, left blank by default.
    ylabel
        The y-axis label, left blank by default.
    title
        The title of the graph, left blank by default.
    show_edges
        Determines if the thin line "edges" around the graph are shown, true by default.
    """
    _preflight_check(adata, coordinate_space)
    emb = adata.obsm[coordinate_space]
    df = adata.obs

    #    if len(states) < len(colors):
    #        raise ValueError("The states and colors arrays must have the same number of elements!")
    #        return

    if color_theme.lower() == "rainbow":
        colors = cp.rainbow_tiavda_colors()
    elif color_theme.lower == "cool":
        colors = cp.cool_tiavda_colors()
    else:
        raise NameError("color_theme must be either 'Rainbow' or 'Cool' (case-insensitive)!")

    for state in states:
        cell_index = df.loc[df['state_info'] == state].index.astype(int)
        for subset_index in cell_index:
            # print("subset_index")
            for color in colors:
                # print("color")
                x_emb, y_emb = emb[subset_index]
                plt.scatter(x_emb, y_emb, c=color, alpha=alpha)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(title)
                if not show_edges:
                    plt.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
                    plt.box(False)
                # These lines hide the edges and ticks.
