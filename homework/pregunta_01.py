# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    def create_docs():
        if os.path.exists("./docs"):
            os.system("rm -r ./docs")
        os.makedirs("./docs")

    def save_plt(name):
        os.makedirs(os.path.dirname(f"docs/{name}"), exist_ok=True)
        plt.savefig(f"docs/{name}")

    # Leer la data
    df = pd.read_csv("./files/input/shipping-data.csv")

    def create_visual_shipping_per_warehouse(df):
        df = df.copy()
        plt.figure()
        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        save_plt("shipping_per_warehouse.png")

    def create_visual_mode_of_shipment(df):
        df = df.copy()
        plt.figure()
        counts = df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title="Mode of Shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )
        save_plt("mode_of_shipment.png")

    def create_visual_for_average_customer_rating(df):
        df = df.copy()
        plt.figure()
        df = (
            df[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        df.columns = df.columns.droplevel()
        df = df[["mean", "min", "max"]]
        plt.barh(
            y=df.index.values,
            width=df["max"].values - 1,
            left=df["min"].values,
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colors = [
            "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
        ]
        plt.barh(
            y=df.index.values,
            width=df["mean"].values - 1,
            left=df["min"].values,
            color=colors,
            height=0.5,
            alpha=1.0,
        )
        plt.title("Average Customer Rating")
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        save_plt("average_customer_rating.png")

    def create_visual_for_weight_distribution(df):
        df = df.copy()
        plt.figure()
        df.Weight_in_gms.plot.hist(
            title="Shipped Weight Distribution", color="tab:orange", edgecolor="white"
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        save_plt("weight_distribution")

    def index():
        contenido_html = """<!DOCTYPE html>
        <html>
            <body>
                <h1>Shipping dashboard Example</h1>
                <div style='width: 45%; float: left;'>
                    <img src='docs/shipping_per_warehouse.png' alt='Fig1'>
                    <img src='docs/mode_of_shipment.png' alt='Fig2'>
                </div>
                <div style='width: 45%; float: right;'>
                    <img src='docs/average_customer_rating.png' alt='Fig3'>
                    <img src='docs/weight_distribution.png' alt='Fig4'>
                </div>
            </body>
        </html>"""
        with open("docs/index.html", "w") as archivo:
            archivo.write(contenido_html)

    create_docs()
    create_visual_shipping_per_warehouse(df)
    create_visual_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)
    index()


pregunta_01()
