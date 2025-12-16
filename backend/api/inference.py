from fastapi import APIRouter, HTTPException
from .plugin_manager import PluginManager

router = APIRouter()
plugin_manager = PluginManager()
plugin_manager.discover_plugins()

@router.post("/predict/{plugin_name}")
async def predict(plugin_name: str, data: dict, params: dict = {}):
    plugin = plugin_manager.get_plugin(plugin_name)
    if not plugin:
        raise HTTPException(status_code=404, detail="Plugin not found")
    result = plugin["model"].predict(data, params)
    return {"status": "success", "result": result}

@router.get("/visualize/{plugin_name}")
async def visualize(plugin_name: str, results: dict):
    plugin = plugin_manager.get_plugin(plugin_name)
    if not plugin or not plugin["visualization"]:
        raise HTTPException(status_code=404, detail="Visualization not found")
    viz_data = plugin["visualization"].visualize(results)
    return {"status": "success", "visualization": viz_data}
