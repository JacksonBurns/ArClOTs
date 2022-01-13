import matplotlib.pyplot as plt

def prediction_error_plot(actual, predicted, title=None):
#     actual = 2.718**actual
#     predicted = 2.718**predicted
    fig, ax = plt.subplots(figsize=(6,6))
    ax.scatter(actual, predicted, edgecolors=(0, 0, 0))
    ax.plot([actual.min(), actual.max()], [actual.min(), actual.max()], "k--", lw=4)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    if title:
        plt.title(title)
    plt.show()