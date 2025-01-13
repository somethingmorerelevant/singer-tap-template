"""tap-name discover module."""
from typing import Dict, Optional
import json
from singer.catalog import Catalog
from tap_name.client import Client
from tap_name.helpers import get_abs_path
from tap_name.streams import STREAMS


def discover(config: Optional[Dict] = None):
    """
    Performs discovery for the given tap by collecting metadata and schema information for all streams.
    """
    # Authenticate the client if a configuration is provided
    if config:
        try:
            client = Client(config)
            client.authenticate()
        except Exception as e:
            raise RuntimeError(f"Authentication failed: {e}")
    streams = []

    # Iterate through the streams to build their metadata and schema
    for stream_name, stream in STREAMS.items():
        try:
            # Resolve the schema file path
            schema_path = get_abs_path(f"schemas/{stream_name}.json")
            
            # Load the schema from the JSON file
            with open(schema_path, encoding="utf-8") as schema_file:
                schema = json.load(schema_file)

            # Append stream details to the streams list
            streams.append({
                "stream": stream_name,
                "tap_stream_id": stream.tap_stream_id,
                "schema": schema,
                "metadata": stream.get_metadata(schema),
            })
        except FileNotFoundError:
            raise RuntimeError(f"Schema file not found for stream: {stream_name}")
        except json.JSONDecodeError:
            raise RuntimeError(f"Failed to parse schema for stream: {stream_name}")
        except Exception as e:
            raise RuntimeError(f"Error processing stream '{stream_name}': {e}")

    # Construct and return a Catalog object from the collected streams
    try:
        return Catalog.from_dict({"streams": streams})
    except Exception as e:
        raise RuntimeError(f"Failed to construct Catalog: {e}")

