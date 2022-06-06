

def main_filter_data(df_all,rule_packet,set_params):
    filters = rule_packet.replace("df","df_all")
    df_set_params = df_all.loc[df_all[eval(filters)].index]
    df_set_params = df_set_params[set_params]
    return df_set_params