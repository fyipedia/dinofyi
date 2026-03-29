# dinofyi

[![PyPI version](https://agentgif.com/badge/pypi/dinofyi/version.svg)](https://pypi.org/project/dinofyi/)
[![Python](https://img.shields.io/pypi/pyversions/dinofyi)](https://pypi.org/project/dinofyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/dinofyi/)

Python API client for dinosaur paleontology and fossil record data. Access 6,142 dinosaur species across 15 geological periods, with taxonomic classification, fossil site locations in 198 countries, species comparison data, and paleontological glossary — all through a clean REST API with zero core dependencies.

Extracted from [DinoFYI](https://dinofyi.com/), a dinosaur encyclopedia platform cataloging every known dinosaur genus with classification, temporal range, geographic distribution, and discovery history based on the [Paleobiology Database](https://paleobiodb.org/) and peer-reviewed paleontological literature.

> **Explore dinosaur data at [dinofyi.com](https://dinofyi.com/)** — browse [dinosaurs](https://dinofyi.com/dinosaurs/), [periods](https://dinofyi.com/periods/), [classifications](https://dinofyi.com/classifications/), [fossil sites](https://dinofyi.com/sites/), and [countries](https://dinofyi.com/countries/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/dinofyi/main/demo.gif" alt="dinofyi demo — dinosaur species lookup, geological period browsing, and paleontology search in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Dinosaur Classification](#dinosaur-classification)
  - [Geological Time Scale](#geological-time-scale)
  - [Fossil Sites and Discovery](#fossil-sites-and-discovery)
  - [Geographic Distribution](#geographic-distribution)
  - [Species Comparison](#species-comparison)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Dinosaurs](#learn-more-about-dinosaurs)
- [Nature FYI Family](#nature-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install dinofyi                # Core (zero deps)
pip install "dinofyi[cli]"         # + Command-line interface (typer, rich)
pip install "dinofyi[mcp]"         # + MCP server for AI assistants
pip install "dinofyi[api]"         # + HTTP client for dinofyi.com API
pip install "dinofyi[all]"         # Everything
```

Or run instantly without installing:

```bash
uvx --from dinofyi dinofyi search "tyrannosaurus"
```

## Quick Start

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    # Search across all dinosaur species
    results = api.search("velociraptor")
    print(results)

    # Get detailed information for a specific dinosaur
    dino = api.get_dinosaur("tyrannosaurus-rex")
    print(dino["name"])  # Tyrannosaurus rex

    # Browse geological periods — 15 periods of the Mesozoic
    periods = api.list_periods()
    print(periods["count"])  # 15

    # Explore fossil sites across 198 countries
    sites = api.list_sites()
    print(sites["count"])
```

## What You Can Do

### Dinosaur Classification

Dinosaurs are classified within the clade **Dinosauria**, first defined by Richard Owen in 1842. The fundamental split separates dinosaurs into two major orders based on hip structure — a distinction proposed by Harry Seeley in 1888 that remains central to dinosaur taxonomy today.

| Order | Hip Structure | Major Groups | Examples |
|-------|--------------|-------------|---------|
| **Saurischia** (lizard-hipped) | Pubis points forward | Theropoda, Sauropodomorpha | *T. rex*, *Brachiosaurus*, *Velociraptor* |
| **Ornithischia** (bird-hipped) | Pubis points backward | Thyreophora, Ornithopoda, Marginocephalia | *Stegosaurus*, *Triceratops*, *Iguanodon* |

Within these two orders, dinosaurs diversify into numerous families and clades:

| Clade | Description | Notable Members |
|-------|-------------|-----------------|
| **Theropoda** | Bipedal carnivores (ancestors of birds) | *Tyrannosaurus*, *Allosaurus*, *Spinosaurus* |
| **Sauropodomorpha** | Long-necked herbivores, largest land animals | *Brachiosaurus*, *Diplodocus*, *Argentinosaurus* |
| **Thyreophora** | Armored dinosaurs | *Stegosaurus*, *Ankylosaurus* |
| **Ornithopoda** | Beaked herbivores, often bipedal | *Iguanodon*, *Parasaurolophus* |
| **Marginocephalia** | Horned and dome-headed dinosaurs | *Triceratops*, *Pachycephalosaurus* |

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    # Browse dinosaur classifications
    classifications = api.list_classifications()
    for cls in classifications["results"][:5]:
        print(f"{cls['name']}")

    # Get details for a specific classification
    theropod = api.get_classification("theropoda")
    print(theropod["name"])  # Theropoda
```

Learn more: [Dinosaur Encyclopedia](https://dinofyi.com/dinosaurs/) · [Classifications](https://dinofyi.com/classifications/) · [Paleontology Glossary](https://dinofyi.com/glossary/)

### Geological Time Scale

Dinosaurs dominated Earth for approximately 165 million years during the **Mesozoic Era** (252-66 Ma), which is divided into three periods: Triassic, Jurassic, and Cretaceous. Each period saw different dinosaur faunas, climate conditions, and continental configurations.

| Period | Time (Ma) | Climate | Dominant Dinosaurs |
|--------|-----------|---------|-------------------|
| **Late Triassic** | 237-201 | Hot, arid interior | Early theropods (*Coelophysis*), prosauropods |
| **Early Jurassic** | 201-174 | Warming, humid | Dilophosaurus, early sauropods |
| **Middle Jurassic** | 174-163 | Warm, tropical | *Megalosaurus*, early stegosaurs |
| **Late Jurassic** | 163-145 | Warm, seasonal | *Allosaurus*, *Stegosaurus*, *Diplodocus* |
| **Early Cretaceous** | 145-100 | Cooling then warming | *Iguanodon*, *Spinosaurus*, flowering plants emerge |
| **Late Cretaceous** | 100-66 | Warm, high sea levels | *T. rex*, *Triceratops*, *Velociraptor* |

The Mesozoic ended with the **Cretaceous-Paleogene extinction event** (66 Ma), caused by an asteroid impact at Chicxulub, Mexico, wiping out all non-avian dinosaurs.

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    # Browse all 15 geological periods
    periods = api.list_periods()
    for p in periods["results"][:5]:
        print(f"{p['name']}")

    # Get details for a specific period
    cretaceous = api.get_period("late-cretaceous")
    print(cretaceous["name"])  # Late Cretaceous
```

Learn more: [Geological Periods](https://dinofyi.com/periods/) · [Guides](https://dinofyi.com/guides/)

### Fossil Sites and Discovery

Dinosaur fossils have been discovered on every continent, including Antarctica. The history of paleontological discovery spans from the first scientific description of *Megalosaurus* by William Buckland in 1824 to modern CT-scanning and molecular analysis techniques. DinoFYI catalogs fossil sites with their geographic coordinates, geological formation, and associated species.

| Formation | Location | Notable Finds |
|-----------|----------|--------------|
| **Hell Creek** | Montana, USA | *T. rex*, *Triceratops*, *Edmontosaurus* |
| **Morrison** | Western USA | *Allosaurus*, *Diplodocus*, *Stegosaurus* |
| **Ischigualasto** | Argentina | *Eoraptor*, *Herrerasaurus* (oldest dinosaurs) |
| **Djadochta** | Mongolia | *Velociraptor*, *Protoceratops*, *Oviraptor* |
| **Solnhofen** | Germany | *Archaeopteryx* (earliest known bird) |
| **Yixian** | China | Feathered dinosaurs (*Sinosauropteryx*, *Microraptor*) |

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    # Browse fossil sites worldwide
    sites = api.list_sites()
    for s in sites["results"][:5]:
        print(s["name"])

    # Get details for a specific fossil site
    site = api.get_site("hell-creek-formation")
    print(site["name"])  # Hell Creek Formation
```

Learn more: [Fossil Sites](https://dinofyi.com/sites/) · [Glossary](https://dinofyi.com/glossary/)

### Geographic Distribution

Dinosaur fossils have been found in 198 countries, reflecting the changing geography of Earth during the Mesozoic. Pangaea was breaking apart throughout the age of dinosaurs — Laurasia (north) and Gondwana (south) separated in the Jurassic, leading to increasing endemism in the Cretaceous.

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    # Browse countries with dinosaur fossil discoveries
    countries = api.list_countries()
    print(countries["count"])  # 198 countries

    # Get fossil data for a specific country
    mongolia = api.get_country("mongolia")
    print(mongolia["name"])  # Mongolia — rich Cretaceous fossil beds
```

Learn more: [Countries](https://dinofyi.com/countries/) · [Guides](https://dinofyi.com/guides/)

### Species Comparison

DinoFYI provides detailed comparisons between similar or frequently confused dinosaur species, covering size, diet, temporal range, geographic overlap, and distinguishing features.

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    # Browse dinosaur comparisons
    comparisons = api.list_comparisons()
    for comp in comparisons["results"][:3]:
        print(comp["name"])

    # Compare two specific dinosaurs
    comp = api.get_comparison("t-rex-vs-spinosaurus")
    print(comp["name"])  # T. rex vs Spinosaurus
```

Learn more: [Dinosaur Comparisons](https://dinofyi.com/glossary/) · [Guides](https://dinofyi.com/guides/)

## Command-Line Interface

```bash
pip install "dinofyi[cli]"

dinofyi search "stegosaurus"     # Search across all dinosaur species
```

## MCP Server (Claude, Cursor, Windsurf)

Add dinosaur data to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "dinofyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "dinofyi": {
            "command": "uvx",
            "args": ["--from", "dinofyi[mcp]", "python", "-m", "dinofyi.mcp_server"]
        }
    }
}
```

## REST API Client

```python
from dinofyi.api import DinoFYI

with DinoFYI() as api:
    dinos = api.list_dinosaurs()          # Browse all 6,142 dinosaurs
    periods = api.list_periods()          # Browse 15 geological periods
    sites = api.list_sites()              # Browse fossil sites
    results = api.search("raptor")        # Full-text search
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/dinosaurs/` | List all dinosaurs |
| GET | `/api/v1/dinosaurs/{slug}/` | Dinosaur detail |
| GET | `/api/v1/periods/` | List geological periods |
| GET | `/api/v1/periods/{slug}/` | Period detail |
| GET | `/api/v1/classifications/` | List classifications |
| GET | `/api/v1/classifications/{slug}/` | Classification detail |
| GET | `/api/v1/sites/` | List fossil sites |
| GET | `/api/v1/sites/{slug}/` | Site detail |
| GET | `/api/v1/countries/` | List countries |
| GET | `/api/v1/comparisons/` | List comparisons |
| GET | `/api/v1/glossary/` | List glossary terms |
| GET | `/api/v1/guides/` | List guides |
| GET | `/api/v1/search/?q={query}` | Search across all content |

```bash
curl -s "https://dinofyi.com/api/v1/dinosaurs/?limit=3"
```

Full API documentation at [dinofyi.com/developers/](https://dinofyi.com/developers/).
OpenAPI 3.1.0 spec: [dinofyi.com/api/openapi.json](https://dinofyi.com/api/openapi.json).

## API Reference

| Function | Description |
|----------|-------------|
| `DinoFYI()` | Create API client (`base_url`, `timeout`) |
| `list_dinosaurs(**params)` | List all dinosaur species |
| `get_dinosaur(slug)` | Get dinosaur detail |
| `list_periods(**params)` | List geological periods |
| `get_period(slug)` | Get period detail |
| `list_classifications(**params)` | List classifications |
| `get_classification(slug)` | Get classification detail |
| `list_sites(**params)` | List fossil sites |
| `get_site(slug)` | Get site detail |
| `list_countries(**params)` | List countries |
| `list_comparisons(**params)` | List comparisons |
| `list_glossary(**params)` | List glossary terms |
| `list_guides(**params)` | List guides |
| `search(query)` | Search across all content |

## Learn More About Dinosaurs

- **Browse**: [Dinosaur Encyclopedia](https://dinofyi.com/dinosaurs/) · [Classifications](https://dinofyi.com/classifications/) · [Geological Periods](https://dinofyi.com/periods/)
- **Reference**: [Fossil Sites](https://dinofyi.com/sites/) · [Countries](https://dinofyi.com/countries/)
- **Guides**: [Glossary](https://dinofyi.com/glossary/) · [Guides](https://dinofyi.com/guides/)
- **API**: [REST API Docs](https://dinofyi.com/developers/) · [OpenAPI Spec](https://dinofyi.com/api/openapi.json)

## Nature FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — living organisms, wildlife, and natural history.

| Package | PyPI | Description |
|---------|------|-------------|
| speciesfyi | [PyPI](https://pypi.org/project/speciesfyi/) | 49,112 species, 17,982 taxa, 846 ecoregions — [speciesfyi.com](https://speciesfyi.com/) |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | 11,251 birds, 40 orders, 258 families — [birdfyi.com](https://birdfyi.com/) |
| fishfyi | [PyPI](https://pypi.org/project/fishfyi/) | 78 fish species, 48 orders, 188 families — [fishfyi.com](https://fishfyi.com/) |
| plantfyi | [PyPI](https://pypi.org/project/plantfyi/) | 379,774 plants, 734 families, 50 orders — [plantfyi.com](https://plantfyi.com/) |
| **dinofyi** | [PyPI](https://pypi.org/project/dinofyi/) | **6,142 dinosaurs, 15 periods, 198 countries — [dinofyi.com](https://dinofyi.com/)** |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies — [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis — [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats — [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings — [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS — [fontfyi.com](https://fontfyi.com/) |
| **dinofyi** | [PyPI](https://pypi.org/project/dinofyi/) | — | Dinosaur paleontology & fossil record — [dinofyi.com](https://dinofyi.com/) |
| speciesfyi | [PyPI](https://pypi.org/project/speciesfyi/) | — | Species taxonomy & biodiversity — [speciesfyi.com](https://speciesfyi.com/) |
| birdfyi | [PyPI](https://pypi.org/project/birdfyi/) | — | Bird species encyclopedia — [birdfyi.com](https://birdfyi.com/) |
| fishfyi | [PyPI](https://pypi.org/project/fishfyi/) | — | Fish species & marine biology — [fishfyi.com](https://fishfyi.com/) |
| plantfyi | [PyPI](https://pypi.org/project/plantfyi/) | — | Plant taxonomy & cultivation — [plantfyi.com](https://plantfyi.com/) |

## Embed Widget

Embed [DinoFYI](https://dinofyi.com) widgets on any website with [dinofyi-embed](https://widget.dinofyi.com):

```html
<script src="https://cdn.jsdelivr.net/npm/dinofyi-embed@1/dist/embed.min.js"></script>
<div data-dinofyi="entity" data-slug="example"></div>
```

Zero dependencies · Shadow DOM · 4 themes (light/dark/sepia/auto) · [Widget docs](https://widget.dinofyi.com)

## License

MIT
