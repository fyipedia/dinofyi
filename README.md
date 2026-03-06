# dinofyi

Dinosaur paleontology encyclopedia API client — [dinofyi.com](https://dinofyi.com)

## Install

```bash
pip install dinofyi
```

## Quick Start

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    results = api.search("tyrannosaurus")
    print(results)
```

## License

MIT
