import json


def plotInit():
    try:
        with open("./settings/plots.json") as f:
            plot_recipe = json.load(f)
    except:
        plot_recipe = None
    return plot_recipe


def mqttInit(name) -> dict:
    try:
        with open(f"./settings/mqtt/{name}.json") as f:
            mqtt_recipe = json.load(f)
    except:
        mqtt_recipe = None
    return mqtt_recipe


def mqttSave(name, data:dict):
    with open(f"./settings/mqtt/{name}.json", "w") as f:
        json.dump(data, f)
