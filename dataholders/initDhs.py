from dataholders.DataHolder import DataHolder


def build_dataholders(recipt:dict):
    dataholders = {}
    for rec in recipt["plotting"]:
        if rec["subtopic"] not in dataholders.keys():
            dataholders[rec["subtopic"]] = {}
        dataholders[rec["subtopic"]][rec["name"]] = DataHolder(rec["sample_num"])
    return dataholders
