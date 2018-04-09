import pandas as pd


def to_excel(df,file_path):
    writer = pd.ExcelWriter(file_path+ ".xlsx", engine='xlsxwriter')
    df.to_excel(writer)
    writer.save()
