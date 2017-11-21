def render(table, params):
    buf = StringIO()
    table.info(buf=buf)
    s = buf.getvalue()
    info_values = [re.split("\\s\\s+",x) for x in s.split("\n")]
    info_values = [x for x in info_values if len(x)>1]
    metadata_df = pd.DataFrame(info_values)
    metadata_df.columns = ["Column_Name","Column_Info"]
    
    ## Column Info Split
    metadata_df['Non_Null_Count'], metadata_df['Object_Type'] = metadata_df['Column_Info'].str.split(' ', 1).str
    metadata_df["Object_Type"] = metadata_df["Object_Type"].str.replace("non-null ","")
    
    ## unique counts for each variable
    uniques_df = table.apply(lambda x: len(x.unique())).reset_index()
    uniques_df.columns = ["Column_Name","Unique_Count"]
    metadata_df["Unique_Count"] = uniques_df["Unique_Count"]
    metadata_df = metadata_df[["Column_Name","Non_Null_Count","Unique_Count","Object_Type"]]
    return metadata_df
