from datetime import datetime
from pathlib import Path

from hdx.location.country import Country

output = Path(__file__).parent / ".." / "mtoolbox" / "countries.py"

date = datetime.now().isoformat()
data = Country.countriesdata()

with output.open("w") as f:
    f.write(f"# Country list generated on {date} from OCHA-DAP/hdx-python-country")
    for key in ["countries", "iso2iso3"]:
        f.write(f"\n{key} = ")
        f.write(str(data[key]))
