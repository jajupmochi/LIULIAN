import importlib.util
import json
from pathlib import Path

PLUGIN_DIR = Path(__file__).parent.parent.parent / "plugins"

class PluginManager:
    def __init__(self):
        self.plugins = {}  # plugin_name -> module dict

    def discover_plugins(self):
        self.plugins = {}
        for plugin_path in PLUGIN_DIR.iterdir():
            if plugin_path.is_dir():
                meta_file = plugin_path / "metadata.json"
                model_file = plugin_path / "model.py"
                vis_file = plugin_path / "visualization.py"
                if meta_file.exists() and model_file.exists():
                    with open(meta_file) as f:
                        metadata = json.load(f)
                    self.plugins[metadata["name"]] = {
                        "path": plugin_path,
                        "metadata": metadata,
                        "model": self.load_module(model_file, f"{metadata['name']}_model"),
                        "visualization": self.load_module(vis_file, f"{metadata['name']}_vis") if vis_file.exists() else None
                    }

    def load_module(self, path, module_name):
        spec = importlib.util.spec_from_file_location(module_name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def get_plugin_names(self):
        return list(self.plugins.keys())

    def get_plugin(self, name):
        return self.plugins.get(name, None)
