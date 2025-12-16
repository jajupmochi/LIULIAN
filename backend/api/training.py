from fastapi import APIRouter, HTTPException
from .plugin_manager import PluginManager

router = APIRouter()
plugin_manager = PluginManager()
plugin_manager.discover_plugins()

@router.post("/train/{plugin_name}")
async def train(plugin_name: str, data: dict, params: dict = {}):
    plugin = plugin_manager.get_plugin(plugin_name)
    if not plugin:
        raise HTTPException(status_code=404, detail="Plugin not found")
    result = plugin["model"].train(data, params)
    return {"status": "success", "result": result}
