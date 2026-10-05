import os, shutil, toml

path = "config.toml"
if not os.path.exists(path):
    shutil.copy("config.example.toml", path)
cfg = toml.load(path)
app = cfg.setdefault("app", {})
app["llm_provider"] = "deepseek"
if os.getenv("DEEPSEEK_API_KEY"):
    app["deepseek_api_key"] = os.environ["DEEPSEEK_API_KEY"]
if os.getenv("PIXABAY_API_KEY"):
    app["pixabay_api_keys"] = [os.environ["PIXABAY_API_KEY"]]
with open(path, "w") as f:
    toml.dump(cfg, f)
os.execvp("python", ["python", "main.py"])

