import importlib, pkgutil
import app.api as api_pkg

for importer, name, ispkg in pkgutil.iter_modules(api_pkg.__path__):
    mod = importlib.import_module("app.api." + name)
    router = getattr(mod, "router", None)
    if router:
        for r in router.routes:
            if hasattr(r, "path"):
                methods = list(r.methods) if r.methods else ["?"]
                print(methods[0] + " " + r.path)
