import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
df = pd.read_csv("kboo_pbcore_master.csv")

keep_cols = ["assetIdentifier", "physicalFormat", "generations", "durationPhysical", "originalCarrierLocation","date", "dateType","itemTitle", "intellectualAssetType"]

new_df = df[keep_cols]
new_df.rename(columns={'assetIdentifier': 'Unique Identifier', 'physicalFormat': 'Physical Format',
'DurationPhysical':"Duration","originalCarrierLocation":'Location', 'itemTitle':'Title','intellectualAssetType':'Title Type'}, inplace=True)
new_df["Identifier Source"] = "KBOO item label"
new_df["Media Type"] = "Sound"
new_df["Digital Format"] = "audio/x-wav"
new_df["Duration Approximate"] = "Yes"
new_df = new_df[['Unique Identifier', 'Identifier Source', 'Physical Format', 'Digital Format', 'Generations','Duration','Location','Date','Date Type','Title','Title Type']]

new_df.to_csv("aapb-test-data.csv", index=False)
