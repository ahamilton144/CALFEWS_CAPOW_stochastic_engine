import pandas as pd
import numpy as np

samples = []
total_flow = []
for s in range(101):
  try:
    df = pd.read_csv('Synthetic_streamflows/output/ORCA_forecast_flows' + str(s) + '.csv')
    cols = [c for c in df.columns if ('fnf' in c.split('_')) and ('MIL' in c.split('_') or 'KWH' in c.split('_') or 'SUC' in c.split('_') or 'PFT' in c.split('_') or 'ISB' in c.split('_'))]
    flow = df.loc[:, cols].sum().sum()
    samples.append(s)
    total_flow.append(flow)
  except:
    pass
flow_df = pd.DataFrame({'sample': samples, 'flow': total_flow})
flow_df.sort_values('flow', inplace=True)
flow_df.reset_index(drop=True, inplace=True)
flow_df.to_csv('Synthetic_streamflows/output/TLB_fnf_sort.csv')
