from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(df,
                  title=f"{x} and {y} searching for {target}",
                  ).mark_circle(size=75).encode(x=x,
                                                y=y,
                                                color=target,
                                                tooltip=Tooltip(df.columns.to_list())
                                                )
    return graph
